from selenium import webdriver
from bs4 import BeautifulSoup

wd = "WORKING_DIRECTORY_HERE"
page = "GLASSDOOR_LINK_HERE"

def glassdoor_questions():
    import os
    os.chdir(wd)

    glassdoor = webdriver.Firefox()
    glassdoor.get(page)
    html = glassdoor.page_source
    gdsoup = BeautifulSoup(html)
    descr = list()
    for tag in gdsoup.find_all('p', {"class":"interviewDetails continueReading interviewContent mb-xsm"}):
        descr.append(tag)
        print(tag.text, "\n")

glassdoor_questions()
