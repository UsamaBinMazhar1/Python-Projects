# from ebaysdk.finding import Connection as Shopping
#
# api = Shopping(appid = 'lalakoja-PriceCom-SBX-cd28d4866-4d31130f', siteid = 'EBAY-GB', config_file=None)
#
# response = api.execute("dealItems", {"categoryId" : "257818"})
# print(response.text)


import requests

url = "https://ebay-data-scraper.p.rapidapi.com/status/server"

querystring = {"country":"australia"}

headers = {
	"X-RapidAPI-Key": "356bedef18msh1bf2faddc46d7aap1689cbjsn49d7fa1284ab",
	"X-RapidAPI-Host": "ebay-data-scraper.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)