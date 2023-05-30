from bs4 import BeautifulSoup
import requests
import pandas as pd

lt = []
lr = []

url = "https://www.imdb.com/chart/top/"
source = requests.get(url)

#print(source)
soup = BeautifulSoup(source.content,'lxml')
movies = soup.find_all('tr')
print(movies)
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
    lt.append(title)
    lr.append(rating)

dic = {'Title':lt, 'Rating':lr}
xd = pd.DataFrame(dic)
xd.to_csv("movie1.csv",header=True,index=False)
#print(xd.columns)