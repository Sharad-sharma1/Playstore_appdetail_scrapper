from celery import shared_task
from django.http import HttpResponse
from google_play_scraper import app
from .models import App
from bs4 import BeautifulSoup
import requests

urll = "https://play.google.com/store/games?hl=en&gl=US"
#the Request.get will fetch all details of the url mnentioned page
resp = requests.get(urll) 
'''from page we will take only content because in content we will get the packages links which we required.
we are using BeautifulSoup to srapping the web details also parsing to html so that we can use BeautifulSoup functions such as finall, get etc.'''
soup = BeautifulSoup(resp.content , 'html.parser') 

@shared_task(bind=True)
def test_func(self):
    listt = []
    for link in soup.find_all('a'): 
        #below we are taking only those href which having "id=com." because in that we will get "/store/apps/details?id=com.bycodec.project_drift"
        if 'id=com.' in link.get('href'):
            '''We are getting anchor tags now inside that we are taking href, splitting it with '=' and then taking second element of list
            result :- from "/store/apps/details?id=com.bycodec.project_drift" to "com.bycodec.project_drift". '''
            listt.append(link.get('href').split('=')[1]) 
            #Break because we are taking first 20 app packages
            if len(listt) == 20:
                break
    #there are some apps which might be having lakhs of review, so we are taking top5 latest reviews
    for i in range(len(listt)):
        a = app(listt[i])
        print(f"App {a['title']} has been added to DB")
        app_detail = App(title=a['title'], summary= a['summary'], contentRating = a['contentRating'], genre = a['genre'], installs = a['installs'] , url = a['url'])
        app_detail.save()
    return "All Apps has been added to DB"