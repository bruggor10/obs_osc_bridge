from src.io.osc_receiver import OSCHandler
from src.core.obs_bridge import OBS_Instance

obs = OBS_Instance('127.0.0.1', port=4455, password="2hS89ET4bSoFJEhD")
osc_in = OSCHandler(port=8001, obs_instance=obs)
def main():
    osc_in.start_osc()

    try:
        while True:
            pass  # Keep main thread alive
    except KeyboardInterrupt:
        osc_in.stop_osc()

if __name__ == "__main__":
    main()