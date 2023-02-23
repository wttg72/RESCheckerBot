import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import time
import ssl
import requests

TOKEN = "6280442518:AAGO2RrGxgetLZGeB_mVOOzHN4keoc_bvQM"
chat_id = "-1001820093494"

url = "https://www.hastor.com.sg/course/res/real-estate-salesperson-res-course/"
ssl._create_default_https_context = ssl._create_unverified_context
req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
page_html = urlopen(req).read()
urlopen(req).close()

page_soup = soup(page_html, "html.parser")
select = page_soup.find("select", {"id": "intake"})

message = url

for option in select.find_all('option'):
    print(option["value"])
    message += str(option["value"]) + "\n\n"
    print(message)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message