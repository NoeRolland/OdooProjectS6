from odoo import fields, models


class Control(models.Model):
    _name = "tetras.control"
    _description = "Tetras School Management - control"

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")

    teacher_id = fields.Many2one(
        string="Teacher",
        comodel_name="tetras.teacher",
    )

    classe_id = fields.Many2one(
        string="Class",
        comodel_name="tetras.classe",
    )

    grade_ids = fields.One2many(
        string="Grades",
        comodel_name="tetras.grade",
        inverse_name="control_id",
    )




