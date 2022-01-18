import sys
import time

from requests import get
from bs4 import BeautifulSoup

def find_links(page):
    print("Scanning:", page)
    soup1=BeautifulSoup(get(page).text)
    links=soup1.select("a")

    linkstrings=list()
    for L in links:
        string=str(L.get("href"))
        if string[0:5]=="/wiki":
            if ":" not in string:
                if "#" not in string:
                    linkstrings.append("https://en.wikipedia.org"+string)
    return linkstrings

start="https://en.wikipedia.org/wiki/"
target="https://en.wikipedia.org/wiki/"

print("Start", start)
print("Target", target)
not_found=True
located={"Start":start}
to_visit=list()
current=Startn_visited=0
while not_found:
    links=find_links(current)
    for lin in links:
        if lin not in located:
            located[lin]=current
            to_visit.append(lin)
        if lin==target:
            print("Target Located")
            not_found=False

    n_visited+=1
    current=to_visit[n_visited]
print(target)
while located[target]!=start:
    print(located[target])
    target=located[target]
print("Pages Scanned:",n_visited)
