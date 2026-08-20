# Linux File Management Commands

## Objective

To practice basic Linux file and directory management operations, including creating, viewing, copying, renaming, moving, and deleting files and directories.

## Prerequisites

- Ubuntu/Linux system
- Terminal access
- Basic Linux command knowledge

## Commands Used

### 1. `mkdir`

```bash
mkdir lab10
```

Creates a new directory named `lab10`.

### 2. `ls`

```bash
ls
```

Lists files and directories in the current location.

### 3. `cd`

```bash
cd lab10
```

Changes the current working directory to `lab10`.

### 4. `pwd`

```bash
pwd
```

Displays the absolute path of the current working directory.

### 5. `touch`

```bash
touch demo.txt
```

Creates an empty file named `demo.txt`.

### 6. `ls -l`

```bash
ls -l
```

Displays files and directories in detailed long-list format, including permissions, ownership, size, and modification time.

### 7. `echo`

```bash
echo "Linux file management lab" > demo.txt
```

Writes text into `demo.txt`. The `>` operator redirects the output into the file.

### 8. `cat`

```bash
cat demo.txt
```

Displays the contents of a text file.

### 9. `cp`

```bash
cp demo.txt copy.txt
```

Creates a copy of `demo.txt` named `copy.txt`.

### 10. `mv`

```bash
mv copy.txt renamed.txt
```

Moves or renames a file. In this case, `copy.txt` is renamed to `renamed.txt`.

### 11. Create a Backup Directory

```bash
mkdir backup
```

Creates a directory named `backup`.

### 12. Move a File

```bash
mv renamed.txt backup/
```

Moves `renamed.txt` into the `backup` directory.

### 13. Verify Directory Contents

```bash
ls -l backup
```

Displays the files stored inside the `backup` directory.

### 14. Remove a File

```bash
rm demo.txt
```

Deletes the specified file.

### 15. Move to Parent Directory

```bash
cd ..
```

Moves from the current directory to its parent directory.

### 16. Remove a Directory

```bash
rm -r lab10
```

Removes the `lab10` directory and its contents recursively.

## Step-by-Step Walkthrough

1. Created a working directory named `lab10` using `mkdir`.
2. Verified the directory using `ls`.
3. Entered the directory using `cd`.
4. Verified the current location using `pwd`.
5. Created a test file using `touch`.
6. Added sample text to the file using `echo`.
7. Displayed the file contents using `cat`.
8. Created a copy of the file using `cp`.
9. Renamed the copied file using `mv`.
10. Created a `backup` directory.
11. Moved the renamed file into the `backup` directory.
12. Verified the contents of the backup directory using `ls -l`.
13. Removed the test file using `rm`.
14. Returned to the parent directory using `cd ..`.
15. Removed the test directory using `rm -r`.

## Screenshots

### Practical Execution

The screenshot below shows the execution and results of the Linux file-management commands performed during this lab.

![Linux File Management Practical](screenshots/linux-file-management.png)

## Common Errors & Fixes

### Error: `Not a directory`

While moving the file into `backup/`, the following error was encountered:

```text
mv: cannot move 'renamed.txt' to 'backup/': Not a directory
```

**Cause:** The target `backup` was not a directory.

**Fix:** The directory was checked and then created correctly using:

```bash
mkdir backup
```

The file was then moved successfully:

```bash
mv renamed.txt backup/
```

### Error: `No such file or directory`

The following error was also encountered while trying to remove `backup`:

```text
rm: cannot remove 'backup': No such file or directory
```

**Cause:** The `backup` directory did not exist at that point.

**Fix:** The directory was created using:

```bash
mkdir backup
```

## Key Learnings

- `mkdir` creates directories.
- `ls` and `ls -l` are used to inspect files and directories.
- `cd` changes directories.
- `pwd` displays the current location.
- `touch` creates files.
- `echo` can write text to files.
- `cat` displays file contents.
- `cp` copies files.
- `mv` moves or renames files.
- `rm` removes files.
- `rm -r` removes directories recursively.
- Linux file-management commands can be combined to perform practical file operations.

## Result

The Linux file-management operations were successfully performed, including directory creation, file creation, file modification, copying, renaming, moving, and deletion.
