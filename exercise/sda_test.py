import unittest

class Car():
    def __init__(self, culoare, marca):
        self.culoare = culoare
        self.marca = marca

Masina= Car('magenta', 'NewBeetle')
Z=25
Masina2 = Car('rosu de gentiana', 'Audi')


class TestExample(unittest.TestCase):
    def test_include(self):
        self.assertNotIn("B", "SDAAcademy")

    def test_instanta(self):
        self.assertNotIsInstance(Z, Car)


    def test_egalitate(self):
        result = 5 + 5
        self.assertEqual(result, 10)

    def test_adevarat(self):
        x = False
        self.assertFalse(x, "daca nu e egat te anuntam noi")




# entry point
# aparent in PyCharm merge fara ?!
if __name__ == "__main__":
    unittest.main()