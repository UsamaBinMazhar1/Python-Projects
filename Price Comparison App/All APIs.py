import requests

url = "https://real-time-product-search.p.rapidapi.com/product-offers"

querystring = {"product_id":"11577822456427762145","country":"us","language":"en"}

headers = {
	"X-RapidAPI-Key": "356bedef18msh1bf2faddc46d7aap1689cbjsn49d7fa1284ab",
	"X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# import requests
#
# url = "https://real-time-product-search.p.rapidapi.com/search"
#
# querystring = {"q":"Mouse","country":"us","language":"en"}
#
# headers = {
# 	"X-RapidAPI-Key": "356bedef18msh1bf2faddc46d7aap1689cbjsn49d7fa1284ab",
# 	"X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

import requests

url = "https://real-time-product-search.p.rapidapi.com/search"

querystring = {"q":"Grayton Outdoor Aluminum Sofa","country":"us","language":"en","sort_by":"LOWEST_PRICE"}

headers = {
	"X-RapidAPI-Key": "356bedef18msh1bf2faddc46d7aap1689cbjsn49d7fa1284ab",
	"X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)