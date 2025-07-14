# Python File Organizer

## Overview
The Python File Organizer is a simple script that helps users organize files in their Downloads directory based on file types. It automatically sorts files into designated folders such as Images, Videos, Documents, Audio, and Archives, making it easier to manage and locate files.

## Functionality
- Scans the Downloads directory for files.
- Identifies file types based on their extensions.
- Moves files into corresponding folders:
  - Images: .jpg, .jpeg, .png, .gif, .bmp
  - Videos: .mp4, .mkv, .avi, .mov
  - Documents: .pdf, .docx, .txt, .pptx
  - Audio: .mp3, .wav, .aac
  - Archives: .zip, .rar, .tar.gz
  - Python Script: .py .pynb

- Skips files with unknown extensions and directories.

## Setup
1. Clone the repository to your local machine:
   ```
   git clone <>
   ```
2. Navigate to the project directory:
   ```
   cd python-file-organizer
   ```

## Usage
1. Ensure you have Python installed on your machine.
2. Run the script:
   ```
   python src/Fmain.py
   ```
3. Check your Downloads directory for organized files.

## Requirements
This project uses the Python standard library, so no additional dependencies are required.
