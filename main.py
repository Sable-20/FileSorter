#cool stuff

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#if not using requirements.txt these two must be installed via pip

import os
import time
import json

class fileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with open("./config.json") as rf:
            data = json.load(rf)
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if filename.endswith(".png" or ".jpg" or ".jpeg" or ".webm"):
                folder_destination = data["image_folder"]
            elif filename.endswith(".mp4" or ".flv" or ".mov" or ".mkv"):
                folder_destination = data["video_folder"]
            elif filename.endswith(".txt" or ".pdf"):
                folder_destination = data["text_doc"]
            elif filename.endswith(".js"):
                folder_destination = data["js_folder"]
            elif filename.endswith(".py"):
                folder_destination = data["py_folder"]
            elif filename.endsiwth(".c" or ".cpp" or ".cs"):
                folder_destination = data["c_family"]
            elif filename.endswith(".go"):
                folder_destination = data["go_doc"]
            else:
                folder_destination = data["misc"]
            newDest = folder_destination + "/" + filename
            os.rename(src, newDest)

with open("configurations/config.json") as rf:
    data = json.load(rf)

folder_to_track = data["folder_to_track"]

event_handler = fileHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
