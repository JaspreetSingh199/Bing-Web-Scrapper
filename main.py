
from bs4 import BeautifulSoup
import requests

search = input("Enter stuff : ")

params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = soup.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Parent", item.find("a").parent)
        print("Para ? ", item.parent.parent.find("p").text)
        print("Child of a ?", item.find("a").children)
        print("next sibling?", item.find("h2").next_sibling)
        print("prev sibling?", item.find("h2").prev_sibling)

