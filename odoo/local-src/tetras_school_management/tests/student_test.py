from odoo.tests.common import TransactionCase, tagged


class TestStudentAverage(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestStudentAverage, self).setUp(*args, **kwargs)
        # Création d'un enregistrement de classe pour lier les étudiants
        self.classe = self.env['tetras.classe'].create({'name': 'Mathematics 101'})

        # Création d'un contrôle pour attribuer les notes
        self.control = self.env['tetras.control'].create({
            'name': 'Math Test 1',
            'classe_id': self.classe.id,
        })

        # Création d'un étudiant
        self.student = self.env['tetras.student'].create({
            'name': 'John Doe',
            'classe_id': self.classe.id,
        })

    @tagged('-at_install', 'post_install')
    def test_average_grade(self):
        # Création de notes pour l'étudiant
        grades = [10, 15, 20]
        for grade in grades:
            self.env['tetras.grade'].create({
                'grade': grade,
                'student_id': self.student.id,
                'control_id': self.control.id,
            })

        # Calcul de la moyenne attendue
        expected_average = sum(grades) / len(grades)

        # Force le recalcul de la moyenne
        self.student.invalidate_cache()

        # Vérification que la moyenne calculée est correcte
        self.assertAlmostEqual(self.student.average_grade, expected_average, places=2, msg="La moyenne de l'étudiant n'est pas correcte.")
