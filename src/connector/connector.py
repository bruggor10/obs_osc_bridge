# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PySide6.QtCore import QTimer
# from ..gui.ui_main import Ui_MainWindow
from ..io.osc_receiver import *
import sys

class MainApp(QMainWindow):
    def __init__(self, osc_in, model, sender, recorder):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.osc_in=osc_in
        self.osc_out = sender
        self.model = model
        self.rec = recorder

        self.ui.models.currentIndexChanged.connect(self.model_selected)     
        self.ui.model_type_classifiers.toggled.connect(self.classifiers_checked)
        self.ui.model_type_regressors.toggled.connect(self.regressors_checked)
        self.ui.model_type_classifiers.setChecked(True)
        
        # blink widgets
        self.input_blink_widget = BlinkWidget(self.ui.data_in_blink, role='blink')
        self.output_blink_widget = BlinkWidget(self.ui.data_out_blink, role='blink')
        self.model_trainingstatus = BlinkWidget(self.ui.model_trainingstatus, role='led')
        self.model_runstatus = BlinkWidget(self.ui.model_runstatus, role='led')
        self.rec_led = BlinkWidget(self.ui.rec_status, role='led')

        self.osc_in.run_led.connect(self.model_runstatus.toggle)
        self.osc_in.trigger_blink.connect(self.input_blink_widget.start_blinking)
        self.osc_out.trigger_blink.connect(self.output_blink_widget.start_blinking)
        self.model.toggle_trainingstate.connect(self.model_trainingstatus.toggle)
        self.osc_in.rec_led.connect(self.rec_led.toggle)

        # init textfields for osc connection
        self.ui.receiver_port.setText(str(self.osc_in.port))
        self.ui.sender_ip.setText(str(self.osc_out.ip))
        self.ui.sender_port.setText(str(self.osc_out.port))
        # buttons
        self.ui.train_btn.clicked.connect(self.on_train_btn)
        self.ui.run_btn.clicked.connect(self.on_run_btn)
        self.ui.record_btn.clicked.connect(self.on_rec_btn)
        self.ui.connect_btn.clicked.connect(self.on_connect_osc)
        
    def model_selected(self,index):
        selection = self.ui.models.currentText()
        all_models = dict(self.model.get_classifiers()) | dict(self.model.get_regressors())
        key = next((k for k, v in all_models.items() if v == selection), None)
        if key: self.model.configure_model(model_type=key)

    def classifiers_checked(self, checked):
        if checked:
            self.ui.models.clear()
            self.ui.models.addItems(list(k for v, k in self.model.get_classifiers())) 
    
    def regressors_checked(self, checked):
        if checked:
            self.ui.models.clear()
            self.ui.models.addItems(list(k for v, k in self.model.get_regressors())) 
    
    
    def closeEvent(self, event):
        # Eigene Funktion ausführen
        self.on_close()

        # Fenster trotzdem schließen lassen
        event.accept()

        # Wenn du das Schließen verhindern willst, verwende: event.ignore()

    def on_close(self):
        # Beispielhafte Funktion beim Schließen
        print("Fenster wird geschlossen. Aufräumen oder Speichern ...")
        self.osc_in.stop_osc()
        # Optional z.B. ein Dialog:
        # QMessageBox.information(self, "Bye!", "Das Fenster wird jetzt geschlossen.")


# ====== BTNS =====
    def on_rec_btn(self):
        recstate = not bool(self.rec.is_recording)
        self.osc_in.recorder_handler(None, recstate)

    def on_run_btn(self):
        runstate = not bool(self.model.is_running)
        self.osc_in.run_handler(None, runstate)

    def on_train_btn(self):
        try:
            self.osc_in.train_handler()
        except ValueError as e:
            QMessageBox.critical(self, "Fehler", str(e))

    def on_connect_osc(self):
        try:
            if self.ui.receiver_port.text()== '' or self.ui.sender_ip.text()=='' or self.ui.sender_port.text()=='':
                raise ValueError('ein oder mehrere Felder leer')
            self.osc_in.port = int(self.ui.receiver_port.text())
            self.osc_out.port = int(self.ui.sender_port.text())
            self.osc_out.ip = self.ui.sender_ip.text()
            self.osc_out.create_sender()
            self.osc_in.stop_osc()
            self.osc_in.start_osc()
            QMessageBox.information(self, 'Verbindung erfolgreich', f"Verbunden! Sender IP {self.osc_out.ip}, Sender Port {self.osc_out.port}")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", str(e))
class BlinkWidget(QTimer):
    def __init__(self, widget, role):
        super().__init__(widget)
        # init blink widget
        self.state = False
        self.role = role
        self.blink_widget = widget
        self.default_stylesheet = self.blink_widget.styleSheet()
        self.blink_duration_timer = QTimer(self)
        self.blink_duration_timer.setSingleShot(True)
        self.blink_duration_timer.timeout.connect(self.stop_blinking)
    
    # === BLINK WIDGET ===
    def start_blinking(self):
        self.state = True
        self.update()
        
    def stop_blinking(self):
        self.state=False
        self.update()
        
    def toggle(self, toggle):
        self.state = toggle
        self.update()

    def update(self):
        if self.state:
            self.blink_widget.setStyleSheet(self.default_stylesheet + "background-color: rgba(151, 243, 132, 1);")
            if self.role=='blink':
                self.blink_duration_timer.start(300)  # 3mm ms lang leuchten
        else:
            self.blink_widget.setStyleSheet(self.default_stylesheet)  # zurücksetzen