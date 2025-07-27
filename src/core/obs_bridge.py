import socket
import obsws_python as obs

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
            print("Verbindung zu OBS erfolgreich hergestellt.")

        except ConnectionRefusedError:
            print("Fehler: Keine Verbindung zu OBS möglich. Ist OBS gestartet und WebSocket aktiviert?")

        except TimeoutError:
            print("Fehler: Zeitüberschreitung beim Verbindungsaufbau zu OBS.")

        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")


    def error_handler(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                err = f"error:{type(e).__name__}:{str(e)}"
                print(f"❌ {err}")
                return None
        return wrapper

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






    # elif msg.startswith("get_scene_item_list:"):
    #     requested_scene = msg.split(":")[1]
    #     sock_out.sendto(f"Available items in {requested_scene}:".encode(), PD_SEND_ADDR)
    #     for item in ws.get_scene_item_list(requested_scene).scene_items:
    #         sock_out.sendto(item["sourceName"].encode(), PD_SEND_ADDR)

    # elif msg.startswith("enable_scene_item:"):
    #     requested_scene = msg.split(":")[1]
    #     requested_item = msg.split(":")[2]
    #     item_id =get_scene_item_id(requested_scene, requested_item)
    #     ws.set_scene_item_enabled(requested_scene, item_id, True)
    #     sock_out.sendto(f"ok:enabled {requested_item} in scene {requested_scene}".encode(), PD_SEND_ADDR)

    # elif msg.startswith("disable_scene_item:"):
    #     requested_scene = msg.split(":")[1]
    #     requested_item = msg.split(":")[2]
    #     item_id =get_scene_item_id(requested_scene, requested_item)
    #     ws.set_scene_item_enabled(requested_scene, item_id, False)
    #     sock_out.sendto(f"ok:disabled {requested_item} in scene {requested_scene}".encode(), PD_SEND_ADDR)



    # else:
    #     sock_out.sendto(f"error:unknown_command:{msg}".encode(), PD_SEND_ADDR)





