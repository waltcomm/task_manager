from odoo import models, api

class ReportTaskManagerAll(models.AbstractModel):
    _name = 'report.task_manager.report_task_manager_document'
    _description = 'Task Manager Tasks Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if not docids:
            docs = self.env['task.manager'].search([])
        else:
            docs = self.env['task.manager'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'task.manager',
            'docs': docs,
        }