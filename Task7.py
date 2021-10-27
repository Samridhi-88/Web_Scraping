import json
from bs4 import BeautifulSoup
from Task5 import movies_detail_list

director_1=movies_detail_list()
def data_director(director_):
    details_dict={}
    for i in director_:
        # print(i)
        dir_name=i["director"]
        # print(dir_name)
        for j in dir_name:
            # print(j)
            if j not in details_dict:
                dir_name=j
                details_dict[j]=1
            else:
                details_dict[j]+=1
                
        # details_dict[dir_change]=list_1
        print(details_dict)
    with open("task7.json","w+")as file:
        json.dump(details_dict,file,indent=4)
data_director(director_1)


