import bs4, requests

url = "https://scrapepark.org/spanish/"
response = requests.get(url)
print("Estado de la request " + str(response.status_code) + " Status: " + "Success" if response.status_code < 400 else "Failed")

soup = bs4.BeautifulSoup(response.text, "html.parser")

divImgBoxed = soup.find_all("div", class_ = "img-box")

index = 0

for img in divImgBoxed:
    boxedImg = img.find("img", recursive = False)

    if boxedImg and boxedImg["src"]:
        index += 1
        print(boxedImg["src"])

        responseImg = requests.get(f"https://scrapepark.org/{boxedImg["src"]}")
        
        with open(f"imagen{index}" + (".png" if boxedImg["src"][-3:] == "png" else ".jpg"), "wb") as file:
            file.write(responseImg.content)