import openpyxl
from selenium import webdriver
from bs4 import BeautifulSoup

glassdoor = webdriver.Firefox()
glassdoor.get("https://www.glassdoor.com/Interview/Google-Product-Manager-Interview-Questions-EI_IE9079.0,6_KO7,22_IP2.htm")
html = glassdoor.page_source
gdsoup = BeautifulSoup(html)
descr = list()
for tag in gdsoup.find_all('p', {"class":"interviewDetails continueReading interviewContent mb-xsm"}):
    descr.append(tag)
    print(tag.text, "\n")
