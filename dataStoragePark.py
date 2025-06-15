import requests, bs4, csv, os

os.makedirs("resources", exist_ok = True)

productsList = []
priceList = []
imageList = []

productsList.insert(0, "productos")
priceList.insert(0, "precios")
imageList.insert(0, "imagenes")

url = "https://scrapepark.org/spanish/"
response = requests.get(url)
print("Estado de la request " + str(response.status_code) + (" Status: " + "Success" if response.status_code < 400 else "Failed"))

soup = bs4.BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_ = "detail-box")

index = 0

for product in products:
    if(product.h6 is not None) and ("Patineta" in product.h5.text):
        index += 1

        productsList.append(product.h5.get_text(strip = True))
        priceList.append(product.h6.get_text(strip = True))
        imageList.append(product.parent.img["src"].removeprefix(".."))

        responseImg = requests.get(f"https://scrapepark.org/{product.parent.img["src"]}")

        with open(f"resources/imagen{index}" + (".png" if product.parent.img["src"][-3:] == "png" else ".jpg"), "wb") as file:
            file.write(responseImg.content)

#data = dict(zip(productsList, priceList))

with open("resources/data.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    #writer.writerows(data.items())

    writer.writerow([productsList[0], priceList[0], imageList[0]])

    for index in range(1, len(productsList)):
        writer.writerow([productsList[index], priceList[index], imageList[index]])