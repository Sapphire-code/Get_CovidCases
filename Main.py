# importing required libraries
import os
from os import *
import sys
import time
import requests
import bs4
from bs4 import *
from requests import *
from bs4 import BeautifulSoup
import plyer
from plyer import notification


# connecting to website and giving cases, deaths and recoveries and then storing them in a variable
def Get_cdr():
    global cases
    global deaths
    global reco
    # connect to the website
    myvar = requests.get("https://www.worldometers.info/coronavirus/")

    # getting source code of the website
    soup = BeautifulSoup(myvar.text, 'lxml')
    # Getting Cases, Deaths and Recoveries
    get_cases = soup.find_all('div', class_ = 'maincounter-number')

    # storing in a variable
    cases = get_cases[0].text
    deaths = get_cases[1].text
    reco = get_cases[2].text
    # printing them to test if this fails then the program will crash
    print("Cases: " + cases)
    print("Deaths: " + deaths)
    print("Recovered: " + reco)


Get_cdr()
input()
