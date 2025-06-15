import requests
import bs4

print("Las version de BS4 es " + bs4.__version__)
print("Las version de request es " + requests.__version__)
print("\n#############################################")

url = "https://scrapepark.org/spanish/"
response = requests.get(url)
responseHTML = response.text

print("Este es el html de " + url)
print(responseHTML)
print("\n#############################################")

soup = bs4.BeautifulSoup(responseHTML, "html.parser")

h2Title = soup.find("h2")
print(h2Title)
print("\n#############################################")

# .text devolvera todos los textos del elemento incluso si este tiene subelementos y devuelve siempre un str aunque sea vacio
# .string Solo funciona si el elemento contiene solo una cadena de texto, sin subelementos, en el caso que existan, devolvera None
print("El titulo de la web con .text " + h2Title.text + "Otra manera es .string " + h2Title.string)
print("\n#############################################")

h2Titles = soup.find_all("h2")
print(h2Titles)
print("\n#############################################")

h2TitlesLimit = soup.find_all("h2", limit = 1)
print(h2TitlesLimit)
print("\n#############################################")

for h2 in h2Titles:
    print("\t")
    print(h2)
    print("Estos son los h2 de la web: " + h2.get_text(strip = True))
print("\n#############################################")

divs = soup.find_all("div", class_ = "heading-container heading-center")

for div in divs:
    print("\t")
    print(div) 
    print("Estos son los contemidos de los divs seleccionados " + div.get_text(strip = True))
print("\n#############################################")

srcs = soup.find_all(src = True)

for src in srcs:
    if src["src"].endswith(".jpg"):
        print("\t")
        print(src)
        print(src["alt"])
print("\n#############################################")

for index, src in enumerate(srcs):
    if src["src"].endswith(".png"):
        print("\t")
        print(src["src"])

        responseImagen = requests.get(f"https://scrapepark.org/{src["src"]}")

        with open(f"imagen{index}.png", "wb") as file:
            file.write(responseImagen.content)