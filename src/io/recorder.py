import numpy as np
from threading import Lock

class Recorder:
    def __init__(self, input_dim, auto_label=True):
        """
        Initialisiert den Recorder.
        :param input_dim: Anzahl der Input-Features pro Datenpunkt
        :param auto_label: Wenn True, wird ein Zähler als Label verwendet
        """
        self.inputs = []
        self.labels = []
        self.current_label = 0
        self.input_dim = input_dim
        self.lock = Lock()
        self.auto_label = auto_label
        self.is_recording = False

    def add_input(self, data):
        """
        Fügt einen neuen Eingabevektor hinzu.
        :param data: Tuple oder Liste mit Features (z. B. vom OSC-Handler)
        """
        if len(data) != self.input_dim:
            print(f"⚠️ Erwartet {self.input_dim} Werte, aber bekommen: {len(data)}")
            return

        with self.lock:
            self.inputs.append(list(data))
            if self.auto_label:
                self.labels.append(self.current_label)
            else:
                self.labels.append(None)  # Kann später gesetzt werden
            print(f"✅ Eingabe aufgenommen: {data}")

    def set_label(self, label):
        """
        Setzt das aktuelle Label, das beim nächsten Input verwendet wird.
        :param label: z. B. int oder str
        """
        with self.lock:
            self.current_label = label
            print(f"🔖 Aktuelles Label gesetzt: {label}")

    def save(self, input_path="inputs.npy", label_path="labels.npy"):
        """
        Speichert die aufgenommenen Daten.
        """
        with self.lock:
            X = np.array(self.inputs)
            y = np.array(self.labels)
            np.save(input_path, X)
            np.save(label_path, y)
            print(f"💾 Daten gespeichert unter: {input_path}, {label_path}")

    def reset(self):
        """
        Setzt die Aufnahme zurück.
        """
        with self.lock:
            self.inputs = []
            self.labels = []
            print("🔄 Aufnahme zurückgesetzt.")

    def load(self, input_path="inputs.npy", label_path="labels.npy"):
        """
        Lädt gespeicherte Daten aus .npy Dateien und ersetzt die aktuellen Inhalte.
        """
        with self.lock:
            try:
                self.inputs = np.load(input_path).tolist()
                self.labels = np.load(label_path).tolist()
                print(f"📂 Daten geladen aus: {input_path}, {label_path}")
            except FileNotFoundError:
                print(f"⚠️ Dateien nicht gefunden: {input_path} oder {label_path}")
            except Exception as e:
                print(f"⚠️ Fehler beim Laden: {e}")

    def get_data(self):
        X = np.array(self.inputs)
        y = np.array(self.labels)
        return X, y