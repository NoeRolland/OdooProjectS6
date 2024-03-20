from odoo import fields, models


class Contact(models.Model):
    _name = "tetras.contact"
    _description = "Tetras School Management - Contact"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    birth_day = fields.Date(string="Birth day")


