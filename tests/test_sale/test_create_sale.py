import json

from tests.fixture import TestFixture


class TestCreateSale(TestFixture):
    """

    """
    def test_create_a_sale(self):
        # Test successful POST request to create a sale
        with self.client:
            # first create a product to append to a sale
            _ = self.create_product()
            # add product to cart
            _ = self.add_product_to_shopping_cart()
            # then create a sale with the appended product
            response = self.create_sale()
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data['attendant'], 'michael')
            self.assertEqual(data['total_amount'], 1499.0)

    def test_create_sale_with_wrong_content_type(self):
        """
        Test unsuccessful POST request to
        create a sale with wrong content type
        """
        with self.client:
            response = self.client.post(
                '/api/v1/sales',
                content_type="xml",
                data=json.dumps(dict(attendant='ivan')))
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data['message'], 'request must be of type json')

    def test_create_sale_without_attendant_attribute(self):
        """
        Test unsuccessful POST request to
        create a sale with missing required attribute
        """
        with self.client:
            response = self.create_sale_without_the_attendant_attribute()

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(
                data['message'],
                'please provide a valid attendant name')

    def test_cant_create_sale_with_an_empty_string(self):
        """
        Test unsuccessful POST request to
        create a sale with an empty string
        """
        with self.client:
            response = self.client.post(
                '/api/v1/sales',
                content_type="application/json",
                data=json.dumps(dict(attendant='  ')))
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(
                data['message'], 'please provide a valid attendant name')
