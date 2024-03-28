from odoo import fields, models, api


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

    average_grade = fields.Float(string="Average Grade", compute="_compute_average_grade")

    @api.depends('grade_ids')
    def _compute_average_grade(self):
        for student in self:
            grades = student.grade_ids.mapped('grade')
            if grades:
                student.average_grade = sum(grades) / len(grades)
            else:
                student.average_grade = 0.0
