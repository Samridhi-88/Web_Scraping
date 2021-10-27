import requests
from bs4 import BeautifulSoup
import json
from Task1 import scrap_movie_list
movie_url = "https://www.rottentomatoes.com/m/toy_story_4"
# moviename = "toy_story_4"

def scrape_movie_details(movie_url):
    url = requests.get(movie_url)
    data = BeautifulSoup(url.text,"html.parser")
    movies_name=data.find("h1",class_="scoreboard__title").get_text()
    mainDiv = data.find_all("li",class_ = "meta-row clearfix")
    # pprint(mainDiv)
    dict1 = {}
    dict1["movies_name"]=movies_name
    dict1["url"]=movie_url
    for i in mainDiv:
        l=[]
        a = i.text
        b = a.split()
        # print(b)
        if "Rating:" in b:
            dict1["Rating"] =  b[1]
        elif "Language:" in b:
            l.append(b[-1])
            dict1["language"]=l
            # print(dict1)
        elif "Genre" in b:
            dict1["Genre:"]=b[1:]
            # print(dict1)
        elif "Director:" in b:
            i = 0
            list2 = []
            while i < len(b):
                if i == 0:
                    i += 1
                    continue
                list2.append(b[i])
                i += 1
            l1=""
            for i in list2:
                for j in i:
                    if j=="":
                        continue
                    else:
                        l1+=j
            list3=l1.split(",")

            dict1["director"] = list3
        elif "Producer:" in b:
            dict1["Producer"] = b[1:]
        elif "Runtime:" in b:
            l3=[]
            for j in b:
                if j !="Runtime:":
                    s=j.strip()[:-1]
                    l3.append(int(s))
                for i in range(len(l3)):
                    if i ==0:
                        minute=l3[i]*60
                    elif i==1:
                        minute=l3[0]*60+l3[i]
            dict1["Runtime"]=minute
    with open("task4.json","w") as file4:
        json.dump(dict1,file4,indent = 4)
    file4.close()
    return dict1
scrape_movie_details(movie_url)



