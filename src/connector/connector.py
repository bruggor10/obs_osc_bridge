from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import QTimer
from ..gui.ui_main import Ui_MainWindow
from ..io.osc_receiver import *
from ..core.obs_bridge import OBS_Instance
import sys
import configparser

class MainApp(QMainWindow):
    def __init__(self, sender, osc_in, obs_instance):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.obs = obs_instance
        self.osc_in=osc_in
        self.osc_out = sender
        
        # buttons
        self.ui.connect_btn.clicked.connect(self.on_connect_btn)
        self.ui.save_btn.clicked.connect(self.on_save_btn)
        self.ui.load_btn.clicked.connect(self.on_load_btn)

    def closeEvent(self, event):
        self.on_close()
        event.accept()

    def on_close(self):
        print("Closing Window")
        self.osc_in.stop_osc()
# ====== BTNS =====
    def on_connect_btn(self):
        try:
            if any(field.text() == '' for field in [self.ui.receiver_port, self.ui.sender_ip, self.ui.sender_port, self.ui.obs_ip, self.ui.obs_port]):
                raise ValueError('one or more fields empty')
            self.osc_in.port = int(self.ui.receiver_port.text())
            self.osc_out.port = int(self.ui.sender_port.text())
            self.osc_out.ip = self.ui.sender_ip.text()
            self.osc_out.create_sender()
            if self.osc_in.running:
                self.osc_in.stop_osc()
            self.osc_in.start_osc()
            self.obs.ip = self.ui.obs_ip.text()
            self.obs.port = int(self.ui.obs_port.text())
            self.obs.password = self.ui.obs_pass.text()
            self.obs.connect_to_obs()
            if self.obs:
                QMessageBox.information(self, 'Connected successfully!', f"Connected! Sender IP {self.osc_out.ip}, Sender Port {self.osc_out.port}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_save_btn(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Konfigurationsdatei speichern",
            "",
            "Konfigurationsdateien (*.ini);;Alle Dateien (*)"
        )
        if filename:
            if not filename.endswith(".ini"):
                filename += ".ini"
            # print(f"Ausgewählte Datei zum Speichern: {filename}")
            config = configparser.ConfigParser()
            config['Settings'] = {
                'osc_in_port': self.ui.receiver_port.text(),
                'osc_out_port': self.ui.sender_port.text(),
                'osc_out_ip': self.ui.sender_ip.text(),
                'obs_ip': self.ui.obs_ip.text(),
                'obs_port': self.ui.obs_port.text(),
                'obs_pass': self.ui.obs_pass.text(),
            }

            # Speichern
            with open(filename, 'w') as configfile:
                config.write(configfile)


    def on_load_btn(self):
            filename, _ = QFileDialog.getOpenFileName(
                self,
                "Konfigurationsdatei laden",
                "",
                "Konfigurationsdateien (*.json *.ini *.yaml *.yml);;Alle Dateien (*)"
            )
            if filename:
                print(f"Ausgewählte Datei zum Laden: {filename}")

                # Laden
                try: 
                    config = configparser.ConfigParser()
                    config.read(filename)
                    self.ui.receiver_port.setText(config['Settings']['osc_in_port'])
                    self.ui.sender_ip.setText(config['Settings']['osc_out_ip'])
                    self.ui.sender_port.setText(config['Settings']['osc_out_port'])
                    self.ui.obs_ip.setText(config['Settings']['obs_ip'])
                    self.ui.obs_pass.setText(config['Settings']['obs_pass'])
                    self.ui.obs_port.setText(config['Settings']['obs_port'])
                except Exception as e:
                    QMessageBox.critical(self, "Error", "Error reading file!")