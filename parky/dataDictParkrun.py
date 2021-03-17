#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:17:06 2020

@author: bfc782
"""
from bs4 import BeautifulSoup
import requests
import json

# defining data source and plot parameters
dataDict = {'UK':{'url':'https://www.parkrun.org.uk/results/courserecords/','plot':'bo'},
           'PL':{'url':'https://www.parkrun.pl/results/courserecords/','plot':'ro'},
           'DE':{'url':'https://www.parkrun.com.de/results/courserecords/','plot':'yo'},
           'IT':{'url':'https://www.parkrun.it/results/courserecords/','plot':'go'},
           'FR':{'url':'https://www.parkrun.fr/results/courserecords/','plot':'ko'}
           }
# setting headers to pull data
session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)' 
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept' : 'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8', 
           'Accept-Language': 'en-US,en;q=0.8'}

# function that converts from text('mm:ss') to int(seconds) 
def get_sec(time_str):
    """Get Seconds from time."""
    if time_str == '':
        return int('0')
    else:
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)

# looping through dictionary of countries
for country in dataDict:
    url = dataDict[country]['url']
    req = session.get(url, headers=headers)
    bs = BeautifulSoup(req.text, 'html.parser')
# how many table row items are there to loop through in the table body?
    eventCount = len(bs.find('tbody'))
    dataList = []
    for prEvent in range(eventCount):
        eventLoc = bs.find('table').find('tbody').find_all('tr')[prEvent].find_all('td')[0].get_text()
        eventFrecSec = get_sec(bs.find('table').find('tbody').find_all('tr')[prEvent].find_all('td')[3].get_text())
        eventMrecSec = get_sec(bs.find('table').find('tbody').find_all('tr')[prEvent].find_all('td')[7].get_text())
        diffFMPC = 100*round((eventFrecSec-eventMrecSec)/eventMrecSec,2)
        dataList[len(dataList):] = [[eventLoc,eventMrecSec,diffFMPC]]    
    dataDict[country]["data"] = dataList

with open('parkrunRecords.json', 'w') as f:
    json.dump(dataDict, f)
