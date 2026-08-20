# Setup PostgreSQL and Create Database for College with Student Table

## Objective

To install and configure the PostgreSQL relational database management system (`postgresql`) on Ubuntu/Linux, manage its system service, access the interactive `psql` shell, create a dedicated database named `college_db`, define a schema and create a `students` table with primary keys and constraints, insert records, and query data.

## Prerequisites

- Ubuntu / Debian-based Linux operating system
- Terminal access
- User account with `sudo` privileges
- Basic familiarity with Linux command line and SQL fundamentals

---

## Commands Used

### 1. Update Package Repository

```bash
sudo apt update
```

Refreshes the local package index to ensure the latest versions and package metadata are fetched from Ubuntu repositories.

### 2. Install PostgreSQL and Contrib Utilities

```bash
sudo apt install postgresql postgresql-contrib -y
```

Installs the PostgreSQL database server and additional extension utilities.

### 3. Manage PostgreSQL Service

```bash
sudo systemctl start postgresql
sudo systemctl status postgresql
```

Starts the PostgreSQL service and verifies that it is active and running.

### 4. Access PostgreSQL Interactive Terminal (`psql`)

```bash
sudo -i -u postgres psql
```

Switches to the default administrative `postgres` system user and directly enters the interactive PostgreSQL shell prompt (`postgres=#`).

### 5. Create College Database

```sql
CREATE DATABASE college_db;
```

Creates a new relational database named `college_db`.

### 6. Connect / Switch to the Database

```sql
\c college_db
```

Connects to `college_db` as the active working database.

### 7. Create `students` Table

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    course VARCHAR(50),
    enrollment_date DATE DEFAULT CURRENT_DATE
);
```

Defines the table structure with columns:
- `student_id`: Auto-incrementing unique identifier (Primary Key).
- `first_name` & `last_name`: Student names (Mandatory string).
- `email`: Student email address (Unique & Mandatory).
- `course`: Enrolled academic program.
- `enrollment_date`: Date of admission (Defaults to current date).

### 8. Inspect Table Structure and List Tables

```sql
\dt
\d students
```

- `\dt`: Lists all tables in the current database.
- `\d students`: Displays the schema, data types, and modifiers for the `students` table.

### 9. Insert Student Records

```sql
INSERT INTO students (first_name, last_name, email, course) VALUES
('John', 'Doe', 'john.doe@college.edu', 'Computer Science'),
('Jane', 'Smith', 'jane.smith@college.edu', 'Information Technology'),
('Alex', 'Johnson', 'alex.j@college.edu', 'Data Science'),
('Emily', 'Davis', 'emily.davis@college.edu', 'Cybersecurity');
```

Inserts sample rows into the `students` table.

### 10. Query Table Records

```sql
SELECT * FROM students;
```

Retrieves and displays all rows and columns stored in the `students` table in tabular format.

### 11. Exit `psql`

```sql
\q
```

Exits the PostgreSQL interactive terminal back to the standard Linux shell.

---

## Step-by-Step Walkthrough

### Step 1 — Install PostgreSQL
Refreshed the package lists and installed PostgreSQL along with additional contrib utilities:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
```

### Step 2 — Start and Verify the Service
Started and checked the PostgreSQL service state:

```bash
sudo systemctl start postgresql
sudo systemctl status postgresql
```

Verified that the status indicates **`active (running)`**.

### Step 3 — Enter the PostgreSQL CLI
Accessed the interactive prompt using the administrative `postgres` user:

```bash
sudo -i -u postgres psql
```

The shell changed to `postgres=#`.

### Step 4 — Create Database
Created the college database:

```sql
CREATE DATABASE college_db;
```

Connected to the database:

```sql
\c college_db
```

The prompt changed to `college_db=#`.

### Step 5 — Create `students` Table
Executed the DDL statement to construct the table schema:

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    course VARCHAR(50),
    enrollment_date DATE DEFAULT CURRENT_DATE
);
```

Verified the table creation using `\dt` and `\d students`.

### Step 6 — Insert Data and Query Table
Inserted sample student records into the table:

```sql
INSERT INTO students (first_name, last_name, email, course) VALUES
('John', 'Doe', 'john.doe@college.edu', 'Computer Science'),
('Jane', 'Smith', 'jane.smith@college.edu', 'Information Technology'),
('Alex', 'Johnson', 'alex.j@college.edu', 'Data Science'),
('Emily', 'Davis', 'emily.davis@college.edu', 'Cybersecurity');
```

Queried the inserted records:

```sql
SELECT * FROM students;
```

### Step 7 — Exit the PostgreSQL Shell
Quit the PostgreSQL session:

```sql
\q
```

---

## Screenshots

### 1. Package Installation and Setup
The screenshots below show updating the package list and installing PostgreSQL with contrib utilities.

![PostgreSQL Installation](screenshots/Screenshot%202026-08-20%20214843.png)

![Installation Confirmation](screenshots/Screenshot%202026-08-20%20214856.png)

### 2. PostgreSQL Service Status
The screenshots below show starting the PostgreSQL service and verifying that it is active and running.

![Service Initialization](screenshots/Screenshot%202026-08-20%20215031.png)

![Service Active Running Status](screenshots/Screenshot%202026-08-20%20215123.png)

### 3. Database Creation and Connection
The screenshot below shows entering the `psql` interactive prompt, creating the `college_db` database, and switching to it.

![Create and Connect Database](screenshots/Screenshot%202026-08-20%20215618.png)

### 4. Creating the Students Table
The screenshot below shows executing the `CREATE TABLE students` statement with column constraints.

![Create Students Table](screenshots/Screenshot%202026-08-20%20220055.png)

### 5. Inspecting Table Schema
The screenshot below shows verifying the table with `\dt` and describing the column schema with `\d students`.

![Inspect Table Schema](screenshots/Screenshot%202026-08-20%20220159.png)

### 6. Inserting and Querying Student Records
The screenshot below shows inserting sample student rows and querying all records using `SELECT * FROM students;`.

![Query Student Records](screenshots/Screenshot%202026-08-20%20220424.png)

---

## Common Errors & Fixes

### Error 1: `psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory`

**Cause:** The PostgreSQL service daemon is not running.  
**Fix:** Start the service using systemctl:
```bash
sudo systemctl start postgresql
```

### Error 2: `Peer authentication failed for user "postgres"`

**Cause:** Attempting to connect to PostgreSQL as a normal Linux user without switching to the `postgres` system account or using `sudo`.  
**Fix:** Connect using `sudo` with the `postgres` user:
```bash
sudo -i -u postgres psql
# or
sudo -u postgres psql
```

### Error 3: `ERROR: duplicate key value violates unique constraint "students_email_key"`

**Cause:** Trying to insert a record with an email address that already exists in the table.  
**Fix:** Provide a distinct, unique email address for each student row.

---

## Key Learnings

- **PostgreSQL Architecture:** High-performance, open-source object-relational database management system.
- **Default Superuser (`postgres`):** Default system and database administrator role created upon installation.
- **Interactive Shell (`psql`):** Command-line client for executing SQL queries and administrative meta-commands.
- **Essential Meta-Commands:**
  - `\l` : List all databases.
  - `\c <db>` : Connect to a specific database.
  - `\dt` : List all relations / tables.
  - `\d <table>` : Describe schema of a table.
  - `\q` : Quit the `psql` terminal.
- **Data Integrity & Constraints:** Utilization of `SERIAL`, `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, and `DEFAULT` column constraints.

---

## Result

The PostgreSQL database server was successfully installed and configured on Ubuntu Linux. The `college_db` database was created, the `students` table was defined with relational constraints, sample records were inserted, and data was retrieved using SQL queries.
