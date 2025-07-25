from pythonosc import dispatcher
from pythonosc import osc_server
# from PySide6.QtCore import QObject, Signal
# from PySide6.QtWidgets import QMessageBox
import threading

class OSCReceiver:
    def __init__(self, ip, port):
        """
        Initialisiert den OSC Server.
        :param ip: IP-Adresse zum Binden (meist 0.0.0.0 für alle)
        :param port: Port, auf dem der Server horcht
        """
        self.ip = ip
        self.port = port
        self.dispatcher = dispatcher.Dispatcher()
        self.server = None
        self.thread = None
        self.message_handler = None



    def add_handler(self, address, handler_func):
        """
        Fügt einen Handler für eine bestimmte OSC-Address hinzu.
        :param address: OSC-Adresse (z.B. "/synthedge/inputs")
        :param handler_func: Funktion mit Signatur handler_func(address, *args)
        """
        self.dispatcher.map(address, handler_func)

    def start(self):
        """
        Startet den OSC-Server in einem separaten Thread.
        """
        self.server = osc_server.ThreadingOSCUDPServer((self.ip, self.port), self.dispatcher)
        print(f"OSC Server läuft auf {self.ip}:{self.port}")
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def stop(self):
        """
        Stoppt den OSC-Server.
        """
        if self.server:
            self.server.shutdown()
            self.thread.join()
            print("OSC Server gestoppt.")

    
                


# class OSCHandler(QObject):
class OSCHandler():
    # trigger_blink = Signal()
    def __init__(self, obs_instance, port):
        # super().__init__()
        self.ip = "0.0.0.0"
        self.port = port
        self.obs_instance = obs_instance


    # ============ Handlers ==========
    def previewscene_handler(self, address, scene):
        print(scene)
       
    def programscene_handler(self, address, scene):
        print(f"Programscene: {scene}")
        self.obs_instance.switch_programscene(scene)

    def stream_handler(self, address, streamstate):
        if bool(streamstate):
            self.obs_instance.start_stream()
        else:
            self.obs_instance.stop_stream()

    def recording_handler(self, address, recstate):
        if bool(recstate):
            self.obs_instance.start_record()
        else:
            self.obs_instance.stop_record()

    def start_osc(self):
        ## handle OSC Inputs
        self.receiver = OSCReceiver(ip=self.ip, port=self.port)
        self.receiver.add_handler("/previewscene", self.previewscene_handler)
        self.receiver.add_handler("/programscene", self.programscene_handler)
        self.receiver.add_handler("/stream", self.stream_handler)
        self.receiver.add_handler("/recording", self.recording_handler)
        self.receiver.start()

    def stop_osc(self):
        ## stop osc receiving thread
        self.receiver.stop()
        