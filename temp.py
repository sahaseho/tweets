# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
import re
import string

data=open(r"E:\tweets\Health-News-Tweets\Health-Tweets\bbchealth.txt","r") 
for line in data:
    #remove  id and timestamp
    data = line.split("|")
    data=data[2]
    #remove hash
    data=data.replace("#","")
    #remove url
    data = re.sub(r"http\S+", "", data)
    data = re.sub(r"www\S+", "", data)
    #convert to lowercase
    data=data.lower()
    #remove words that starts with @
    data = re.sub(r"@\S+", "", data)
    #remove @
    data=data.replace("@","")

    print(data)
