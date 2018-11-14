from tests.fixture import TestFixture
from flasky.sale.sale_model import Sale


class TestSaleModel(TestFixture):
    """
    Test sale object initialisation
    """

    def test_sale_init(self):
        self.assertEqual(self.sale.attendant, 'kibuuka')
        self.assertIsInstance(self.sale, Sale)

    def test_convert_sale_to_json(self):
        dict_sale = self.sale.to_json()
        self.assertIsInstance(dict_sale, dict)
