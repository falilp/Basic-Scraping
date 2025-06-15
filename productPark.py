import requests, bs4

url = "https://scrapepark.org/spanish/"
response = requests.get(url)
print("Estado de la request " + str(response.status_code) + " Status: " + "Success" if response.status_code < 400 else "Failed")

soup = bs4.BeautifulSoup(response.text, "html.parser")

productsBox = soup.find_all("div", class_ = "detail-box")
products = []
prices = []

for product in productsBox:
    if(product.h6 is not None) and ("Patineta" in product.h5.text):
        name = product.h5.get_text(strip = True)
        price = product.h6.get_text(strip = True)
        
        print("El producto " + name + " cuesta " + price)
        
        products.append(name)
        prices.append(price)

print(products)
print(prices)