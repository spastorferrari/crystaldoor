# ---------------------------------------------------------- IMPORT DEPENDENCIES
from selenium import webdriver
from bs4 import BeautifulSoup
import argparse as np
# --------------------------------------------------------------------- ARGPARSE
parser = np.ArgumentParser()
parser.add_argument("link", type=str, help='insert link to parse.')
args = parser.parse_args()
page = args.link
# ------------------------------------------------------------------------ LOGIC
def glassdoor_questions():
    glassdoor = webdriver.Firefox()
    glassdoor.get(page)
    html = glassdoor.page_source
    gdsoup = BeautifulSoup(html, features="html.parser")
    descr = list()
    for tag in gdsoup.find_all('p', {"class":"interviewDetails continueReading interviewContent mb-xsm"}):
        descr.append(tag)
        print(tag.text, "\n")
glassdoor_questions()
