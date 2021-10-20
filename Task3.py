from Task1 import movie_data
import json
def group_by_decade(movies):
    list=[]
    i=0
    while i<len(movies):
        #print(i)
        for key in movies[i]:
            # print(movies[i][key])
            if key=="Year":
                mod=int(movies[i][key])%10
                decade=int(movie_data[i][key])-mod
                list.append(decade)
        i+=1
    list.sort()
    # print(list)
    dic={}
    j=0
    while j<len(movies):
        dec=list[j]+10
        year_list=[]
        k=0
        while k<len(list):
            if int(movies[k]["Year"])>list[j] and int(movies[k]["Year"])<dec:
                year_list.append(movies[k])
            dic[list[j]]=year_list
            k+=1
        j+=1
    with open("Task3.json","w+") as year_info:
        json.dump(dic,year_info,indent=4)
        return dic
store=group_by_decade(movies=movie_data)


