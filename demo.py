# Importing the library requests and beautiful soup
import requests
import bs4

result = requests.get("http://www.example.com")
print(result.text)