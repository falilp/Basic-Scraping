import requests, bs4, re

url = "https://scrapepark.org/spanish/"
response = requests.get(url)
print("Estado de la request " + str(response.status_code) + (" Status: " + "Success" if response.status_code < 400 else "Failed"))

soup = bs4.BeautifulSoup(response.text, "html.parser")

telephons = soup.find_all(string = re.compile(r"\d+-\d+-\d+"))

print("Estos son todos los telefonos " + str(telephons))

copyright = soup.find_all(string = re.compile("©"))
print(copyright)
print(copyright[0])
print(copyright[0].parent)

menu = soup.find(string = re.compile("MENÚ"))
print(menu)
print(menu.parent.find_next_siblings())

strings = ["MENÚ", "©", "carpincho", "Patineta"]

for string in strings:
    try:
        responseString = soup.find(string = re.compile(string))
        print(responseString.text)
    except AttributeError:
        print(f"El string que no se encontro fue {string}")