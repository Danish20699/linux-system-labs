
# Linux User Management Commands

## Objective

To learn and practice basic Linux user management commands, including creating, verifying, locking, unlocking, and deleting user accounts.

## Prerequisites

- Ubuntu/Linux operating system
- Terminal access
- Sudo privileges
- Basic knowledge of Linux commands

## Commands Used

### 1. Check Current User

```bash
whoami
Displays the username of the currently logged-in user.
id
Displays the current user's UID, GID, and group memberships.
2. Create a New User
sudo adduser labuser
Creates a new Linux user named labuser.
The command also creates the user's home directory and prompts for a password and optional user information.
3. Verify User Information
id labuser
Displays the UID, GID, and groups associated with the labuser account.
groups labuser
Displays the groups that the labuser belongs to.
4. View User Account Information
getent passwd labuser
Retrieves the account entry for labuser from the system's user database.
5. Lock a User Account
sudo passwd -l labuser
Locks the password of the labuser account and prevents password-based authentication.
sudo passwd -S labuser
Displays the current password status of the user.
6. Unlock a User Account
sudo passwd -u labuser
Unlocks the password of the labuser account.
sudo passwd -S labuser
Verifies the password status after unlocking the account.
7. Delete a User
sudo deluser labuser
Removes the labuser account from the system.
To verify that the user has been removed:
id labuser
The command should report that the user does not exist.
Step-by-Step Walkthrough
1. Checked the currently logged-in Linux user using whoami.
2. Used id to view the current user's UID, GID, and group memberships.
3. Created a test user named labuser using adduser.
4. Verified the new user's UID, GID, and group memberships.
5. Used getent passwd to view the user's account entry.
6. Locked the labuser account using passwd -l.
7. Checked the account status using passwd -S.
8. Unlocked the account using passwd -u.
9. Verified the account status again.
10. Deleted the test user using deluser.
11. Confirmed that the user account was successfully removed.
