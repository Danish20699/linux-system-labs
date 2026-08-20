# Linux Nano Editor Commands

## Objective

To practice creating, editing, saving, and exiting a text file using the Nano editor in Linux.

## Prerequisites

- Ubuntu/Linux system
- Terminal access
- Nano editor
- Basic Linux command-line knowledge

## Commands Used

### 1. Create a Lab Directory

```bash
mkdir lab12
cd lab12
2. Change Directory
cd lab12
Moves into the lab12 directory.
3. Open or Create a File Using Nano
nano demo.txt
Opens demo.txt in the Nano text editor. If the file does not exist, Nano creates it when the file is saved.
4. Save the File
Ctrl + O
Saves the changes made to the file. Nano asks for the filename before saving.
5. Exit Nano
Ctrl + X
Exits the Nano editor.
6. Display File Contents
cat demo.txt
Displays the contents of demo.txt in the terminal.
7. Display File Details
ls -l demo.txt
Displays detailed information about the file, including permissions, ownership, size, and modification time.
Step-by-Step Walkthrough
Step 1 — Create the Lab Directory
mkdir lab12
A directory named lab12 was created.
Step 2 — Enter the Directory
cd lab12
The terminal was moved into the lab12 directory.
Step 3 — Create and Open the File
nano demo.txt
The demo.txt file was opened using the Nano editor.
Step 4 — Enter Text
The following content was entered into the Nano editor:
Linux Nano Editor Lab
This file was created using the Nano editor.
I am practicing Linux text editing commands.
Step 5 — Save the File
The file was saved using:
Ctrl + O
The filename was confirmed by pressing Enter.
Step 6 — Exit Nano
Nano was closed using:
Ctrl + X
Step 7 — Edit the File Again
The file was reopened:
nano demo.txt
An additional line was added:
Nano is a simple terminal-based text editor.
The changes were saved using:
Ctrl + O
and the editor was closed using:
Ctrl + X
Step 8 — Verify the File
The final contents were checked using:
cat demo.txt
The file details were checked using:
ls -l demo.txt
Common Errors & Fixes
Unable to Exit Nano
If Nano does not close, press:
Ctrl + X
If Nano asks whether to save changes, press:
Y
Then press Enter to confirm the filename.
File Not Found
If the file cannot be found, check the current directory:
pwd
Then list the files:
ls
Result
A text file was successfully created and edited using the Nano editor. The file was saved, reopened, modified, and verified using Linux commands.
```
