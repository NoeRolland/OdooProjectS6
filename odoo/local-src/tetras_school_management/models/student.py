from odoo import fields, models


class Student(models.Model):
    _name = "tetras.student"
    _inherit = "tetras.contact"
    _description = "Tetras School Management - Student"

    grade_ids = fields.One2many(
        string="Grades",
        comodel_name="tetras.grade",
        inverse_name="student_id",
    )

    classe_id = fields.Many2one(
        string="Classe",
        comodel_name="tetras.classe",
    )
