from datetime import datetime, timedelta
from odoo import models, fields, api

# Model class definition
class TaskManager(models.Model):
    _name = 'task.manager'
    _description = 'Task'

    name         = fields.Char(string='Title', required=True)
    description  = fields.Text(string='Description')
    assigned_to  = fields.Many2one('res.users', string='Assigned To')
    due_date     = fields.Datetime(string='Due Date')
    priority     = fields.Selection([
                       ('low', 'Low'),
                       ('medium', 'Medium'),
                       ('high', 'High'),
                   ], default='medium', string='Priority')
    status       = fields.Selection([
                       ('new', 'New'),
                       ('in_progress', 'In Progress'),
                       ('done', 'Done'),
                   ], default='new', string='Status')
    days_left    = fields.Integer(string='Days Left', compute='_compute_days_left', store=True)

    @api.depends('due_date')
# Method definition
    def _compute_days_left(self):
        for rec in self:
            if rec.due_date:
                delta = rec.due_date - datetime.now()
                rec.days_left = max(delta.days, 0)
            else:
                rec.days_left = 0

# Method definition
    def cron_notify_expiring_tasks(self):
        template = self.env.ref('task_manager.task_expire_email_template')
        now = datetime.now()
        cutoff = now + timedelta(days=3)
        tasks = self.search([
            ('due_date', '<=', cutoff),
            ('due_date', '>=', now),
            ('status', '!=', 'done'),
        ])
        for task in tasks:
            template.send_mail(task.id, force_send=True)
