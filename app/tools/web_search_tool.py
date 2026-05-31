import requests
from bs4 import BeautifulSoup

def web_search(query):
    url = "https://duckduckgo.com/html/"
    res = requests.get(url, params={"q": query})
    soup = BeautifulSoup(res.text, "html.parser")

    results = []

    for a in soup.find_all("a", class_="result__a", limit=5):
        results.append(a.text)

    return results