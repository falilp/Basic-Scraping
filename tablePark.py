import requests, bs4

url = "https://scrapepark.org/spanish/"
response = requests.get(url)
print("Estado de la request " + str(response.status_code) + " Status: " + "Success" if response.status_code < 400 else "Failed")

soup = bs4.BeautifulSoup(response.text, "html.parser")

table = soup.find_all("iframe")[0]["src"]
print(table)

requestTable = requests.get(url + table)
print("Estado de la request de la tabla" + str(requestTable.status_code) + " Status: " + "Success" if requestTable.status_code < 400 else "Failed")

soupTable = bs4.BeautifulSoup(requestTable.text, "html.parser")

finalTable = soupTable.find("table")
print(finalTable)

product = soupTable.find_all(["th", "td"], attrs = {"style":"color: red;"})
print(product)

for pr in product:
    print(pr.text)