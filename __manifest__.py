{
    "name": "Task Manager",
    "version": "1.0",
    "author": "Nikolajs Valters",
    "category": "Services",
    "summary": "Manage simple tasks",
    "depends": ["base", "mail"],
    "images": ["static/description/icon.png"],
    "data": [
        "security/task_manager_security.xml",
        "security/ir.model.access.csv",
        "data/task_mail_template.xml",
        "data/task_cron.xml",
        "report/task_manager_report.xml",
        "views/task_manager_views.xml"
    ],
    "installable": True,
    "application": True
}
