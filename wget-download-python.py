# pip install wget
import wget
url = "https://github.com/robinsonbrz/python-snippets/archive/refs/heads/main.zip"
filename = wget.download(url)
