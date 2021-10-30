import json
from bs4 import BeautifulSoup
with open("task5.json","r")as f:
    data=json.load(f)
movie=data
def data_director(movie_dic):
    dict={}
    for director in movie_dic:
        # print(director)
        for director_name in director["director"]:
            # print(director_name)
            dic={}
            c=0
            for dic_movie in movie_dic:
                if director_name in dic_movie["director"] and "language" in dic_movie:
                        # print("right")
                    c+=1
                    for language_name in dic_movie["language"]:
                        # print(language_name)
                        dic[language_name]=c
            # print(dic)
        dict[director_name]=dic
    # print(dict)
    with open("task10.json","w+") as f:
        json.dump(dict,f,indent=4) 
data_director(movie)


