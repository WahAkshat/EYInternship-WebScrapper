import bs4
import requests

fh = open('demo.txt', 'w')

# url = input("Enter the URL:")

req = requests.get("http://www.cvedetails.com/")

# print(soup.get_text())

# print(req.text)

filename="temp.html"

bs = bs4.BeautifulSoup(req.content, "html.parser")

formatted_text = bs.prettify()

# print(formatted_text)

with open(filename, "w+") as f:
    f.write(formatted_text)

fh.write("Formatted text:\n"+formatted_text)

list_of_links = bs.find_all('a')

# print(list_of_links)

grid = bs.find('table', class_ = "grid")


# print(grid)

