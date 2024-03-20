from odoo import fields, models


class Teacher(models.Model):
    _name = "tetras.teacher"
    _inherit = "tetras.contact"
    _description = "Tetras School Management - Teacher"

    diploma = fields.Char(string="Diploma")

    control_ids = fields.One2many(
        string="Control",
        comodel_name="tetras.control",
        inverse_name="teacher_id",
    )

