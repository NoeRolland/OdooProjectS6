from odoo import fields, models, api


class Grade(models.Model):
    _name = "tetras.grade"
    _description = "Tetras School Management - Grade"

    name = fields.Char(string="Name", compute="_compute_name", store=True)
    grade = fields.Float(string="Grade", required=True)

    student_id = fields.Many2one(
        string="Student",
        comodel_name="tetras.student",
        domain="[('classe_id', '=', classe_id)]"
    )
    classe_id = fields.Many2one(related="control_id.classe_id")

    control_id = fields.Many2one(
        string="Control",
        comodel_name="tetras.control",
    )

    @api.depends('student_id.name', 'control_id.name')
    def _compute_name(self):
        for record in self:
            student_name = record.student_id.name if record.student_id else ''
            control_name = record.control_id.name if record.control_id else ''
            record.name = f"{student_name} - {control_name}" if student_name and control_name else 'No Name'

