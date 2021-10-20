import requests
from bs4 import BeautifulSoup
# import pprint 
import json

link=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
soup=BeautifulSoup(link.text,"html.parser")
#print(soup)
titles=soup.find_all("td", class_="unstyled articleLink")

def scrap_movie_list():
    maindiv=soup.find("div",class_="container")
    #print(mainDiv)
    table= maindiv.find("div",class_="panel-body content_body allow-overflow")
    
    all_tr= table.find_all('tr')
    list1=[]
    for i in all_tr:
        all_td= i.find_all('td')
        dic={}
        for j in all_td:
            moviename=i.find("a",class_="unstyled articleLink")["href"][3:]
            dic["Moviename"]=moviename

            rating=i.find("span",class_="tMeterScore").get_text()[:3]
            dic["Rating"]=int(rating)

            year=i.find("a",class_="unstyled articleLink").get_text()[-5:-1]
            dic["Year"]=year

            rank=i.find("td",class_="bold").get_text()
            dic["Rank"]=rank

            riviews=i.find("td",class_="right hidden-xs").get_text()
            dic["Riviews"]=riviews

            url=i.find("a",class_="unstyled articleLink")["href"]
            url_add= "https://www.rottentomatoes.com"+url
            dic["url"]=url_add
        for new in dic:
            if new!={}:
                if dic not in list1:
                    list1.append(dic)
        # list1.append(dic)
        with open("task1.json","w+") as movie_data:
            json.dump(list1,movie_data,indent=4)        
    return list1
movie_data=scrap_movie_list()








