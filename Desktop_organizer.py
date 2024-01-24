from os import scandir, rename
from os.path import splitext, exists, join
from time import sleep
from shutil import move
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


Download_dir = r"E:"
dest_dir_image = r"C:\Users\vidya\Pictures\Downloaded Images"
dest_dir_video = r"C:\Users\vidya\Videos\Downloaded videos"
dest_dir_sfx = r"C:\Users\vidya\Audios"
dest_dir_documents = r"C:\Users\vidya\Documents\Downloads"
dest_dir_music = r"C:\Users\vidya\Music\Downloaded Musics"
dest_dir_pyfiles = r"E:\Python Files"


# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

python_extensions = [".py", ".ipynb", ".pyi",
                     ".pyc", ".pyd", ".pyo", ".pyw", ".pyz"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, name)
        rename(old_name, new_name)
    move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # ? .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(Download_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_python_files(entry, name)

    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:  # 10megabytes
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file:  {name}")

    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                dest = dest_dir_video
                move_file(dest, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                dest = dest_dir_image
                move_file(dest, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):
        for document_extension in document_extensions:
            if name.endswith(document_extension) or name.endswith(document_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_python_files(self, entry, name):
        for pyfiles_extension in python_extensions:
            if name.endswith(pyfiles_extension) or name.endswith(pyfiles_extension.upper()):
                move_file(dest_dir_pyfiles, entry, name)
                logging.info(f"Moved python file: {name}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    path = Download_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            """choice = input("Enter 'stop' to stop the program: ")
            if choice.lower() == 'stop':
                break"""
            sleep(10)
    except KeyboardInterrupt:
        # pass
        observer.stop()
    observer.join()
