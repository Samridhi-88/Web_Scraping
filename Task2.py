import requests
from bs4 import BeautifulSoup
import pprint 
import json
# from Task1 import my_1_task
from Task1 import scrap_movie_list

movie=scrap_movie_list()
def group_by_year(movie):
    d={}
    for i in movie:
        movie_year=[]
        year=i["Year"]
        #print(year)
        if year not in d:
            for j in movie:
                # print(j)
                if j["Year"]==year:
                    movie_year.append(j)
            # print(movie_year)        
                d[year]=movie_year
            # print(d)
            with open("task2.json","w+") as movie_data:
                json.dump(d,movie_data,indent=4)
            
    return d

                
            
        
group_by_year(movie)






