# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:39:40 2020

@author: Koma
"""

#-----------#
# HW4's code#
#-----------#

import csv
import datetime

# readCSV
def readCSV(filename):
    lod = []
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        headline = next(reader) 
        
        for line in reader:
            dic = dict(zip(headline, line))
            lod.append(dic)
        return lod
   
    
#-----------------------------------------------------------------#
# writeCSV
def writeCSV(filename, lod):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, lod[0].keys())
        writer.writeheader()
        writer.writerows(lod)


#-----------------------------------------------------------------#
# keepOnly
def keepOnly(lod, key, value):
    ret = [item for item in lod if item[key] == value]  
    return ret


#-----------------------------------------------------------------#
# discardOnly
def discardOnly(lod, key, value):
    ret = [item for item in lod if item[key] != value]  
    return ret

#-----------------------------------------------------------------#
# filterRange
def filterRange(lod, key, low, high):
    lst=[]
    
    for item in lod:
        if int(item[key]) >= int(low) and int(item[key]) < int(high):
            lst.append(item)  
    return lst
     
  
#-----------------------------------------------------------------#
# duration
def duration(date1, date2):
    diff = date2 - date1
    return diff.days


#-----------#
# HW5's code#
#-----------#
      
# departments
def departments(lod):
    subject = [item['SUBJECT'] for item in lod]
    return sorted(set(subject))

#-----------------------------------------------------------------#
# open_year 
def open_year(dic):
    return dic["OPEN DATE"][6:10]

#-----------------------------------------------------------------#
# filterYear 
def filterYear(lod, low, high):  
    return [item for item in lod if int(open_year(item)) >= int(low) and int(open_year(item)) < int(high)]         
 
    
#-----------------------------------------------------------------#
# date
def date(string):
    # d= datetime.datetime.strptime(string,"%m/%d/%Y %H:%M:%S %p").strftime('%Y/%m/%d')
    # return datetime.datetime.strptime(d, '%Y/%m/%d')
    year = int(string[6:10])
    day = int(string[3:5])
    month= int(string[0:2])
    newdate = datetime.date(year,month,day)
    return newdate



    

#-----------------------------------------------------------------#
# data_by_subject
def data_by_subject(lod, year_dic):
    # Filter the year range data
    filter_data = filterYear(lod, year_dic['year_start'], year_dic['year_end'])
    #print(filter_data)
    
    # Filter duplicate year
    year = sorted(set([open_year(item) for item in filter_data]))
    
    # Geneate format for every year
    format_lod = []
    for (index, evryear) in enumerate(year):
        #print('Year: ' + evryear)
        values = []
        labels = []
        
        # Filter specific year data
        filter_year_data = filterYear(filter_data, evryear, str(int(evryear) + 1))
        
        # Compute rate for every department
        for dep in departments(filter_year_data):
            #print('Dep: ' + dep)
            # Append department's number of calls first, we calculate the ratio later
            values.append(len(keepOnly(filter_year_data, 'SUBJECT', dep)))
            labels.append(dep)
            
        format_dic = {}
        format_dic['values'] = [i * 100 / sum(values) for i in values]
        format_dic['labels'] = labels
        format_dic['domain'] = {"column": index}
        format_dic['name'] = evryear
        format_dic['hole'] = .4
        format_dic['type'] = 'pie'    
        format_lod.append(format_dic)
        #print('\n===============================')
    
    print(format_lod)
    return format_lod
        
    
#-----------------------------------------------------------------#
# data_by_subject
def data_by_subject_duration(lod, year_dic):
    # Filter the year data
    filter_data = filterYear(lod, year_dic['year'], str(int(year_dic['year']) + 1))
    #print(filter_data)
    
    # Geneate format for every department
    format_lod = []
    for dep in departments(filter_data):
        #print('Dep: ' + dep)
        req_duration = []       
        
        # Retrieve date of every department first
        dep_data = keepOnly(filter_data, 'SUBJECT', dep)
        # print(dep_data)
        # print()
        
        # Next, we compute duration time and amount for every department
        for item in dep_data:
            req_duration.append(duration(date(item['OPEN DATE']), date(item['CLOSED DATE'])))
        
        #print(req_duration)
        
        format_dic = {}
        format_dic['x'] = list(set(req_duration))
        format_dic['y'] = [req_duration.count(i) for i in set(req_duration)]
        format_dic['name'] = dep
        format_dic['mode'] = 'markers'
        format_dic['type'] = 'scatter'    
        format_lod.append(format_dic)
        #print('\n===============================')
        
    return format_lod

    
        
    
    
    
    