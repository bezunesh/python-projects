from __future__ import annotations
from urllib import request
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, quote
import certifi, ssl, json
from .products import Product

class EcommerceApi:
    def __init__(self):
        self.api_url = "https://fakestoreapi.com"
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.context = ssl.create_default_context(cafile=certifi.where())
    
    def sendRequest(self, path, limit=None, sort=None):
        d, queryString = {}, None
        if limit: d['limit'] = limit
        if sort: d['sort'] = sort
        if d: queryString = urlencode(d)
        url = f"{self.api_url}{path}?{queryString}" if queryString else f"{self.api_url}{path}"
        try:
            requestObj = request.Request(url, headers=self.headers)
            with request.urlopen(requestObj, context=self.context) as response:
                # convert response to a python list object
                parsed_python_obj = json.load(response)
                # convert python list object to  a json formatted str
                #serialized_python_obj = json.dumps(parsed_python_obj, indent=2)  
                return parsed_python_obj    
        except HTTPError as e:
            print(e)
        except URLError as e:
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
        url = f"{self.api_url}{path}"
        data = json.dumps(product.__dict__)
        req_obj = request.Request(url, data=data.encode(), method="POST", headers=self.headers)
        try:
            with request.urlopen(req_obj, context=self.context) as response:
                content_type = response.getheader('Content-Type')
                print(content_type)
                if content_type.startswith("application/json"):
                    # parse it to a python obj
                    parsed_data = json.load(response)
                    return parsed_data
        except (HTTPError, URLError) as e:
            print(e)


def addNewProduct():
    api = EcommerceApi()
    product = Product('Addidas sneaker', 14.5, 'New release sneaker', 
        'https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg', 'men\'s clothing')
    new_product = api.addNewProduct(product)
    print(new_product)

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
    addNewProduct()

