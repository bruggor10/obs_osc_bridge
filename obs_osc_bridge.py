import sys
from PySide6.QtWidgets import QApplication

from src.io.osc_receiver import OSCHandler
from src.io.osc_sender import OSCSender
from src.core.obs_bridge import OBS_Instance
from src.connector.connector import MainApp

sender = OSCSender(ip=None, port=None)

obs = OBS_Instance(ip=None, port=None, password=None, sender=sender)

osc_in = OSCHandler(port=None, obs_instance=obs)
def main():
    # osc_in.start_osc()
    # try:
    #     while True:
    #         time.sleep(1)
    #         # pass  # Keep main thread alive
    # except KeyboardInterrupt:
    #     osc_in.stop_osc()

    app = QApplication(sys.argv)
    window = MainApp(osc_in, sender, obs)
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
