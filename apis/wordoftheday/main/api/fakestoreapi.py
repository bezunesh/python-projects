from urllib import request
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
import certifi
import ssl
import json

api_url = "https://fakestoreapi.com"
path = "/products"
limit = 2
queryString = urlencode({'limit': limit})
url = f"{api_url}{path}?{queryString}"
context = ssl.create_default_context(cafile=certifi.where())

try:
    requestObj = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with request.urlopen(requestObj, context=context) as response:
        # convert response to a python list object
        parsed_python_obj = json.load(response)
        # convert python list object to  a json formatted str, 
        # pretty print too
        serialized_python_obj = json.dumps(parsed_python_obj, indent=2)
        print(parsed_python_obj)
        print(type(parsed_python_obj))
        print(serialized_python_obj)
        print(type(serialized_python_obj))
      
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)