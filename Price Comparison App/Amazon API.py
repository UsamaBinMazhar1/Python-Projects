import requests

url = "https://amazon24.p.rapidapi.com/api/todaydeals"

headers = {
	"X-RapidAPI-Key": "356bedef18msh1bf2faddc46d7aap1689cbjsn49d7fa1284ab",
	"X-RapidAPI-Host": "amazon24.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
print(response.text
	  )
print((response.json())['deal_docs'])

for i, data in enumerate((response.json())['deal_docs']):
  print(f'{i}--/{data["deal_title"]}')