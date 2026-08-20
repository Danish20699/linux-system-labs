# Linux VI Editor Commands

## Objective

To practice creating, editing, saving, and exiting a text file using the VI editor in Linux.

## Prerequisites

- Ubuntu/Linux system
- Terminal access
- VI editor installed

## Commands Used

### 1. Create Lab Directory

```bash
mkdir lab11
```

Creates a directory named `lab11`.

### 2. Change Directory

```bash
cd lab11
```

Moves into the `lab11` directory.

### 3. Open or Create a File with VI

```bash
vi demo.txt
```

Opens `demo.txt` in the VI editor. If the file does not exist, VI creates it when the file is saved.

### 4. Insert Mode

```text
i
```

Enters Insert Mode, allowing text to be typed into the file.

### 5. Command Mode

```text
Esc
```

Returns from Insert Mode to VI's Command Mode.

### 6. Save and Exit

```text
:wq
```

Writes/saves the file and exits the VI editor.

### 7. Display File Contents

```bash
cat demo.txt
```

Displays the contents of `demo.txt` in the terminal.

### 8. Display File Details

```bash
ls -l demo.txt
```

Displays detailed information about the file, including permissions, ownership, size, and modification time.

## Step-by-Step Walkthrough

### Step 1 — Create the Lab Directory

```bash
mkdir lab11
```

A directory named `lab11` was created.

### Step 2 — Enter the Directory

```bash
cd lab11
```

The terminal was moved into the `lab11` directory.

### Step 3 — Create and Open the File

```bash
vi demo.txt
```

The `demo.txt` file was opened using the VI editor.

### Step 4 — Enter Text

The `i` key was pressed to enter Insert Mode.

The following content was entered:

```text
Linux VI Editor Lab
This file was created using the VI editor.
I am practicing Linux text editing commands.
```

### Step 5 — Save and Exit

The `Esc` key was pressed to return to Command Mode.

The following command was then used:

```text
:wq
```

The file was saved and VI was closed.

### Step 6 — Verify the File

The file contents were checked using:

```bash
cat demo.txt
```

The file details were checked using:

```bash
ls -l demo.txt
```

## Screenshots

### VI Editor Practical

![Linux VI Editor](screenshots/linux-vi-editor.png)

The screenshot shows the VI editor practical and the successful file verification.

## Key Learnings

- VI is a terminal-based text editor available on Linux.
- `i` is used to enter Insert Mode.
- `Esc` returns to Command Mode.
- `:wq` saves the file and exits VI.
- `cat` can be used to verify the saved file contents.
- `ls -l` can be used to inspect file details.

## Common Errors & Fixes

### Accidentally Stuck Inside VI

If the editor is open and you need to exit:

```text
Esc
```

Then save and exit:

```text
:wq
```

### Exit Without Saving

If changes should not be saved:

```text
Esc
:q!
```

## Result

A text file was successfully created and edited using the Linux VI editor. The file was saved, exited from VI, and verified using Linux commands.
