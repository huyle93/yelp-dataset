#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 23:12:54 2017

@author: huyle
"""

import json

with open('sample-checkin.json') as json_data:
    d = json.load(json_data)

#print(d["time"]["Thursday"]["21:00"])
#print(d["time"]["Thursday"]," ",d["time"]["Thursday"]["21:00"])



for day in d["time"]:
    for time in d["time"][day]:
        checkin = d["time"][day][time]
        print("On {} customer checkin at {} for {} time/times".format(day, time, checkin))
#            print(checkin)
    
print("business_id: " + d["business_id"])


#//"time": {"Monday": {"13:00": 1}, "Thursday": {"20:00": 1, "13:00": 1}, "Sunday": {"19:00": 1}, "Wednesday": {"17:00": 1}, "Saturday": {"21:00": 1, "16:00": 1}}, "business_id": "kREVIrSBbtqBhIYkTccQUg"}