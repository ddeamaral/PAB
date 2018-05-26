import requests
from bs4 import BeautifulSoup
from pprint import pprint as p

def main():

    base_uri = "https://pokemondb.net"
    page = requests.get(f"{base_uri}/pokedex/all")
    soup = BeautifulSoup(page.content, "html.parser")
    # p(soup.prettify())

    anchors = soup.find_all(lambda tag: tag.name == "a" and "/pokedex" in tag.get("href")) #"a", href=True)

    for a in anchors:
        content = requests.get(f'{base_uri}{a["href"]}')
        parse_pokemon_page(BeautifulSoup(content.content, "html.parser"))
        # print("found the url", a["href"])


def parse_pokemon_page(content):
    print(content)

if __name__ == "__main__":
    main()