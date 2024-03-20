from odoo import fields, models


class Classe(models.Model):
    _name = "tetras.classe"
    _description = "Tetras School Management - classe"

    name = fields.Char(string="Name")

    student_ids = fields.One2many(
        string="Students",
        comodel_name="tetras.student",
        inverse_name="classe_id",
    )

    control_ids = fields.One2many(
        string="Control",
        comodel_name="tetras.control",
        inverse_name="classe_id",
    )



