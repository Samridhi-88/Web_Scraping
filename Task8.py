from Task1 import scrap_movie_list
import os 
import requests

movies=scrap_movie_list()
movie=movies[:100]
def text_file():
    for i in movie:
        # print(i)
        path=("/home/admin123/Desktop/web scraping/eight_task"+i["Moviename"]+".text")
        if os.path.exists(path):
            pass
        else:
            creating=open("/home/admin123/Desktop/web scraping/eight_task"+i["Moviename"]+".text","w+")
            url=requests.get(i["url"])
            a=creating.write(url.text)
            creating.close()

text_file()





