import unittest
from Glive import Cell, Glive




class TestCellMethod(unittest.TestCase):

    def test_cell_alone_dead(self):
        cell = Cell()
        cell.status(0)
        self.assertEqual(cell.phase, False)
    
    def test_cell_alone_alive(self):
        cell = Cell(True)
        cell.status(0)
        self.assertEqual(cell.phase, False)

    def test_cell_group2_dead(self):
        cell = Cell()
        cell.status(2)
        self.assertEqual(cell.phase, False)

    def test_cell_group2_alive(self):
        cell = Cell(True)
        cell.status(2)
        self.assertEqual(cell.phase, True)

    def test_cell_group3_dead(self):
        cell = Cell()
        cell.status(3)
        self.assertEqual(cell.phase, True)

    def test_cell_group3_alive(self):
        cell = Cell(True)
        cell.status(3)
        self.assertEqual(cell.phase, True)

    def test_cell_group4_dead(self):
        cell = Cell()
        cell.status(4)
        self.assertEqual(cell.phase, False)

    def test_cell_group4_alive(self):
        cell = Cell(True)
        cell.status(4)
        self.assertEqual(cell.phase, False)


class TestBoardMethod(unittest.TestCase):
    

    def test_neighboar_nocell(self):
        miboard = Glive()
        patron = [[True, True, True], [True, False, True], [True, True, True]]
        miboard.probe_state(patron)
        miboard.show(1)
        self.assertEqual(miboard.neighbor(1, 1), 8)
    
    def test_neighboar_cell(self):
        miboard = Glive()
        patron = [[True, True, True], [True, True, True], [True, True, True]]
        miboard.probe_state(patron)
        miboard.show(1)
        self.assertEqual(miboard.neighbor(1, 1), 8)

    def test_neighboar_corner_Top_left_cell(self):
        miboard = Glive()
        patron = [[True, True, True], [True, True, True], [True, True, True]]
        miboard.probe_state(patron)
        miboard.show(1)
        self.assertEqual(miboard.neighbor(0, 0), 3)

    def test_neighboar_corner_Top_left_nocell(self):
        miboard = Glive()
        patron = [[False, True, True], [True, True, True], [True, True, True]]
        miboard.probe_state(patron)
        miboard.show(1)
        self.assertEqual(miboard.neighbor(0, 0), 3)


if __name__ == '__main__':
    unittest.main()
