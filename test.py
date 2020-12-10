# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:39:40 2020

@author: Koma
"""

import App
import datetime

# test_lod = [{ 'abby':'51', 'bell':'62', 'dee':'33', 'river':'97' },
#             { 'abby':'54', 'bell':'65', 'dee':'26', 'river':'71' },
#             { 'abby':'45', 'bell':'39', 'dee':'88', 'river':'22' },
#             { 'abby':'57', 'bell':'68', 'dee':'26', 'river':'62' }]

ALL_DATA = App.readCSV('311_Service_Requests_Abbreviated1.csv')
#print(App.departments(ALL_DATA))
#print(App.open_year(ALL_DATA[0]))
#print(App.filterYear(ALL_DATA, 2016, 2018))
#print(App.date('04/23/2016 11:37:00 AM'))

#year_dic = { "year_start": 2016, "year_end": 2018 }
year_dic = { "year": 2016 }
#App.data_by_subject(ALL_DATA, year_dic)
App.data_by_subject_duration(ALL_DATA, year_dic)








