import requests, bs4

url = "https://scrapepark.org/spanish/contact"

for index in range(1, 3):
    resposne = requests.get(f"{url}{index}")
    print("El resultado de la request ha sido " + str(resposne.status_code) + (" Success" if resposne.status_code < 400 else " Failed"))

    soup = bs4.BeautifulSoup(resposne.text, "html.parser")
    print(soup.h5.get_text(strip = True))