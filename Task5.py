import json
from Task1 import scrap_movie_list
from Task4 import scrape_movie_details

all_movies=scrap_movie_list()
top_movies = all_movies[:100]
# print(top_movies)
def movies_detail_list():
    list1=[]
    for i in top_movies:
        for j in i:
            # print(j)
            if j=="url":
                list1.append(scrape_movie_details(i["url"]))
        # print(list1)
    with open("task5.json","w") as file5:
        json.dump(list1,file5,indent = 4)
    file5.close()
    return list1
movies_detail_list()
    