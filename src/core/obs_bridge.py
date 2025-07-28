import socket
import obsws_python as obs
from PySide6.QtWidgets import QMessageBox


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            msg = str(e)
            self=args[0]
            self.sender.send_message("/obs_bridge_error", msg)
            return None
    return wrapper

class OBS_Instance:
    def __init__(self,ip,port,password, sender):
        self.ip = ip
        self.port = port
        self.password = password
        self.sender = sender
        # self.connect_to_obs()



    def get_scene_item_id(_req_scene, _req_item):
        for item in ws.get_scene_item_list(_req_scene).scene_items:
            if _req_item in item["sourceName"]:
                return int(item["sceneItemId"])

    def get_scene_uuid(_req_scene):
        for scene in ws.get_scene_list().scenes:
            if _req_scene in scene["sceneName"]:
                return scene["sceneUuid"]



    # OBS-WebSocket Verbindung
    def connect_to_obs(self):
        try:
            self.ws = obs.ReqClient(
                host=self.ip,
                port=self.port,
                password=self.password,
                timeout=3
            )
            print("Connection to OBS successful.")

        except ConnectionRefusedError:
            raise ConnectionRefusedError("Error: Unable to connect to OBS. Is OBS running and is WebSocket enabled?")
        except TimeoutError:
            raise TimeoutError("Fehler: Connection timeout")
        except Exception as e:
            raise Exception("An unexpected error occurred: {e}")



    @error_handler
    def switch_programscene(self, scene):
        self.ws.set_current_program_scene(scene)
        
    @error_handler
    def switch_previewscene(self, scene):
        self.ws.set_current_preview_scene(scene)
    
    @error_handler
    def start_stream(self):
        self.ws.start_stream()

    @error_handler
    def stop_stream(self):
        self.ws.stop_stream()      

    @error_handler
    def start_record(self):
        self.ws.start_record()

    @error_handler
    def stop_record(self):
        self.ws.stop_record() 
    
    @error_handler
    def set_transitionduration(self, duration):
        self.ws.set_current_scene_transition_duration(duration)

    @error_handler
    def get_scene_list(self, *_args, **_kwargs):
        scenelist = self.ws.get_scene_list()
        for scene in scenelist.scenes:
            self.sender.send_message("/obs_osc_bridge/available_scenes", scene['sceneName'])

    @error_handler
    def get_scene_item_list(self, scene):
        for item in self.ws.get_scene_item_list(scene).scene_items:
            self.sender.send_message("/obs_osc_bridge/available_scene_items", item['sceneItemId'], item['sourceName'])


    @error_handler
    def enable_scene_item(self, scene, item, state):
        self.ws.set_scene_item_enabled(scene, item, state)
