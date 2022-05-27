from __future__ import annotations
from urllib import request
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, quote
import certifi, ssl, json
from products import Product

class EcommerceApi:
    def __init__(self):
        self.api_url = "https://fakestoreapi.com"
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.context = ssl.create_default_context(cafile=certifi.where())
    
    def sendRequest(self, path: str, data: str =None, method: str ='GET',
        limit: int =None, sort: str =None) ->Any[list,dict]:

        d, queryString = {}, None
        if limit: d['limit'] = limit
        if sort: d['sort'] = sort
        if d: queryString = urlencode(d)
        
        url = f"{self.api_url}{path}?{queryString}" if queryString else f"{self.api_url}{path}"
        data = data.encode() if isinstance(data, str) else  None

        try:
            requestObj = request.Request(url, data=data, method=method, headers=self.headers)
            with request.urlopen(requestObj, context=self.context) as response:
                # convert response to a python object
                parsed_python_obj = json.load(response) 
                return parsed_python_obj    
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
        except json.JSONDecodeError as e:
            print(e)
    
    def getProducts(self, limit=10, sort='asc') -> str:
        path = "/products"
        return self.sendRequest(path, limit=limit, sort=sort)
    
    def getProduct(self, id) ->str:
        path = f"/products/{id}"
        url = f"{self.api_url}{path}"
        return self.sendRequest(path)
    
    def getCategories(self, limit=None, sort=None) -> list[str]:
        """
        Returns a list of product categories
        """
        path = "/products/categories"
        return self.sendRequest(path, limit, sort)

    def getProductsInCategory(self, category: str, limit: int = None, sort: str = None) -> str:
        path = quote(f"/products/category/{category}")
        return self.sendRequest(path, limit, sort)
    
    def addNewProduct(self, product: Product):
        path = "/products"
        data = json.dumps(product.__dict__)
        return self.sendRequest(path, data=data, method='POST')

    def updateProduct(self, product: dict) -> dict: 
        id = product['id']
        path = f"/products/{id}"
        return self.sendRequest(path, data=json.dumps(product), method='PUT')
    
    def patchProduct(self, product: dict, id: int) -> dict:
        path = f"/products/{id}"
        return self.sendRequest(path, data=json.dumps(product), method='PATCH')
    
    def deleteProduct(self, id) -> dict:
        path = f"/products/{id}"
        return self.sendRequest(path, method="DELETE")


def addProduct():
    api = EcommerceApi()
    product = Product('Addidas sneaker', 14.5, 'New release sneaker', 
        'https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg', 'men\'s clothing')
    new_product = api.addNewProduct(product)
    print(new_product)

def updateProduct():
    api = EcommerceApi()
    product = {
        'id': 2,
        'title': 'New Title',
        'price': 10.00,
        'description': 'New Description',
        'image': 'https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg',
        'category': 'men\'s clothing'
    }
    updated_product = api.updateProduct(product)
    print(updated_product)

def partialUpdateProduct(id):
    api = EcommerceApi()
    product = {
        'price': 10.00,
        'description': 'New Description'
    }
    print(api.patchProduct(product, id))

def deleteProduct(id):
    api = EcommerceApi()
    print(api.deleteProduct(id))

def getAllCategories():
    api = EcommerceApi()
    categories = api.getCategories()
    # get two products from each category
    for category in categories:
        products = api.getProductsInCategory(category, limit=2)
        print(category)
        print("********")
        print(products)
    

if __name__ == '__main__':
    # add new product
    addProduct()
    #updateProduct()
    #partialUpdateProduct(5)
    #deleteProduct(7)