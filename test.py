from unittest import TestCase
from unittest import main
from kata import sqInRect, return_smaller, calcul_area, calcul_wdth


class TestKatta(TestCase):

    def test_return_null_if_lng_equals_wdth(self):
        square = []
        self.assertEqual(sqInRect(square, 5, 5), [])

    def test_return_values_depends_lng_and_wdth(self):
        square = []

        sqInRect(square, 5, 3)
        self.assertEqual(square, [3, 2, 1, 1])

    def test_return_same_values_lng_and_wdth_exchanges(self):
        square = []

        sqInRect(square, 3, 5)
        self.assertEqual(square, [3, 2, 1, 1])

    def test_with_other_values(self):
        square = []

        sqInRect(square, 6, 4)
        self.assertEqual(square, [4, 2, 2])

    def test_return_smaller_when_lng_longueur_than_wdth(self):
        self.assertEquals(return_smaller(4, 2), 2)

    def test_return_9_with_lng_3(self):
        self.assertEqual(calcul_area(3), 9)

    def test_calcul_wdth_return_2_with_values_5_3(self):
        self.assertEqual(calcul_wdth(5, 3), 2)


if __name__ == "__main__":
    main()
