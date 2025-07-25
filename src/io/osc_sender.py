from pythonosc import udp_client
from PySide6.QtCore import QObject, Signal

class OSCSender(QObject):
    trigger_blink = Signal()
    def __init__(self, ip, port):
        super().__init__()
        self.ip=ip
        self.port=port
        """
        Initialisiert den OSC Client.
        :param ip: IP-Adresse des OSC-Servers (Empfängers)
        :param port: Port des OSC-Servers
        """
        self.create_sender()

    def create_sender(self):
        self.client = udp_client.SimpleUDPClient(self.ip, self.port)
        # print(self.client)

    def send_message(self, address, *args):
        """
        Sendet eine OSC-Nachricht an die angegebene Adresse.
        :param address: OSC-Adresse (z. B. "/wek/inputs")
        :param args: Beliebig viele Werte, z. B. float, int, str
        """
        self.client.send_message(address, args)
        self.trigger_blink.emit()