import sys
import time



if "F:\\python_stuff" not in sys.path:
    sys.path.append("F:\\python_stuff")
if "D:\\python_stuff" not in sys.path:
    sys.path.append("D:\\python_stuff")
if "G:\\python_stuff" not in sys.path:
    sys.path.append("G:\\python_stuff")
if "E:\\python_stuff" not in sys.path:
    sys.path.append("E:\\python_stuff")

from requests import get
from bs4 import BeautifulSoup

start_time=time.time()

def find_links(page):
    print("checking:",page)
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

print("Start:",start)
print("Target:",target)
not_found=True
located={"Start:":start}
to_visit=list()
current=start
n_visited=0
while not_found:
    links=find_links(current)
    for lin in links:

        if lin not in located:
            located[lin]=current
            to_visit.append(lin)
        if lin==target:
            print("TARGET FOUND!")
            not_found=False

    n_visited+=1
    current=to_visit[n_visited]

print(target)
while located[target]!=start:
    print (located[target])
    target=located[target]

print("pages visited:",n_visited)

input("Press any Key >>>")

finish_finish=time.time()
print(finish_finish-start_time)
