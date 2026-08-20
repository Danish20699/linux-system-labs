# DDL, DML, and DQL Commands in Linux PostgreSQL

## Objective

To understand and practice the three foundational categories of SQL statements—**DDL** (Data Definition Language), **DML** (Data Manipulation Language), and **DQL** (Data Query Language)—using the PostgreSQL interactive shell (`psql`) on Ubuntu Linux.

## Prerequisites

- Ubuntu / Debian Linux system
- PostgreSQL installed and service running (`postgresql`)
- Access to the `psql` command-line utility via `sudo`
- Basic terminal and SQL knowledge

---

## SQL Command Categories Overview

| Category | Full Name | Purpose | Core Commands |
| :--- | :--- | :--- | :--- |
| **DDL** | Data Definition Language | Defines, modifies, and deletes database schema and structure | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Manages and manipulates data records inside existing tables | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | Retrieves, filters, and analyzes data stored in tables | `SELECT` (with `WHERE`, `ORDER BY`, `GROUP BY`, `LIMIT`) |

---

## Commands Used

### 1. Database Connection & Setup

```bash
sudo -i -u postgres psql
```

Opens the PostgreSQL interactive shell.

```sql
CREATE DATABASE company_db;
\c company_db
```

Creates and switches to a dedicated database named `company_db`.

---

### 2. DDL (Data Definition Language) Commands

#### A. `CREATE TABLE` (Define Schema)
```sql
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE
);
```
Creates the initial table schema with primary key and default constraints.

#### B. `ALTER TABLE` (Modify Schema)
```sql
ALTER TABLE employees ADD COLUMN department VARCHAR(50);
```
Adds a new column `department` to the existing table.

```sql
ALTER TABLE employees RENAME COLUMN role TO job_title;
```
Renames an existing column within the table.

#### C. `CREATE` & `DROP TABLE` (Delete Table)
```sql
CREATE TABLE temp_data (id INT, note TEXT);
DROP TABLE temp_data;
```
Creates a temporary table and completely deletes its structure and contents.

---

### 3. DML (Data Manipulation Language) Commands

#### A. `INSERT` (Add Records)
```sql
INSERT INTO employees (name, job_title, salary, department) VALUES
('Alice Walker', 'Software Engineer', 75000.00, 'Engineering'),
('Bob Martin', 'DevOps Engineer', 82000.00, 'Operations'),
('Charlie Brown', 'Data Analyst', 68000.00, 'Analytics'),
('Diana Prince', 'Engineering Manager', 95000.00, 'Engineering'),
('Evan Wright', 'Intern', 35000.00, 'Engineering');
```
Inserts multiple new data rows into the `employees` table.

#### B. `UPDATE` (Modify Existing Records)
```sql
UPDATE employees 
SET salary = 40000.00 
WHERE name = 'Evan Wright';
```
Updates the salary value for a specific employee matching the condition.

#### C. `DELETE` (Remove Specific Records)
```sql
DELETE FROM employees 
WHERE name = 'Evan Wright';
```
Deletes specific rows that match the given criteria.

---

### 4. DQL (Data Query Language) Commands

#### A. Basic `SELECT`
```sql
SELECT * FROM employees;
```
Retrieves all columns and rows from the table.

#### B. Filtered `SELECT` with `WHERE` Clause
```sql
SELECT name, job_title, salary 
FROM employees 
WHERE salary > 70000;
```
Retrieves specific columns where employee salary exceeds 70,000.

#### C. Sorted `SELECT` with `ORDER BY`
```sql
SELECT name, salary, department 
FROM employees 
ORDER BY salary DESC;
```
Sorts employee records in descending order by salary.

#### D. Aggregation and Grouping with `GROUP BY`
```sql
SELECT department, COUNT(*) AS total_employees, AVG(salary) AS avg_salary
FROM employees 
GROUP BY department;
```
Groups employees by department, calculating the employee count and average salary per department.

#### E. Limit Results with `LIMIT`
```sql
SELECT name, salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 2;
```
Fetches the top 2 highest-paid employees.

---

## Step-by-Step Walkthrough

### Step 1 — Connect to PostgreSQL and Create Database
1. Opened the PostgreSQL shell:
   ```bash
   sudo -i -u postgres psql
   ```
2. Created a new database and connected:
   ```sql
   CREATE DATABASE company_db;
   \c company_db
   ```

### Step 2 — Practice DDL Commands
1. Created the `employees` table using `CREATE TABLE`.
2. Modified the structure using `ALTER TABLE` to add the `department` column and rename `role` to `job_title`.
3. Tested `DROP TABLE` on a temporary test table.
4. Inspected the resulting schema using `\d employees`.

### Step 3 — Practice DML Commands
1. Inserted 5 employee records using `INSERT INTO`.
2. Updated a salary using `UPDATE employees SET ... WHERE ...`.
3. Deleted a row using `DELETE FROM employees WHERE ...`.

### Step 4 — Practice DQL Commands
1. Executed `SELECT * FROM employees;` to inspect active records.
2. Filtered records using `WHERE salary > 70000;`.
3. Ordered records using `ORDER BY salary DESC;`.
4. Grouped records by department using `GROUP BY department;`.
5. Retrieved the highest earners using `LIMIT 2;`.

### Step 5 — Exit PostgreSQL
```sql
\q
```

---

## Screenshots

### 1. DDL — Altering Table Columns
The screenshot below shows executing `ALTER TABLE` commands to add columns.

![DDL Alter Table Add Column](screenshots/Screenshot%202026-08-20%20223241.png)

### 2. DDL — Adding the Department Column
The screenshot below shows adding the `department VARCHAR(50)` column to the `employees` table.

![DDL Add Department Column](screenshots/Screenshot%202026-08-20%20223433.png)

### 3. DDL — Renaming Column & Table Schema Inspection
The screenshots below show renaming `role` to `job_title` and inspecting the updated schema with `\d employees`.

![DDL Rename Column and Schema](screenshots/Screenshot%202026-08-20%20223459.png)

![DDL Terminal Overview](screenshots/Screenshot%20(211).png)

### 4. DML — Fixing Column & Inserting Records
The screenshot below shows dropping duplicate column with `ALTER TABLE ... DROP COLUMN` and successfully inserting 5 employee records with `INSERT INTO`.

![DML Insert Records](screenshots/Screenshot%202026-08-20%20224113.png)

### 5. DML — Updating and Deleting Records
The screenshot below shows executing `UPDATE` to modify salary and `DELETE` to remove a record with conditional `WHERE` clauses.

![DML Update and Delete](screenshots/Screenshot%202026-08-20%20224215.png)

### 6. DQL — Querying, Filtering, Sorting, and Grouping Data
The screenshot below shows executing `SELECT` queries with `WHERE`, `ORDER BY`, `GROUP BY`, and `LIMIT`.

![DQL Select Queries](screenshots/Screenshot%202026-08-20%20224309.png)

---

## Common Errors & Fixes

### Error 1: `ERROR: column "department" does not exist`

**Cause:** Trying to insert data into a column that has not yet been added to the table.  
**Fix:** Run the DDL `ALTER TABLE` command to add the missing column first:
```sql
ALTER TABLE employees ADD COLUMN department VARCHAR(50);
```

### Error 2: `UPDATE/DELETE Without WHERE Clause`

**Cause:** Executing `UPDATE employees SET salary = 50000;` or `DELETE FROM employees;` without a `WHERE` clause modifies or deletes **ALL** records in the table.  
**Fix:** Always specify a precise condition using `WHERE`:
```sql
UPDATE employees SET salary = 50000 WHERE emp_id = 1;
```

### Error 3: Semicolon `;` Missing in SQL Statement

**Cause:** PostgreSQL prompts with `company_db-#` waiting for a query terminator.  
**Fix:** Type `;` and press `Enter` to execute, or press `Ctrl + C` to cancel.

---

## Key Learnings

- **DDL:** Defines database schema (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`). Affects table structure, not row data.
- **DML:** Modifies data stored within tables (`INSERT`, `UPDATE`, `DELETE`). Directly modifies records.
- **DQL:** Queries and extracts data (`SELECT`). Read-only operation that does not modify underlying data.
- **Data Filtering & Sorting:** Using `WHERE` for conditions and `ORDER BY ASC/DESC` for ordered output.
- **Data Aggregation:** Using `COUNT()`, `AVG()`, `SUM()`, `MIN()`, `MAX()` alongside `GROUP BY` to summarize dataset metrics.

---

## Result

DDL, DML, and DQL SQL operations were successfully executed inside PostgreSQL on Ubuntu Linux. A new relational schema was constructed, altered, populated with dataset records, updated, and queried using analytical SQL clauses.
