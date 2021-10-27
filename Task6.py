import json
from bs4 import BeautifulSoup
from Task5 import movies_detail_list

all_movie=movies_detail_list()
def movie_language(language):
    dict={}
    for i in language:
        # print(i)
        if "language" in i:
            Language_1=i["language"]
            # print(Language_1)
            for j in Language_1:
                # print(j)
                if j not in dict:
                    dict[j]=1    
                else:
                    dict[j]+=1
    # print(dict)    
    with open ("task6.json","w+")as f1:
        json.dump(dict,f1,indent=4)
movie_language(all_movie)


