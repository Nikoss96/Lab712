import requests
import html
import re
from bs4 import BeautifulSoup
import json
"""
check = requests.get("http://172.18.160.156")
soup = BeautifulSoup(check.text, 'html.parser')
hmm = soup.find_all(id="Json",style="white-space:pre-wrap;")
res = json.loads(hmm[0].text)
"""

dict = {"Open":True,"Closed":False}
def get_sensors() -> str:
    check = requests.get("http://172.18.160.156")
    soup = BeautifulSoup(check.text, 'html.parser')
    hmm = soup.find_all(id="Json",style="white-space:pre-wrap;")
    res = json.loads(hmm[0].text)
    time = res["datetime"]["time"]
    date = res["datetime"]["data"]
    door = dict[res["det0"]["state"]]
    lwindow = dict[res["det1"]["state"]]
    rwindow = dict[res["det2"]["state"]]
    temp = res["det6"]["temp"]
    humi = res["det6"]["hum"]
    sensors = " time: " + str(time) + " date: " + str(date) + " door: " + str(door) + " lwindow: " + str(lwindow) + " rwindow: " + str(rwindow) + " temp: " + str(temp) + " humi: " + str(humi)
    #time , date , door , lwindow , rwindow , temp , humi
    return sensors