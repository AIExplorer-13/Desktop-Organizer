# Desktop-Organizer
Automate your Desktop File Management and declutter your Downloads Folder. This app will automatically organize &amp; move your downloads into folders based on file type


This Python script is designed to organize files in a specified directory (Download_dir) based on their types. It utilizes the watchdog library to monitor file system events and automatically categorizes files into designated destination directories (dest_dir_image, dest_dir_video, dest_dir_sfx, dest_dir_documents, dest_dir_music).


Usage
Set up Directories:
Update the paths for Download_dir, dest_dir_image, dest_dir_video, dest_dir_sfx, dest_dir_documents, and dest_dir_music with the appropriate directories on your system.


Observing File Organization:
The script will continuously run, monitoring the specified Download_dir for changes. When new files are added or existing files are modified, the script will organize them into the specified destination directories based on their types.


Terminating the Script:
To stop the script, enter 'stop' to in terminal or press Ctrl+C in the terminal.


Supported File Types
Images: .jpg, .jpeg, .jpe, .jif, .jfif, .jfi, .png, .gif, .webp, .tiff, .tif, .psd, .raw, .arw, .cr2, .nrw, .k25, .bmp, .dib, .heif, .heic, .ind, .indd, .indt, .jp2, .j2k, .jpf, .jpf, .jpx, .jpm, .mj2, .svg, .svgz, .ai, .eps, .ico

Videos: .webm, .mpg, .mp2, .mpeg, .mpe, .mpv, .ogg, .mp4, .mp4v, .m4v, .avi, .wmv, .mov, .qt, .flv, .swf, .avchd

Audio: .m4a, .flac, .mp3, .wav, .wma, .aac

Documents: .doc, .docx, .odt, .pdf, .xls, .xlsx, .ppt, .pptx



 -----MAIN PROGRAM-----

The given code is a Python script that utilizes the `watchdog` library to monitor file system events in a specified directory. Here's a breakdown of the code:

1. The script imports necessary modules:
   - `sys` and `time` are standard Python modules.
   - `logging` is used for logging events.
   - `watchdog.observers` and `watchdog.events` are part of the `watchdog` library, which provides a way to monitor file system events.

2. The script sets up logging configuration using `logging.basicConfig()`, which determines the logging format and level.

3. It checks if a directory path is provided as a command line argument. If provided, it uses that directory; otherwise, it defaults to the current directory.

4. It creates a `LoggingEventHandler` object for handling file system events.

5. It creates an `Observer` object, which is responsible for scheduling the event handler and starting the event monitoring process.

6. The script enters a `while` loop with a `try` block that continuously sleeps for 1 second to keep the script running and allow the observer to monitor file system events.

7. Finally, there's a `finally` block that stops the observer and joins it, ensuring proper cleanup when the script is terminated.

In summary, this script sets up a file system event monitoring system using the `watchdog` library, logging events as they occur.  
