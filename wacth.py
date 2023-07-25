import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import PyPDF2
import os

class Watcher:
    
    DIRECTORY_TO_WATCH = "./pdf"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer stopped")
        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print(f"New file {event.src_path} has been created!")
            exec(open("pdf_to_txt.py").read())

if __name__ == '__main__':
    w = Watcher()
    w.run()
