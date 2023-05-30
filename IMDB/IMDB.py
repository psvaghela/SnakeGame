from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.imdb.com/chart/top/"
source = requests.get(url)


soup = BeautifulSoup(source.content,'lxml')
movies = soup.find_all('tr')

with open('movies.csv','w',newline='',encoding='utf8') as f:
  thewriter = writer(f)
  header = ['Title','Rating']
  thewriter.writerow(header)
  for movie in movies:
    t = movie.find("td",{'class':"titleColumn"})
    if(t!=None):
      title = t.get_text(strip = True)
    else:
      continue
    r = movie.find("strong")
    if(r!=None):
      rating = r.get_text(strip = True)
    else:
      continue
    info = [title,rating]
    thewriter.writerow(info)

