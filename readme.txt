# Odoo Task Manager Module

A simple, extensible Task Management module for Odoo 17, with automated reminders and printable reports.

---

Features

- CRUD Tasks: Create, read, update and delete tasks.
- Fields:
  - Title (required)
  - Description
  - Assigned To (Many2one -> Users)
  - Due Date (Datetime)
  - Status (New -> In Progress -> Completed)
  - Days Left (computed calendar days to due date)
- Automated Reminders:  
  - Cron job runs daily and emails users when a task’s due date is within the next 3 days.
  - Uses a customizable Mail Template.
- Printable QWeb Report:  
  - “Print Report” button on the Task form.
  - Outputs a styled table of selected tasks (title, description, assignee, due date, status, days left).
- Access Control:  
  - New group Task Manager User.
  - Only users in this group (or all internal users, if you adjust access rights) can view/create/edit tasks.
- Clean UI:  
  - Menu entries under Tasks -> My Tasks.
  - Responsive tree and form views.

---

Prerequisites

- Odoo 17 (Community or Enterprise).
- Python dependencies: ships with Odoo core; no extra Python modules.
- Outgoing Mail Server configured (Settings -> Technical -> Email -> Outgoing Mail Servers) for reminders.
- (Optional) Developer Mode enabled for advanced troubleshooting.

---

Installation

1. Download & Extract
   copy the ZIP into your addons folder
   cd <your-odoo-addons-path>
   unzip task_manager.zip
   mv task_manager /path/to/addons/task_manager

---

Usage

1. After installing the module, you need to log into the system, select the Services category, find the Task Manager module there, and click the Activate button.
Once activated, the Tasks menu items will appear.
Select this menu, and the Tasks module interface will open.

The Tasks window displays the full list of tasks.
In the My Tasks window, you can click the New button to create a new task.
To edit a task, click on it, and you’ll be able to press the Print Report button.
