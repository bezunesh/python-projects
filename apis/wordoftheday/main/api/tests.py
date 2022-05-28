import unittest, io
from unittest import TestCase
from unittest.mock import patch
from urllib.parse import quote
from urllib import request
from urllib.error import HTTPError, URLError
from http.client import HTTPResponse
import certifi, ssl, json
from fakestoreapi import EcommerceApi
from products import Product

class ApiTestCase(TestCase):
    def setUp(self):
        self.api = EcommerceApi()

    def createProduct(self):
        title = 'New Title'
        price = 10.00
        description = 'New Description'
        image = 'https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg'
        category = 'men\'s clothing'

        return Product(title, price, description, image, category)

    def test_initializaton(self):
        api = self.api
        self.assertEqual(api.api_url, "https://fakestoreapi.com")
        self.assertIsNotNone(api.headers['User-Agent'])
        self.assertIsInstance(api.context,  ssl.SSLContext)
    
    @patch.object(EcommerceApi, 'sendRequest')
    def test_getProductsCallsSendRequest(self, mock_sendRequest):
        """
        test EcommerceApi.sendRequest is called with appropriate arguments
        """
        path = "/products"
        limit = 5
        sort = 'desc'
        self.api.getProducts(limit=limit, sort=sort)
        mock_sendRequest.assert_called_with(path, limit=limit, sort=sort)

    @patch.object(EcommerceApi, 'sendRequest')
    def test_getProductCallsSendRequest(self, mock_sendRequest):
        """ 
        test EcommerceApi.sendRequest is called with appropriate arguments
        """
        self.api.getProduct(id=7)
        mock_sendRequest.assert_called_with("/products/7")

    @patch.object(EcommerceApi, 'sendRequest')
    def test_getCategoriesMakesRequest(self, mock_sendRequest):
        self.api.getCategories()
        mock_sendRequest.assert_called_with("/products/categories", None, None)
    
    @patch.object(EcommerceApi, 'sendRequest')
    def test_getProductsInCategory(self, mock_sendRequest):
        category = 'Men\'s clothing'
        path = quote(f"/products/category/{category}")
        self.api.getProductsInCategory(category)
        mock_sendRequest.assert_called_with(path, None, None)
   
    @patch.object(EcommerceApi, 'sendRequest')
    def test_addNewProduct(self, mock_sendRequest):
        product = self.createProduct()
        self.api.addNewProduct(product)

        data = json.dumps(product.__dict__)
        mock_sendRequest.assert_called_with('/products', data=data, method='POST')

    @patch.object(EcommerceApi, 'sendRequest')
    def test_updateProduct(self, mock_sendRequest):
        product = self.createProduct()
        product_dict = product.__dict__
        product_dict['id'] = 8
        self.api.updateProduct(product_dict)
        mock_sendRequest.assert_called_with('/products/8', 
            data=json.dumps(product_dict), method='PUT')
   
    @patch.object(EcommerceApi, 'sendRequest')
    def test_patchProduct(self, mock_sendRequest):
        product = self.createProduct()
        product_dict = product.__dict__
        self.api.patchProduct(product_dict, id=6)
        mock_sendRequest.assert_called_with('/products/6', 
            data=json.dumps(product_dict), method='PATCH')
    
    @patch.object(EcommerceApi, 'sendRequest')
    def test_deleteProduct(self, mock_sendRequest):
        id = 9
        self.api.deleteProduct(id)
        mock_sendRequest.assert_called_with('/products/9', method='DELETE')

    def test_sendRequest(self):
        url = "https://fakestoreapi.com/categories"
        # getCatagories
        # a .read() supporting text/binary file, returning bytes of JSON document 
        fp = io.BytesIO(b'["clothing", "jewelery", "perfumes"]')
        with patch('urllib.request.urlopen', return_value = fp) as mock_urlopen:
            result = self.api.sendRequest("/categories") 
            #mock_urlopen.assert_called_with(requestObj, context=self.api.context)
            self.assertIsInstance(result, list)
            self.assertEqual(result, ["clothing", "jewelery", "perfumes"])

    def test_sendRequestRaisesExceptions(self):
        # non existing path
        path = "/category"
        self.assertRaises(HTTPError, self.api.sendRequest, path)
        # wrong url
        self.api.api_url = "http://fakestoreapi.co"
        self.assertRaises(URLError, self.api.sendRequest, '/categories')
       
if __name__ == '__main__':
    unittest.main()