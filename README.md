# obs_osc_bridge
Bridge to control OBS- Studio via OpenSoundControl.

## Features:
Connection to OBS via Websockets, and generic OpenSoundControl (OSC) for controlling the OBS instance. Connection parameters as IP addresses, ports and Websocket Passwords can be saved and loaded from within the user interface

### available functions for controlling OBS:
- Switching preview scenes:
    - /previewscene [name of scene] 
        - example: "/previewscene my_scene"
- Switching program scenes:
    - /programscene [name of scene]
        - example: "/programscene my_scene"
- Toggle streaming:
    - /stream [0/1]
        - example: "/stream 1"
- Toggle recording:
    - /recording [0/1]
        - example: "/recording 1"
- Set transition duration:
    - /transition:_duration [duration]
        - example_ "/transition_duration 2000"
- Get list of available scenes:
    - /get_scene_list 1
- Get items of a scene:
    - /get_scene_item_list [name of scene]
        - example: "/get_scene_item_list my_scene"
- Enable or disable items of a scene:
    - /enable_scene_item [name of scene] [item number] [0/1]
        - example: "/enable_scene_item my_scene 3 1". This will enable item number 3 in scene "my_scene". You can get a numbered list of scene items with "/get_scene_item_list", see above.

# How to run the program
## Prebuilt package (Linux)
Go to the release section and download the executable. Make it executable
### Create a virtual environment and install the requirements:
You need python3 and python3-venv for this.
then, git clone the repo, create a virtual environment and source into it with the following commands:
```
git clone https://github.com/bruggor10/obs_osc_bridge.git
cd obs_osc_bridge/
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

### run the program:
#### from dev environment
Source into the virtual environment and run it: (make sure the path is correct)
```
source .env/bin/activate
python3 obs_osc_bridge.py
```
#### build instructions
If you want to create an executable, follow the steps above and source into the development environment. Build the program with `pyinstaller --onefile obs_osc_bridge.py`
