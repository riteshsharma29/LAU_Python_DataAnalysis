#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import matplotlib.patches as mpatches
import numpy as np

from matplotlib.font_manager import FontProperties

# fontP = FontProperties()
# fontP.set_size('xx-small')

import sys

#13,17,18,20,21,22,24,25,2627,30,32,33,34,36

df = pd.read_excel("All results 2017 - 2018.xlsx",sheet_name='Data')

#  Gender

df['Gender'].value_counts().plot(kind='pie',autopct='%1.1f%%',title='FIGURE 1 RESPONDENTS BY GENDER')
plt.savefig('fig1.jpg')
plt.clf()


#  RESPONDENTS BY TERM OF GRADUATION

term_labels = list(set(df['Graduation_Term'].to_list()))
term_count  = df['Graduation_Term'].value_counts()
plt.figure(figsize=(10,5))
sns.barplot(term_count.index, term_count.values, alpha=0.8)
plt.ylabel('Count', fontsize=12)
plt.xlabel('FIGURE 2 RESPONDENTS BY TERM OF GRADUATION', fontsize=12)
legend_dict = { 'Spring 2018' : '#3498db', 'Fall 2017' : 'orange', 'Summer 2018' : '#2ecc71' }
patchList = []
for key in legend_dict:
        data_key = mpatches.Patch(color=legend_dict[key], label=key)
        patchList.append(data_key)
plt.legend(handles=patchList)
plt.savefig('fig2.jpg')
plt.clf()

#  RESPONDENTS BY SCHOOL

term_sccount  = df['School'].value_counts()
plt.figure(figsize=(10,5))
ax = sns.barplot(term_sccount.index, term_sccount.values, alpha=0.8)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.ylabel('Count', fontsize=12)
plt.xlabel('FIGURE 3 RESPONDENTS BY SCHOOL', fontsize=8)
legend_dict_sc = { 'AKSOB' : '#3498db', 'SAS' : 'orange', 'SOE' : '#2ecc71', 'SArD':'firebrick','SOP':'mediumpurple','ARCSON':'sienna'}
patchListsc = []
for key in legend_dict_sc:
        data_key = mpatches.Patch(color=legend_dict_sc[key], label=key)
        patchListsc.append(data_key)
plt.legend(handles=patchListsc)
plt.savefig('fig3.jpg')
plt.clf()

#  Employment status

es_labels = list(set(df['Q1_Your employment status:_Your employment status:'].to_list()))
es = df['Q1_Your employment status:_Your employment status:'].to_list()
es_1 = []
es_2 = []
es_3 = []
for e in es:
    if e == 'Currently employed':es_1.append('Currently employed')
    if e == 'Currently employed': es_2.append('Unemployed but have been employed at least once since graduating from LAU')
    if e == 'Currently employed': es_3.append('Never been employed')

slices = [len(es_1),len(es_2),len(es_3)]
activities = ['Currently employed','Unemployed but have been employed at least once since graduating from LAU','Never been employed']
cols = ['r','b','m','c','k','g','w','navy','khaki','pink']
plt.pie(slices,
    labels=activities,
    colors=cols,
    startangle=90,
    shadow=True,
    explode=(0,0,0), #0.1 is used to explote the slice-share use 0.0 instead if this feature is not required.
    autopct='%1.1f%%'
)
plt.title('FIGURE4 Employment status',y=-0.10)
plt.savefig('fig4.jpg')
plt.clf()

#  FIGURE 5 ALUMNI CONTINUING HIGHER EDUCATION BASED ON UNDERGRADUATE DEGREE

fig5_prog = df['Program'].to_list()
fig5_grad = df['Q2_Since graduating from LAU, have you earned or pursued:_A graduate degree'].to_list()
fig5_doc = df['Q2_Since graduating from LAU, have you earned or pursued:_A doctoral degree'].to_list()

y_5_1 = []
n_5_1 = []
x_5_1 = []

y_5_2 = []
n_5_2 = []
x_5_2 = []

y_5_3 = []
n_5_3 = []
x_5_3 = []

y_5_4 = []
n_5_4 = []
x_5_4 = []

y_5_5 = []
n_5_5 = []
x_5_5 = []

y_5_6 = []
n_5_6 = []
x_5_6 = []

y_5_7 = []
n_5_7 = []
x_5_7 = []

y_5_8 = []
n_5_8 = []
x_5_8 = []

y_5_9 = []
n_5_9 = []
x_5_9 = []

y_5_10 = []
n_5_10 = []
x_5_10 = []

y_5_11 = []
n_5_11 = []
x_5_11 = []

y_5_12 = []
n_5_12 = []
x_5_12 = []

y_5_13 = []
n_5_13 = []
x_5_13 = []

y_5_14 = []
n_5_14 = []
x_5_14 = []

y_5_15 = []
n_5_15 = []
x_5_15 = []

y_5_16 = []
n_5_16 = []
x_5_16 = []

y_5_17 = []
n_5_17 = []
x_5_17 = []

y_5_18 = []
n_5_18 = []
x_5_18 = []

y_5_19 = []
n_5_19 = []
x_5_19 = []

y_5_20 = []
n_5_20 = []
x_5_20 = []

y_5_21 = []
n_5_21 = []
x_5_21 = []

y_5_22 = []
n_5_22 = []
x_5_22 = []

y_5_23 = []
n_5_23 = []
x_5_23 = []

y_5_24 = []
n_5_24 = []
x_5_24 = []

y_5_25 = []
n_5_25 = []
x_5_25 = []

y_5_26 = []
n_5_26 = []
x_5_26 = []

y_5_27 = []
n_5_27 = []
x_5_27 = []

y_5_28 = []
n_5_28 = []
x_5_28 = []

y_5_29 = []
n_5_29 = []
x_5_29 = []

y_5_30 = []
n_5_30 = []
x_5_30 = []

y_5_31 = []
n_5_31 = []
x_5_31 = []

y_5_32 = []
n_5_32 = []
x_5_32 = []

y_5_33 = []
n_5_33 = []
x_5_33 = []

y_5_34 = []
n_5_34 = []
x_5_34 = []

y_5_35 = []
n_5_35 = []
x_5_35 = []

y_5_36 = []
n_5_36 = []
x_5_36 = []

y_5_37 = []
n_5_37 = []
x_5_37 = []

def filter_fig_5(prog_name,l_5_1,l_5_2,l_5_3,lst_51,lst_52,lst_53):
    for ind_5 in range(0,len(l_5_1)):
        if l_5_1[ind_5] == prog_name and l_5_2[ind_5] == 'Yes' and l_5_3[ind_5] == 'No':lst_51.append('Yes')
        if l_5_1[ind_5] == prog_name and l_5_2[ind_5] == 'No' and l_5_3[ind_5] == 'Yes': lst_52.append('Yes')
        if l_5_1[ind_5] == prog_name and l_5_2[ind_5] == 'No' and l_5_3[ind_5] == 'No': lst_53.append('No')

filter_fig_5('BS in Mathematics',fig5_prog,fig5_grad,fig5_doc,y_5_1,n_5_1,x_5_1)
filter_fig_5('BS in Computer Science',fig5_prog,fig5_grad,fig5_doc,y_5_2,n_5_2,x_5_2)
filter_fig_5('BA in Education', fig5_prog,fig5_grad,fig5_doc,y_5_3,n_5_3,x_5_3)
filter_fig_5('BA in Multimedia Journalism',fig5_prog,fig5_grad,fig5_doc,y_5_4,n_5_4,x_5_4)
filter_fig_5('BS in Economics',fig5_prog,fig5_grad,fig5_doc,y_5_5,n_5_5,x_5_5)
filter_fig_5('BA in Performing Arts',fig5_prog,fig5_grad,fig5_doc,y_5_6,n_5_6,x_5_6)
filter_fig_5('BA in Political Sc/Int.Affairs', fig5_prog,fig5_grad,fig5_doc,y_5_7,n_5_7,x_5_7)
filter_fig_5('BS in Graphic Design',fig5_prog,fig5_grad,fig5_doc,y_5_8,n_5_8,x_5_8)
filter_fig_5('BE in Industrial Engineering',fig5_prog,fig5_grad,fig5_doc,y_5_9,n_5_9,x_5_9)
filter_fig_5('Dip.in Learn. Dis.& Giftedness',fig5_prog,fig5_grad,fig5_doc,y_5_10,n_5_10,x_5_10)
filter_fig_5('BS in Nutr.&Diet. Coord. Prog.',fig5_prog,fig5_grad,fig5_doc,y_5_11,n_5_11,x_5_11)
filter_fig_5('BA in English',fig5_prog,fig5_grad,fig5_doc,y_5_12,n_5_12,x_5_12)
filter_fig_5('BS in Hosp. & Tourism Manag.',fig5_prog,fig5_grad,fig5_doc,y_5_13,n_5_13,x_5_13)
filter_fig_5('BS in Pharmacy',fig5_prog,fig5_grad,fig5_doc,y_5_14,n_5_14,x_5_14)
filter_fig_5('Teaching Diploma',fig5_prog,fig5_grad,fig5_doc,y_5_15,n_5_15,x_5_15)
filter_fig_5('BA in Fashion Design',fig5_prog,fig5_grad,fig5_doc,y_5_16,n_5_16,x_5_16)
filter_fig_5('BS in Biology',fig5_prog,fig5_grad,fig5_doc,y_5_17,n_5_17,x_5_17)
filter_fig_5('BS in Bioinformatics',fig5_prog,fig5_grad,fig5_doc,y_5_18,n_5_18,x_5_18)
filter_fig_5('BS in Chemistry', fig5_prog,fig5_grad,fig5_doc,y_5_19,n_5_19,x_5_19)
filter_fig_5('BS in Interior Design',fig5_prog,fig5_grad,fig5_doc,y_5_20,n_5_20,x_5_20)
filter_fig_5('BS in Nutrition', fig5_prog,fig5_grad,fig5_doc,y_5_21,n_5_21,x_5_21)
filter_fig_5('BE in Civil Engineering',fig5_prog,fig5_grad,fig5_doc,y_5_22,n_5_22,x_5_22)
filter_fig_5('BS in Business', fig5_prog,fig5_grad,fig5_doc,y_5_23,n_5_23,x_5_23)
filter_fig_5('BE in Electrical Engineering',fig5_prog,fig5_grad,fig5_doc,y_5_24,n_5_24,x_5_24)
filter_fig_5('BA in Social Work',fig5_prog,fig5_grad,fig5_doc,y_5_25,n_5_25,x_5_25)
filter_fig_5('BA in Translation',fig5_prog,fig5_grad,fig5_doc,y_5_26,n_5_26,x_5_26)
filter_fig_5('Bachelor of Architecture',fig5_prog,fig5_grad,fig5_doc,y_5_27,n_5_27,x_5_27)
filter_fig_5('BA in Psychology',fig5_prog,fig5_grad,fig5_doc,y_5_28,n_5_28,x_5_28)
filter_fig_5('BA in Communication Arts',fig5_prog,fig5_grad,fig5_doc,y_5_29,n_5_29,x_5_29)
filter_fig_5('BE in Petroleum Engineering',fig5_prog,fig5_grad,fig5_doc,y_5_30,n_5_30,x_5_30)
filter_fig_5('BE in Computer Engineering', fig5_prog,fig5_grad,fig5_doc,y_5_31,n_5_31,x_5_31)
filter_fig_5('BS in Nursing',fig5_prog,fig5_grad,fig5_doc,y_5_32,n_5_32,x_5_32)
filter_fig_5('BA in Television and Film',fig5_prog,fig5_grad,fig5_doc,y_5_33,n_5_33,x_5_33)
filter_fig_5('BA in Interior Architecture',fig5_prog,fig5_grad,fig5_doc,y_5_34,n_5_34,x_5_34)
filter_fig_5('BA in Political Science',fig5_prog,fig5_grad,fig5_doc,y_5_35,n_5_35,x_5_35)
filter_fig_5('BA in Fine Arts',fig5_prog,fig5_grad,fig5_doc,y_5_36,n_5_36,x_5_36)
filter_fig_5('BE in Mechanical Engineering',fig5_prog,fig5_grad,fig5_doc,y_5_37,n_5_37,x_5_37)


fig_per_5_1 = (len(y_5_1) + len(n_5_1)) * 100 / (len(y_5_1) + len(n_5_1) + len(x_5_1))
fig_per_5_1 = round(fig_per_5_1)
fig_per_5_1_s = 'BS in Mathematics : ' +  str(fig_per_5_1) + "%"

fig_per_5_2 = (len(y_5_2) + len(n_5_2)) * 100 / (len(y_5_2) + len(n_5_2) + len(x_5_2))
fig_per_5_2 = round(fig_per_5_2)
fig_per_5_2_s = 'BS in Computer Science : ' +  str(fig_per_5_2) + "%"

fig_per_5_3 = (len(y_5_3) + len(n_5_3)) * 100 / (len(y_5_3) + len(n_5_3) + len(x_5_3))
fig_per_5_3 = round(fig_per_5_3)
fig_per_5_3_s = 'BA in Education : ' +  str(fig_per_5_3) + "%"

fig_per_5_4 = (len(y_5_4) + len(n_5_4)) * 100 / (len(y_5_4) + len(n_5_4) + len(x_5_4))
fig_per_5_4 = round(fig_per_5_4)
fig_per_5_4_s = 'BA in Multimedia Journalism : ' +   str(fig_per_5_4) + "%"

fig_per_5_5 = (len(y_5_5) + len(n_5_5)) * 100 / (len(y_5_5) + len(n_5_5) + len(x_5_5))
fig_per_5_5 = round(fig_per_5_5)
fig_per_5_5_s = 'BS in Economics : ' + str(fig_per_5_5) + "%"

fig_per_5_6 = (len(y_5_6) + len(n_5_6)) * 100 / (len(y_5_6) + len(n_5_6) + len(x_5_6))
fig_per_5_6 = round(fig_per_5_6)
fig_per_5_6_s = 'BA in Performing Arts : ' +  str(fig_per_5_6) + "%"

fig_per_5_7 = (len(y_5_7) + len(n_5_7)) * 100 / (len(y_5_7) + len(n_5_7) + len(x_5_7))
fig_per_5_7 = round(fig_per_5_7)
fig_per_5_7_s = 'BA in Political Sc/Int.Affairs : ' + str(fig_per_5_7) + "%"

fig_per_5_8 = (len(y_5_8) + len(n_5_8)) * 100 / (len(y_5_8) + len(n_5_8) + len(x_5_8))
fig_per_5_8 = round(fig_per_5_8)
fig_per_5_8_s = 'BS in Graphic Design : ' +  str(fig_per_5_8) + "%"

fig_per_5_9 = (len(y_5_9) + len(n_5_9)) * 100 / (len(y_5_9) + len(n_5_9) + len(x_5_9))
fig_per_5_9 = round(fig_per_5_9)
fig_per_5_9_s = 'BE in Industrial Engineering : ' + str(fig_per_5_9) + "%"

fig_per_5_10 = (len(y_5_10) + len(n_5_10)) * 100 / (len(y_5_10) + len(n_5_10) + len(x_5_10))
fig_per_5_10 = round(fig_per_5_10)
fig_per_5_10_s = 'Dip.in Learn. Dis.& Giftedness : ' +  str(fig_per_5_10) + "%"

fig_per_5_11 = (len(y_5_11) + len(n_5_11)) * 100 / (len(y_5_11) + len(n_5_11) + len(x_5_11))
fig_per_5_11 = round(fig_per_5_11)
fig_per_5_11_s = 'BS in Nutr.&Diet. Coord. Prog. : ' +  str(fig_per_5_11) + "%"

fig_per_5_12 = (len(y_5_12) + len(n_5_12)) * 100 / (len(y_5_12) + len(n_5_12) + len(x_5_12))
fig_per_5_12 = round(fig_per_5_12)
fig_per_5_12_s = 'BA in English : ' +  str(fig_per_5_12) + "%"

fig_per_5_13 = (len(y_5_13) + len(n_5_13)) * 100 / (len(y_5_13) + len(n_5_13) + len(x_5_13))
fig_per_5_13 = round(fig_per_5_13)
fig_per_5_13_s = 'BS in Hosp. & Tourism Manag. : ' +  str(fig_per_5_13) + "%"

fig_per_5_14 = (len(y_5_14) + len(n_5_14)) * 100 / (len(y_5_14) + len(n_5_14) + len(x_5_14))
fig_per_5_14 = round(fig_per_5_14)
fig_per_5_14_s = 'BS in Pharmacy : ' +  str(fig_per_5_14) + "%"

fig_per_5_15 = (len(y_5_15) + len(n_5_15)) * 100 / (len(y_5_15) + len(n_5_15) + len(x_5_15))
fig_per_5_15 = round(fig_per_5_15)
fig_per_5_15_s = 'Teaching Diploma : ' +  str(fig_per_5_15) + "%"

fig_per_5_16 = (len(y_5_16) + len(n_5_16)) * 100 / (len(y_5_16) + len(n_5_16) + len(x_5_16))
fig_per_5_16 = round(fig_per_5_16)
fig_per_5_16_s = 'BA in Fashion Design : ' +  str(fig_per_5_16) + "%"

fig_per_5_17 = (len(y_5_17) + len(n_5_17)) * 100 / (len(y_5_17) + len(n_5_17) + len(x_5_17))
fig_per_5_17 = round(fig_per_5_17)
fig_per_5_17_s = 'BS in Biology : ' +  str(fig_per_5_17) + "%"

fig_per_5_18 = (len(y_5_18) + len(n_5_18)) * 100 / (len(y_5_18) + len(n_5_18) + len(x_5_18))
fig_per_5_18 = round(fig_per_5_18)
fig_per_5_18_s = 'BS in Bioinformatics : ' +  str(fig_per_5_18) + "%"

fig_per_5_19 = (len(y_5_19) + len(n_5_19)) * 100 / (len(y_5_19) + len(n_5_19) + len(x_5_19))
fig_per_5_19 = round(fig_per_5_19)
fig_per_5_19_s = 'BS in Chemistry : ' + str(fig_per_5_19) + "%"

fig_per_5_20 = (len(y_5_20) + len(n_5_20)) * 100 / (len(y_5_20) + len(n_5_20) + len(x_5_20))
fig_per_5_20 = round(fig_per_5_20)
fig_per_5_20_s = 'BS in Interior Design : ' + str(fig_per_5_20) + "%"

fig_per_5_21 = (len(y_5_21) + len(n_5_21)) * 100 / (len(y_5_21) + len(n_5_21) + len(x_5_21))
fig_per_5_21 = round(fig_per_5_21)
fig_per_5_21_s = 'BS in Nutrition : ' +  str(fig_per_5_21) + "%"

fig_per_5_22 = (len(y_5_22) + len(n_5_22)) * 100 / (len(y_5_22) + len(n_5_22) + len(x_5_22))
fig_per_5_22 = round(fig_per_5_22)
fig_per_5_22_s = 'BE in Civil Engineering : ' +  str(fig_per_5_22) + "%"

fig_per_5_23 = (len(y_5_23) + len(n_5_23)) * 100 / (len(y_5_23) + len(n_5_23) + len(x_5_23))
fig_per_5_23 = round(fig_per_5_23)
fig_per_5_23_s = 'BS in Business : ' +  str(fig_per_5_23) + "%"

fig_per_5_24 = (len(y_5_24) + len(n_5_24)) * 100 / (len(y_5_24) + len(n_5_24) + len(x_5_24))
fig_per_5_24 = round(fig_per_5_24)
fig_per_5_24_s = 'BE in Electrical Engineering : ' +   str(fig_per_5_24) + "%"

fig_per_5_25 = (len(y_5_25) + len(n_5_25)) * 100 / (len(y_5_25) + len(n_5_25) + len(x_5_25))
fig_per_5_25 = round(fig_per_5_25)
fig_per_5_25_s = 'BA in Social Work : ' +  str(fig_per_5_25) + "%"

fig_per_5_26 = (len(y_5_26) + len(n_5_26)) * 100 / (len(y_5_26) + len(n_5_26) + len(x_5_26))
fig_per_5_26 = round(fig_per_5_26)
fig_per_5_26_s = 'BA in Translation : ' +  str(fig_per_5_26) + "%"

fig_per_5_27 = (len(y_5_27) + len(n_5_27)) * 100 / (len(y_5_27) + len(n_5_27) + len(x_5_27))
fig_per_5_27 = round(fig_per_5_27)
fig_per_5_27_s = 'Bachelor of Architecture : ' +  str(fig_per_5_27) + "%"

fig_per_5_28 = (len(y_5_28) + len(n_5_28)) * 100 / (len(y_5_28) + len(n_5_28) + len(x_5_28))
fig_per_5_28 = round(fig_per_5_28)
fig_per_5_28_s = 'BA in Psychology : ' +  str(fig_per_5_28) + "%"

fig_per_5_29 = (len(y_5_29) + len(n_5_29)) * 100 / (len(y_5_29) + len(n_5_29) + len(x_5_29))
fig_per_5_29 = round(fig_per_5_29)
fig_per_5_29_s = 'BA in Communication Arts : ' +  str(fig_per_5_29) + "%"

fig_per_5_30 = (len(y_5_30) + len(n_5_30)) * 100 / (len(y_5_30) + len(n_5_30) + len(x_5_30))
fig_per_5_30 = round(fig_per_5_30)
fig_per_5_30_s = 'BE in Petroleum Engineering : ' +  str(fig_per_5_30) + "%"

fig_per_5_31 = (len(y_5_31) + len(n_5_31)) * 100 / (len(y_5_31) + len(n_5_31) + len(x_5_31))
fig_per_5_31 = round(fig_per_5_31)
fig_per_5_31_s = 'BE in Computer Engineering : ' +  str(fig_per_5_31) + "%"

fig_per_5_32 = (len(y_5_32) + len(n_5_32)) * 100 / (len(y_5_32) + len(n_5_32) + len(x_5_32))
fig_per_5_32 = round(fig_per_5_32)
fig_per_5_32_s = 'BS in Nursing : ' +  str(fig_per_5_32) + "%"

fig_per_5_33 = (len(y_5_33) + len(n_5_33)) * 100 / (len(y_5_33) + len(n_5_33) + len(x_5_33))
fig_per_5_33 = round(fig_per_5_33)
fig_per_5_33_s = 'BA in Television and Film : ' +  str(fig_per_5_33) + "%"

fig_per_5_34 = (len(y_5_34) + len(n_5_34)) * 100 / (len(y_5_34) + len(n_5_34) + len(x_5_34))
fig_per_5_34 = round(fig_per_5_34)
fig_per_5_34_s = 'BA in Interior Architecture : ' +  str(fig_per_5_34) + "%"

fig_per_5_35 = (len(y_5_35) + len(n_5_35)) * 100 / (len(y_5_35) + len(n_5_35) + len(x_5_35))
fig_per_5_35 = round(fig_per_5_35)
fig_per_5_35_s = 'BA in Political Science : ' +  str(fig_per_5_35) + "%"

fig_per_5_36 = (len(y_5_36) + len(n_5_36)) * 100 / (len(y_5_36) + len(n_5_36) + len(x_5_36))
fig_per_5_36 = round(fig_per_5_36)
fig_per_5_36_s = 'BA in Fine Arts : ' +  str(fig_per_5_36) + "%"

fig_per_5_37 = (len(y_5_33) + len(n_5_37)) * 100 / (len(y_5_37) + len(n_5_37) + len(x_5_37))
fig_per_5_37 = round(fig_per_5_37)
fig_per_5_37_s = 'BE in Mechanical Engineering : ' +  str(fig_per_5_37) + "%"

fig5_perc_int = [fig_per_5_1,fig_per_5_2,fig_per_5_3,fig_per_5_4,fig_per_5_5,fig_per_5_6,fig_per_5_7,fig_per_5_8,fig_per_5_9,fig_per_5_10,fig_per_5_11,fig_per_5_12,fig_per_5_13,fig_per_5_14,fig_per_5_15,fig_per_5_16,fig_per_5_17,fig_per_5_18,fig_per_5_19,fig_per_5_20,fig_per_5_21,fig_per_5_22,fig_per_5_23,fig_per_5_24,fig_per_5_25,fig_per_5_26,fig_per_5_27,fig_per_5_28,fig_per_5_29,fig_per_5_30,fig_per_5_31,fig_per_5_32,fig_per_5_33,fig_per_5_34,fig_per_5_35,fig_per_5_36,fig_per_5_37]

fig5_prog_per = [fig_per_5_1_s,fig_per_5_2_s,fig_per_5_3_s,fig_per_5_4_s,fig_per_5_5_s,fig_per_5_6_s,fig_per_5_7_s,fig_per_5_8_s,fig_per_5_9_s,fig_per_5_10_s,fig_per_5_11_s,fig_per_5_12_s,fig_per_5_13_s,fig_per_5_14_s,fig_per_5_15_s,fig_per_5_16_s,fig_per_5_17_s,fig_per_5_18_s,fig_per_5_19_s,fig_per_5_20_s,fig_per_5_21_s,fig_per_5_22_s,fig_per_5_23_s,fig_per_5_24_s,fig_per_5_25_s,fig_per_5_26_s,fig_per_5_27_s,fig_per_5_28_s,fig_per_5_29_s,fig_per_5_30_s,fig_per_5_31_s,fig_per_5_32_s,fig_per_5_33_s,fig_per_5_34_s,fig_per_5_35_s,fig_per_5_36_s,fig_per_5_37_s]

# remove 0%
for sort_5_i in range(len(fig5_perc_int) - 1, -1, -1):
    if fig5_perc_int[sort_5_i] == 0:
        del fig5_prog_per[sort_5_i]
        del fig5_perc_int[sort_5_i]

fig5_newdf = pd.DataFrame({'Program':fig5_prog_per,'Percentage':fig5_perc_int})
fig5_sort = fig5_newdf.sort_values('Percentage',ascending=True)
fig_8 = fig5_sort.plot.barh(x='Program', y='Percentage')
plt.tight_layout()
plt.savefig('fig5.jpg')

#  Time 2 1st job
# drop rows with values of D/A
# df = df.drop(df.index[df['Q17_How long did it take you to find your first job?_How long did it take you to find your first job?'] == 'D/A'])
# first_job = list(set(df['Q17_How long did it take you to find your first job?_How long did it take you to find your first job?'].to_list()))

#  EMPLOYMENT RATES BY DEGREE PRIOR TO GRADUATION
prog_7 = df['Program'].to_list()
prog_7_filter = list(set(df['Program'].to_list()))
fnd_job = df['Q17_How long did it take you to find your first job?_How long did it take you to find your first job?'].to_list()

prog_7_2 = []
job_stat = []
c = 0
cc = []
for prg in range(0,len(prog_7)):
    # print(prog_7[prg],fnd_job[prg])
    if fnd_job[prg] == 'I found the job before graduating from LAU':
        job_stat.append(fnd_job[prg])
        prog_7_2.append(prog_7[prg])
        c += 1
        cc.append(c)

#  dataframe creation for fig 7
fig_7_df = pd.DataFrame({"sno":cc,'Program_7':prog_7_2,'Job Status':job_stat})

t_prog_c = df['Program'].value_counts()
t_prog_c_1 = list(zip(t_prog_c.index,t_prog_c.values))

t_prog_cc = fig_7_df['Program_7'].value_counts()
t_prog_c_2 = list(zip(t_prog_cc.index,t_prog_cc.values))

t_prog_list = []
for c1 in range(0,len(t_prog_c_1)):
    #print(t_prog_c_1[c1][0],t_prog_c_1[c1][1])
    for c2 in range(0, len(t_prog_c_2)):
        if t_prog_c_1[c1][0] == t_prog_c_2[c2][0]:
            prog_ratio = t_prog_c_2[c2][1] * 100 // t_prog_c_1[c1][1]
            prog_ratio_t = str(prog_ratio) + '%'
            #print(t_prog_c_1[c1][0],t_prog_c_1[c1][1],t_prog_c_2[c2][0],t_prog_c_2[c2][1])
            t_prog_list.append(t_prog_c_1[c1][0] + "|" + prog_ratio_t)

tt_prog_list = []
for t1 in range(0,len(t_prog_list)):
    #print(t_prog_list[t1].split('|')[1])
    for t2 in range(0, len(prog_7_2)):
        if t_prog_list[t1].split('|')[0] == prog_7_2[t2]:
            tt_prog_list.append(prog_7_2[t2] + ":" + t_prog_list[t1].split('|')[1])

#  Adding column with Percentage
fig_7_df['Program'] = tt_prog_list
prog_per_7 = fig_7_df['Program'].to_list()

prog_per_7_n = list(set(prog_per_7))
prog_per_nw = []

for per_i_17 in range(0,len(prog_per_7_n)):
    prog_per_nw.append(int(str(prog_per_7_n[per_i_17]).split(':')[1].strip("%")))

fig_7_dict = dict(zip(list(set(tt_prog_list)),prog_per_nw))
fig7_df_nw = pd.Series(fig_7_dict)
fig7_df_nw = fig7_df_nw.sort_values(ascending=True)
plt.barh(range(len(fig7_df_nw)), fig7_df_nw.values, align='center')
plt.yticks(range(len(prog_per_nw)), fig7_df_nw.index.values, size='small')
plt.tight_layout()
plt.savefig('fig7.jpg')
plt.clf()

#  FIGURE 8 EMPLOYMENT RATES BY DEGREE TWELVE MONTHS AFTER GRADUATION
pd.options.display.float_format = '{:,.0f}'.format
Fig_8_df = pd.read_excel("All results 2017 - 2018.xlsx",sheet_name='1. found job')

fi8_perc = Fig_8_df['%'].to_list()
fi8_js = Fig_8_df['Job seekers'].to_list()

fi8_perc_int = []
fi8_perc_str = []
for val_8 in range(0,len(fi8_perc)):
    fi8_perc_int.append(int(str(fi8_perc[val_8]*100).split(".")[0]))
    fi8_perc_str.append(fi8_js[val_8] + ":" + str(fi8_perc[val_8]*100).split(".")[0] + "%")
    #fi8_perc_int.append(int(fi8_perc[val_8]))

fig8_newdf = pd.DataFrame({'Job seekers':fi8_perc_str,'Percentage':fi8_perc_int})
fig8_sort = fig8_newdf.sort_values('Percentage',ascending=True)
fig_8 = fig8_sort.plot.barh(x='Job seekers', y='Percentage')
plt.tight_layout()
plt.savefig('fig8.jpg')

#  FIGURE 9 METHODS ALUMNI RELIED ON FOR THEIR JOB SEARCH

pd.options.display.float_format = '{:.2f}%'.format
Fig_9_df = pd.read_excel("All results 2017 - 2018.xlsx",sheet_name='means to job')
Fig_9_df.columns = ["Means", "count","Percentage"]
#  Removing last row
Fig_9_df = Fig_9_df[:-1]

fi9_perc = Fig_9_df['Percentage'].to_list()
fi9_js = Fig_9_df['Means'].to_list()

fi9_perc_int = []
fi9_perc_str = []
for val_9 in range(0,len(fi9_perc)):
    fi9_perc_int.append(int(str(fi9_perc[val_9]*100).split(".")[0]))
    fi9_perc_str.append(fi9_js[val_9] + ":" + str(fi9_perc[val_9]*100).split(".")[0] + "%")

fig9_newdf = pd.DataFrame({'Means':fi9_perc_str,'Percentage':fi9_perc_int})
fig9_sort = fig9_newdf.sort_values('Percentage',ascending=True)
fig_9 = fig9_sort.plot.barh(x='Means', y='Percentage')
plt.savefig('fig9.jpg',bbox_inches='tight')
plt.clf()
#  FIGURE 10 ALUMNI WHO RELIED ON LAU JOB SEARCH PLATFORMS AND SERVICES BASED ON DEGREE




#  FIGURE 12 EMPLOYMENT IN JOBS RELATED TO UNDERGRADUATE FIELD OF STUDY BY SEMESTER OF GRADUATION

Fig12_col_1 = df['Graduation_Term'].to_list()
Fig12_col_2 = df['Q19_Was the job related to your undergraduate field of study?_Was the job related to your undergraduate field of study?'].to_list()

Fig12_col_1_nw = []
Fig12_col_2_nw = []
for f_12_v in range(0,len(Fig12_col_1)):
    if Fig12_col_2[f_12_v] == 'Yes':
        Fig12_col_1_nw.append(Fig12_col_1[f_12_v])
        Fig12_col_2_nw.append(Fig12_col_2[f_12_v])

fig12_df = pd.DataFrame({"Graduation_Term":Fig12_col_1_nw,"Answer":Fig12_col_2_nw})


t_pfig12_vc = fig12_df['Graduation_Term'].value_counts()
fig12_vc_dict = dict(zip(t_pfig12_vc.index,t_pfig12_vc.values))

s = sum(t_pfig12_vc.values)
fig12_perc = []
for vc_v in t_pfig12_vc.values:
    fig12_perc.append(str(vc_v*100//s) + "%")
#  Adding % to dict keys by renaming old keys
fig12_vc_dict['Spring 2018 : ' + str(fig12_perc[0])] = fig12_vc_dict.pop('Spring 2018')
fig12_vc_dict['Fall 2017 : ' + str(fig12_perc[1])] = fig12_vc_dict.pop('Fall 2017')
fig12_vc_dict['Summer 2018 : ' + str(fig12_perc[2])] = fig12_vc_dict.pop('Summer 2018')

fig12_df_nw = pd.Series(fig12_vc_dict)
plt.bar(range(len(fig12_df_nw)), fig12_df_nw.values, align='center')
plt.xticks(range(len(fig12_df_nw)), fig12_df_nw.index.values, size='small')
plt.savefig('fig12.jpg')
plt.clf()

#  FIGURE 14 EMPLOYMENT BY JOB LOCATION
#  Dropping values with D/A
df_14 = df[df['Q26_Company location_Company location'] != 'D/A']

fig_14_vc = df_14['Q26_Company location_Company location'].value_counts()
fig_14_vc_l = list(zip(fig_14_vc.index,fig_14_vc.values))

# fig_14_x = []
# fig_14_y = []
# for fig_14_i in range(0,len(fig_14_vc_l)):
#     fig_14_x.append(fig_14_vc_l[fig_14_i][0])
#     fig_14_y.append(fig_14_vc_l[fig_14_i][1])

# fig_14_y_nw = np.array(fig_14_y)
# colors = ['yellowgreen','red','gold','lightskyblue','magenta','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta']
# fig14_percent = 100.*fig_14_y_nw/fig_14_y_nw.sum()
# patches, texts = plt.pie(fig_14_y_nw, colors=colors, startangle=90, radius=1.2)
# labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(fig_14_x, fig14_percent)]
# sort_legend = True
# if sort_legend:
#     patches, labels, dummy =  zip(*sorted(zip(patches, labels, fig_14_y_nw),
#                                           key=lambda x: x[2],
#                                           reverse=True))
# plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.1, 1.),
#            fontsize=8)
# plt.savefig('fig14.jpg', bbox_inches='tight')
# plt.clf()

def pie_chart_with_legend(l,fig):

    l
    x = []
    y = []
    for i in range(0,len(l)):
        x.append(l[i][0])
        y.append(l[i][1])

    y_nw = np.array(y)
    colors = ['yellowgreen','red','gold','lightskyblue','magenta','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta']
    fig_percent = 100.*y_nw/y_nw.sum()
    # rounding of percentages
    for per_i, per in enumerate(range(0,len(fig_percent))):
        s = str(fig_percent[per_i])
        if "0." in s:
            if fig_percent[per_i] >= 0.5:
                fig_percent[per_i] = int(1)
        if not "0." in s:
            fig_percent[per_i] = int(s.split(".")[0])
    patches, texts = plt.pie(y_nw, colors=colors, startangle=90, radius=1.2)
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, fig_percent)]
    labels_nw = []
    for lab_i, lab in enumerate(range(0, len(labels))):
        if "0." in labels[lab_i].split("-")[1]:
            labels_nw.append(labels[lab_i].split("-")[0] + " - " + labels[lab_i].split("-")[1])
        else:
            labels_nw.append(labels[lab_i].split("-")[0] + " - " + labels[lab_i].split("-")[1].split(".")[0] + "%")
    sort_legend = True
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels_nw, y_nw),
                                          key=lambda x: x[2],
                                          reverse=True))
    plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
    plt.savefig(fig + '.jpg', bbox_inches='tight')
    plt.clf()

pie_chart_with_legend(fig_14_vc_l,"fig14")

#  FIGURE 19 EMPLOYMENT BY GOVERNORATE

fig_19_vc = df['Q27_Company region/country_Company region/country'].value_counts()
fig_19_vc_l = list(zip(fig_19_vc.index,fig_19_vc.values))
pie_chart_with_legend(fig_19_vc_l,"fig19")

#  FIGURE 10 ALUMNI WHO RELIED ON LAU JOB SEARCH PLATFORMS AND SERVICES BASED ON DEGREE
df_10 = df[df['Q15_What methods did you rely on while searching for your first job?_What methods did you rely on while searching for your first job?'] != 'D/A']

fig_10_criteria = df_10['Q15_What methods did you rely on while searching for your first job?_What methods did you rely on while searching for your first job?'].to_list()
fig_10_prog = df_10['Program'].to_list()

fig_10_df = pd.DataFrame({"Program":fig_10_prog,"relied on":fig_10_criteria})
fig_10_df.to_excel("10test.xlsx")
fig_10_vc = df_10['Program'].value_counts()
fig_10_vc_pg_dict = dict(zip(fig_10_vc.index,fig_10_vc.values))
s_10 = sum(fig_10_vc.values)

BSB = 0
BEME = 0
BCE = 0
BOB=0
BOA=0
BSIA=0
BSND=0
BAP=0
BN=0
BSM=0
BAPA=0
BPH=0
BAT=0
BSC=0
BSID=0
for fig10_i in range(0,len(fig_10_criteria)):
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BS in Business':BSB += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BE in Mechanical Engineering': BEME += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BE in Civil Engineering': BCE += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BS in Biology': BOB += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'Bachelor of Architecture':BOA += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BA in Interior Architecture': BSIA += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BS in Nutr.&Diet. Coord. Prog.': BSND += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BA in Psychology': BAP += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BS in Nutrition': BN += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BS in Mathematics': BSM += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BA in Political Sc/Int.Affairs': BAPA += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BS in Pharmacy': BPH += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BA in Television and Film': BAT += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BS in Chemistry': BSC += 1
    if "LAU" in fig_10_criteria[fig10_i] and fig_10_prog[fig10_i] == 'BS in Interior Design': BSID += 1

fig_10_vci_l = list(fig_10_vc.index)
fig_10_vcv_l = list(fig_10_vc.values)

#  Adding % to dict keys by renaming old keys
fig_10_vc_pg_dict['BS in Business' + " - " + str(BSB * 100//fig_10_vcv_l[0]) + "%"] = fig_10_vc_pg_dict.pop('BS in Business')
fig_10_vc_pg_dict['BE in Mechanical Engineering' + " - " + str(BEME * 100//fig_10_vcv_l[1]) + "%"] = fig_10_vc_pg_dict.pop('BE in Mechanical Engineering')
fig_10_vc_pg_dict['BE in Civil Engineering' + " - " + str(BCE * 100//fig_10_vcv_l[2]) + "%"] = fig_10_vc_pg_dict.pop('BE in Civil Engineering')
fig_10_vc_pg_dict['BS in Biology' + " - " + str(BOB * 100//fig_10_vcv_l[3]) + "%"] = fig_10_vc_pg_dict.pop('BS in Biology')
fig_10_vc_pg_dict['Bachelor of Architecture' + " - " + str(BOA * 100//fig_10_vcv_l[4]) + "%"] = fig_10_vc_pg_dict.pop('Bachelor of Architecture')
fig_10_vc_pg_dict['BS in Mathematics' + " - " + str(BSM * 100//fig_10_vcv_l[5]) + "%"] = fig_10_vc_pg_dict.pop('BS in Mathematics')
#  fig_10_vc_pg_dict['BA in Psychology' + " - " + str(fig_10_vcv_l[6] * 100//BAP)] = fig_10_vc_pg_dict.pop('BA in Psychology')
fig_10_vc_pg_dict['BA in Interior Architecture' + " - " + str(BSIA * 100//fig_10_vcv_l[7]) + "%"] = fig_10_vc_pg_dict.pop('BA in Interior Architecture')
fig_10_vc_pg_dict['BS in Nutr.&Diet. Coord. Prog.' + " - " + str(BSND * 100//fig_10_vcv_l[8]) + "%"] = fig_10_vc_pg_dict.pop('BS in Nutr.&Diet. Coord. Prog.')
fig_10_vc_pg_dict['BS in Nutrition' + " - " + str(BN * 100//fig_10_vcv_l[9]) + "%"] = fig_10_vc_pg_dict.pop('BS in Nutrition')
fig_10_vc_pg_dict['BS in Pharmacy' + " - " + str(BPH * 100//fig_10_vcv_l[10]) + "%"] = fig_10_vc_pg_dict.pop('BS in Pharmacy')
#  fig_10_vc_pg_dict['BA in Political Sc/Int.Affairs' + " - " + str(fig_10_vcv_l[11] * 100//BAPA)] = fig_10_vc_pg_dict.pop('BA in Political Sc/Int.Affairs')
# fig_10_vc_pg_dict['BA in Television and Film' + " - " + str(fig_10_vcv_l[12] * 100//BAT)] = fig_10_vc_pg_dict.pop('BA in Television and Film')
fig_10_vc_pg_dict['BS in Chemistry' + " - " + str(BSC * 100//fig_10_vcv_l[13]) + "%"] = fig_10_vc_pg_dict.pop('BS in Chemistry')
# fig_10_vc_pg_dict['BS in Interior Design' + " - " + str(fig_10_vcv_l[14] * 100//BSID)] = fig_10_vc_pg_dict.pop('BS in Interior Design')

#  Removing non LAU keys
del fig_10_vc_pg_dict['BA in Psychology']
del fig_10_vc_pg_dict['BA in Political Sc/Int.Affairs']
del fig_10_vc_pg_dict['BA in Television and Film']
del fig_10_vc_pg_dict['BS in Interior Design']

# New dict for fig 10
fig_10_vc_pg_dict_nw = {'BS in Business - 64%': 64, 'BE in Mechanical Engineering - 66%': 66, 'BE in Civil Engineering - 20%': 20, 'BS in Biology - 50%': 50, 'Bachelor of Architecture - 50%': 50, 'BS in Mathematics - 50%': 50, 'BA in Interior Architecture - 100%': 100, 'BS in Nutr.&Diet. Coord. Prog. - 50%': 50, 'BS in Nutrition - 50%': 50, 'BS in Pharmacy - 100%': 100, 'BS in Chemistry - 100%': 100}

fig10_df_nw = pd.Series(fig_10_vc_pg_dict_nw)
fig10_df_nw = fig10_df_nw.sort_values(ascending=True)
plt.barh(range(len(fig10_df_nw)), fig10_df_nw.values, align='center')
plt.yticks(range(len(fig10_df_nw)), fig10_df_nw.index.values, size='small')
plt.tight_layout()
plt.savefig('fig10.jpg')
plt.clf()

# FIGURE 13 EMPLOYMENT IN JOBS RELATED TO UNDERGRADUATE FIELD OF STUDY BY UNDERGRADUATE DEGREE

fig_13_criteria = df['Q19_Was the job related to your undergraduate field of study?_Was the job related to your undergraduate field of study?'].to_list()
fig_13_prog = df['Program'].to_list()
fig_13_prog_filter = list(set(fig_13_prog))

fig_13_d = {}
fig_13_perc = []

TP_y=0
TP_n=0

BAIA_y =0
BAIA_n =0

BATF_y=0
BATF_n=0

DLDG_y=0
DLDG_n=0

BLPS_y=0
BLPS_n=0

BECE_y=0
BECE_n=0

BSB_y=0
BSB_n=0

BEIE_y=0
BEIE_n=0

BAE_y=0
BAE_n=0

BSHT_y=0
BSHT_n=0

BAT_y=0
BAT_n=0

BAEG_y=0
BAEG_n=0

BSND_y=0
BSND_n=0

BAMJ_y=0
BAMJ_n=0

BARCH_y=0
BARCH_n=0

BEPE_y=0
BEPE_n=0

BMATH_y=0
BMATH_n=0

BElEC_y=0
BElEC_n=0

BECOMP_y=0
BECOMP_n=0

BAPSIA_y=0
BAPSIA_n=0

BSNUT_y=0
BSNUT_n=0

BAPAART_y=0
BAPAART_n=0

BEMECH_y=0
BEMECH_n=0

BSPHA_y=0
BSPHA_n=0

BSCHM_y=0
BSCHM_n=0

BSGD_y=0
BSGD_n=0

BSBIO_y=0
BSBIO_n=0

BSBUS_y=0
BSBUS_n=0

BSNUR_y=0
BSNUR_n=0

BCOMM_y=0
BCOMM_n=0

BSIND_y=0
BSIND_n=0

BFAS_y=0
BFAS_n=0

BCOMPS_y=0
BCOMPS_n=0

BSECO_y=0
BSECO_n=0

BASW_y=0
BASW_n=0

BAPSY_y=0
BAPSY_n=0

BIFA_y = 0
BIFA_n = 0
for v_13 in range(0,len(fig_13_prog)):
    if fig_13_prog[v_13] == 'Teaching Diploma' and fig_13_criteria[v_13] == 'Yes':TP_y += 1
    if fig_13_prog[v_13] == 'Teaching Diploma' and fig_13_criteria[v_13] == 'No': TP_n += 1
    if fig_13_prog[v_13] == 'BA in Interior Architecture' and fig_13_criteria[v_13] == 'Yes':BAIA_y += 1
    if fig_13_prog[v_13] == 'BA in Interior Architecture' and fig_13_criteria[v_13] == 'No': BAIA_n += 1
    if fig_13_prog[v_13] == 'BA in Television and Film' and fig_13_criteria[v_13] == 'Yes':BATF_y += 1
    if fig_13_prog[v_13] == 'BA in Television and Film' and fig_13_criteria[v_13] == 'No': BATF_n += 1
    if fig_13_prog[v_13] == 'Dip.in Learn. Dis.& Giftedness' and fig_13_criteria[v_13] == 'Yes':DLDG_y += 1
    if fig_13_prog[v_13] == 'Dip.in Learn. Dis.& Giftedness' and fig_13_criteria[v_13] == 'No': DLDG_n += 1
    if fig_13_prog[v_13] == 'BA in Political Science' and fig_13_criteria[v_13] == 'Yes':BLPS_y += 1
    if fig_13_prog[v_13] == 'BA in Political Science' and fig_13_criteria[v_13] == 'No': BLPS_n += 1
    if fig_13_prog[v_13] == 'BE in Civil Engineering' and fig_13_criteria[v_13] == 'Yes':BECE_y += 1
    if fig_13_prog[v_13] == 'BE in Civil Engineering' and fig_13_criteria[v_13] == 'No': BECE_n += 1
    if fig_13_prog[v_13] == 'BS in Bioinformatics' and fig_13_criteria[v_13] == 'Yes':BSB_y += 1
    if fig_13_prog[v_13] == 'BS in Bioinformatics' and fig_13_criteria[v_13] == 'No': BSB_n += 1
    if fig_13_prog[v_13] == 'BE in Industrial Engineering' and fig_13_criteria[v_13] == 'Yes': BEIE_y += 1
    if fig_13_prog[v_13] == 'BE in Industrial Engineering' and fig_13_criteria[v_13] == 'No': BEIE_n += 1
    if fig_13_prog[v_13] == 'BA in Education' and fig_13_criteria[v_13] == 'Yes': BAE_y += 1
    if fig_13_prog[v_13] == 'BA in Education' and fig_13_criteria[v_13] == 'No': BAE_n += 1
    if fig_13_prog[v_13] == 'BS in Hosp. & Tourism Manag.' and fig_13_criteria[v_13] == 'Yes': BSHT_y += 1
    if fig_13_prog[v_13] == 'BS in Hosp. & Tourism Manag.' and fig_13_criteria[v_13] == 'No': BSHT_n += 1
    if fig_13_prog[v_13] == 'BA in Translation' and fig_13_criteria[v_13] == 'Yes':BAT_y += 1
    if fig_13_prog[v_13] == 'BA in Translation' and fig_13_criteria[v_13] == 'No': BAT_n += 1
    if fig_13_prog[v_13] == 'BA in English' and fig_13_criteria[v_13] == 'Yes':BAEG_y += 1
    if fig_13_prog[v_13] == 'BA in English' and fig_13_criteria[v_13] == 'No': BAEG_n += 1
    if fig_13_prog[v_13] == 'BS in Nutr.&Diet. Coord. Prog.' and fig_13_criteria[v_13] == 'Yes':BSND_y += 1
    if fig_13_prog[v_13] == 'BS in Nutr.&Diet. Coord. Prog.' and fig_13_criteria[v_13] == 'No': BSND_n += 1
    if fig_13_prog[v_13] == 'BA in Multimedia Journalism' and fig_13_criteria[v_13] == 'Yes':BAMJ_y += 1
    if fig_13_prog[v_13] == 'BA in Multimedia Journalism' and fig_13_criteria[v_13] == 'No': BAMJ_n += 1
    if fig_13_prog[v_13] == 'Bachelor of Architecture' and fig_13_criteria[v_13] == 'Yes':BARCH_y += 1
    if fig_13_prog[v_13] == 'Bachelor of Architecture' and fig_13_criteria[v_13] == 'No': BARCH_n += 1
    if fig_13_prog[v_13] == 'BE in Petroleum Engineering' and fig_13_criteria[v_13] == 'Yes':BEPE_y += 1
    if fig_13_prog[v_13] == 'BE in Petroleum Engineering' and fig_13_criteria[v_13] == 'No': BEPE_n += 1
    if fig_13_prog[v_13] == 'BS in Mathematics' and fig_13_criteria[v_13] == 'Yes':BMATH_y += 1
    if fig_13_prog[v_13] == 'BS in Mathematics' and fig_13_criteria[v_13] == 'No': BMATH_n += 1
    if fig_13_prog[v_13] == 'BE in Electrical Engineering' and fig_13_criteria[v_13] == 'Yes':BElEC_y += 1
    if fig_13_prog[v_13] == 'BE in Electrical Engineering' and fig_13_criteria[v_13] == 'No': BElEC_n += 1
    if fig_13_prog[v_13] == 'BE in Computer Engineering' and fig_13_criteria[v_13] == 'Yes':BECOMP_y += 1
    if fig_13_prog[v_13] == 'BE in Computer Engineering' and fig_13_criteria[v_13] == 'No': BECOMP_n += 1
    if fig_13_prog[v_13] == 'BA in Political Sc/Int.Affairs' and fig_13_criteria[v_13] == 'Yes':BAPSIA_y += 1
    if fig_13_prog[v_13] == 'BA in Political Sc/Int.Affairs' and fig_13_criteria[v_13] == 'No': BAPSIA_n += 1
    if fig_13_prog[v_13] == 'BS in Nutrition' and fig_13_criteria[v_13] == 'Yes':BSNUT_y += 1
    if fig_13_prog[v_13] == 'BS in Nutrition' and fig_13_criteria[v_13] == 'No': BSNUT_n += 1
    if fig_13_prog[v_13] == 'BA in Performing Arts' and fig_13_criteria[v_13] == 'Yes':BAPAART_y += 1
    if fig_13_prog[v_13] == 'BA in Performing Arts' and fig_13_criteria[v_13] == 'No': BAPAART_n += 1
    if fig_13_prog[v_13] == 'BE in Mechanical Engineering' and fig_13_criteria[v_13] == 'Yes':BEMECH_y += 1
    if fig_13_prog[v_13] == 'BE in Mechanical Engineering' and fig_13_criteria[v_13] == 'No': BEMECH_n += 1
    if fig_13_prog[v_13] == 'BS in Pharmacy' and fig_13_criteria[v_13] == 'Yes':BSPHA_y += 1
    if fig_13_prog[v_13] == 'BS in Pharmacy' and fig_13_criteria[v_13] == 'No': BSPHA_n += 1
    if fig_13_prog[v_13] == 'BA in Fine Arts' and fig_13_criteria[v_13] == 'Yes':BIFA_y += 1
    if fig_13_prog[v_13] == 'BA in Fine Arts' and fig_13_criteria[v_13] == 'No': BIFA_n += 1
    if fig_13_prog[v_13] == 'BS in Chemistry' and fig_13_criteria[v_13] == 'Yes':BSCHM_y += 1
    if fig_13_prog[v_13] == 'BS in Chemistry' and fig_13_criteria[v_13] == 'No': BSCHM_n += 1
    if fig_13_prog[v_13] == 'BS in Graphic Design' and fig_13_criteria[v_13] == 'Yes':BSGD_y += 1
    if fig_13_prog[v_13] == 'BS in Graphic Design' and fig_13_criteria[v_13] == 'No': BSGD_n += 1
    if fig_13_prog[v_13] == 'BS in Biology' and fig_13_criteria[v_13] == 'Yes':BSBIO_y += 1
    if fig_13_prog[v_13] == 'BS in Biology' and fig_13_criteria[v_13] == 'No': BSBIO_n += 1
    if fig_13_prog[v_13] == 'BS in Business' and fig_13_criteria[v_13] == 'Yes':BSBUS_y += 1
    if fig_13_prog[v_13] == 'BS in Business' and fig_13_criteria[v_13] == 'No': BSBUS_n += 1
    if fig_13_prog[v_13] == 'BS in Nursing' and fig_13_criteria[v_13] == 'Yes':BSNUR_y += 1
    if fig_13_prog[v_13] == 'BS in Nursing' and fig_13_criteria[v_13] == 'No': BSNUR_n += 1
    if fig_13_prog[v_13] == 'BA in Communication Arts' and fig_13_criteria[v_13] == 'Yes':BCOMM_y += 1
    if fig_13_prog[v_13] == 'BA in Communication Arts' and fig_13_criteria[v_13] == 'No': BCOMM_n += 1
    if fig_13_prog[v_13] == 'BS in Interior Design' and fig_13_criteria[v_13] == 'Yes':BSIND_y += 1
    if fig_13_prog[v_13] == 'BS in Interior Design' and fig_13_criteria[v_13] == 'No': BSIND_n += 1
    if fig_13_prog[v_13] == 'BA in Fashion Design' and fig_13_criteria[v_13] == 'Yes':BFAS_y += 1
    if fig_13_prog[v_13] == 'BA in Fashion Design' and fig_13_criteria[v_13] == 'No': BFAS_n += 1
    if fig_13_prog[v_13] == 'BS in Computer Science' and fig_13_criteria[v_13] == 'Yes':BCOMPS_y += 1
    if fig_13_prog[v_13] == 'BS in Computer Science' and fig_13_criteria[v_13] == 'No': BCOMPS_n += 1
    if fig_13_prog[v_13] == 'BS in Economics' and fig_13_criteria[v_13] == 'Yes':BSECO_y += 1
    if fig_13_prog[v_13] == 'BS in Economics' and fig_13_criteria[v_13] == 'No': BSECO_n += 1
    if fig_13_prog[v_13] == 'BA in Social Work' and fig_13_criteria[v_13] == 'Yes':BASW_y += 1
    if fig_13_prog[v_13] == 'BA in Social Work' and fig_13_criteria[v_13] == 'No': BASW_n += 1
    if fig_13_prog[v_13] == 'BA in Psychology' and fig_13_criteria[v_13] == 'Yes':BAPSY_y += 1
    if fig_13_prog[v_13] == 'BA in Psychology' and fig_13_criteria[v_13] == 'No': BAPSY_n += 1
    if fig_13_prog[v_13] == 'BA in Fine Arts' and fig_13_criteria[v_13] == 'Yes':BIFA_y += 1
    if fig_13_prog[v_13] == 'BA in Fine Arts' and fig_13_criteria[v_13] == 'No': BIFA_n += 1

TP_per = TP_y * 100 / (TP_y + TP_n)
if TP_n == 0:
    fig_13_d['Teaching Diploma - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['Teaching Diploma - ' + str(TP_per)[0:2] + "%"] = int(str(TP_per)[0:2])
    fig_13_perc.append(int(str(TP_per)[0:2]))

BAIA_per = BAIA_y * 100 / (BAIA_y + BAIA_n)
if BAIA_n == 0:
    fig_13_d['BA in Interior Architecture - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Interior Architecture - ' + str(BAIA_per)[0:2] + "%"] = int(str(BAIA_per)[0:2])
    fig_13_perc.append(int(str(BAIA_per)[0:2]))

BATF_per = BATF_y * 100 / (BATF_y + BATF_n)
if BATF_n == 0:
    fig_13_d['BA in Television and Film - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Television and Film - ' + str(BATF_per)[0:2] + "%"] = int(str(BATF_per)[0:2])
    fig_13_perc.append(int(str(BATF_per)[0:2]))

DLDG_per = DLDG_y * 100 / (DLDG_y + DLDG_n)
if DLDG_n == 0:
    fig_13_d['Dip.in Learn. Dis.& Giftedness - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['Dip.in Learn. Dis.& Giftedness - ' + str(DLDG_per)[0:2] + "%"] = int(str(DLDG_per)[0:2])
    fig_13_perc.append(int(str(DLDG_per)[0:2]))

# BLPS_per = BLPS_y * 100 / (BLPS_y + BLPS_n)
# fig_13_d['BA in Political Science'] = str(BLPS_per)[0:2] + "%"
# fig_13_perc.append(str(BLPS_per)[0:2])

BECE_per = BECE_y * 100 / (BECE_y + BECE_n)
if BECE_n == 0:
    fig_13_d['BE in Civil Engineering - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BE in Civil Engineering - ' + str(BECE_per)[0:2] + "%"] = int(str(BECE_per)[0:2])
    fig_13_perc.append(int(str(BECE_per)[0:2]))

BSB_per = BSB_y * 100 / (BSB_y + BSB_n)
if BSB_n == 0:
    fig_13_d['BS in Bioinformatics - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Bioinformatics - ' + str(BSB_per)[0:2] + "%"] = 0
    fig_13_perc.append(0)

BEIE_per = BEIE_y * 100 / (BEIE_y + BEIE_n)
if BEIE_n == 0:
    fig_13_d['BE in Industrial Engineering - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BE in Industrial Engineering - ' + str(BEIE_per)[0:2] + "%"] = int(str(BEIE_per)[0:2])
    fig_13_perc.append(int(str(BEIE_per)[0:2]))

BAE_per = BAE_y * 100 / (BAE_y + BAE_n)
if BAE_n == 0:
    fig_13_d['BA in Education - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Education - ' + str(BAE_per)[0:2] + "%"] = int(str(BAE_per)[0:2])
    fig_13_perc.append(int(str(BAE_per)[0:2]))

BSHT_per = BSHT_y * 100 / (BSHT_y + BSHT_n)
if BSHT_n == 0:
    fig_13_d['BS in Hosp. & Tourism Manag. - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Hosp. & Tourism Manag. - ' + str(BSHT_per)[0:2] + "%"] = int(str(BSHT_per)[0:2])
    fig_13_perc.append(int(str(BSHT_per)[0:2]))

BAT_per = BAT_y * 100 / (BAT_y + BAT_n)
if BAT_n == 0:
    fig_13_d['BA in Translation - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Translation - ' + str(BAT_per)[0:2] + "%"] = int(str(BAT_per)[0:2])
    fig_13_perc.append(int(str(BAT_per)[0:2]))

# BAEG_per = BAEG_y * 100 / (BAEG_y + BAEG_n)
# fig_13_d['BA in English'] = str(BAEG_per)[0:2] + "%"
# fig_13_perc.append(str(BAEG_per)[0:2])

BSND_per = BSND_y * 100 / (BSND_y + BSND_n)
if BSND_n == 0:
    fig_13_d['BS in Nutr.&Diet. Coord. Prog. - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Nutr.&Diet. Coord. Prog. - ' + str(BSND_per)[0:2] + "%"] = int(str(BSND_per)[0:2])
    fig_13_perc.append(int(str(BSND_per)[0:2]))

BAMJ_per = BAMJ_y * 100 / (BAMJ_y + BAMJ_n)
if BAMJ_n == 0:
    fig_13_d['BA in Multimedia Journalism - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Multimedia Journalism - ' + str(BAMJ_per)[0:2] + "%"] = int(str(BAMJ_per)[0:2])
    fig_13_perc.append(int(str(BAMJ_per)[0:2]))

BARCH_per = BARCH_y * 100 / (BARCH_y + BARCH_n)
if BARCH_n == 0:
    fig_13_d['Bachelor of Architecture - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['Bachelor of Architecture - ' + str(BARCH_per)[0:2] + "%"] = int(str(BARCH_per)[0:2])
    fig_13_perc.append(int(str(BARCH_per)[0:2]))

BEPE_per = BEPE_y * 100 / (BEPE_y + BEPE_n)
fig_13_d['BE in Petroleum Engineering - ' + str(BEPE_per)[0:2] + "%"] = 0
fig_13_perc.append(0)

BMATH_per = BMATH_y * 100 / (BMATH_y + BMATH_n)
if BMATH_n ==0:
    fig_13_d['BS in Mathematics - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Mathematics - ' + str(BMATH_per)[0:2] + "%"] = int(str(BMATH_per)[0:2])
    fig_13_perc.append(int(str(BMATH_per)[0:2]))

BElEC_per = BElEC_y * 100 / (BElEC_y + BElEC_n)
if BElEC_n == 0:
    fig_13_d['BE in Electrical Engineering - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BE in Electrical Engineering - ' + str(BElEC_per)[0:2] + "%"] = int(str(BElEC_per)[0:2])
fig_13_perc.append(int(str(BElEC_per)[0:2]))

BECOMP_per = BECOMP_y * 100 / (BECOMP_y + BECOMP_n)
if BECOMP_n == 0:
    fig_13_d['BE in Computer Engineering - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BE in Computer Engineering - ' + str(BECOMP_per)[0:2] + "%"] = int(str(BECOMP_per)[0:2])
    fig_13_perc.append(int(str(BECOMP_per)[0:2]))

BAPSIA_per = BAPSIA_y * 100 / (BAPSIA_y + BAPSIA_n)
if BAPSIA_n == 0:
    fig_13_d['BA in Political Sc/Int.Affairs - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Political Sc/Int.Affairs - ' + str(BAPSIA_per)[0:2] + "%"] = int(str(BAPSIA_per)[0:2])
    fig_13_perc.append(int(str(BAPSIA_per)[0:2]))

BSNUT_per = BSNUT_y * 100 / (BSNUT_y + BSNUT_n)
if BSNUT_n == 0:
    fig_13_d['BS in Nutrition - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Nutrition - ' + str(BSNUT_per)[0:2] + "%"] = int(str(BSNUT_per)[0:2])
    fig_13_perc.append(int(str(BSNUT_per)[0:2]))

BAPAART_per = BAPAART_y * 100 / (BAPAART_y + BAPAART_n)
if BAPAART_n == 0:
    fig_13_d['BA in Performing Arts - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Performing Arts - ' + str(BAPAART_per)[0:2] + "%"] = int(str(BAPAART_per)[0:2])
    fig_13_perc.append(int(str(BAPAART_per)[0:2]))

BEMECH_per = BEMECH_y * 100 / (BEMECH_y + BEMECH_n)
if BEMECH_n == 0:
    fig_13_d['BE in Mechanical Engineering - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BE in Mechanical Engineering - ' + str(BEMECH_per)[0:2] + "%"] = int(str(BEMECH_per)[0:2])
    fig_13_perc.append(int(str(BEMECH_per)[0:2]))

BSPHA_per = BSPHA_y * 100 / (BSPHA_y + BSPHA_n)
if BSPHA_n == 0:
    fig_13_d['BS in Pharmacy - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Pharmacy - ' + str(BSPHA_per)[0:2] + "%"] = int(str(BSPHA_per)[0:2])
    fig_13_perc.append(int(str(BSPHA_per)[0:2]))

BSCHM_per = BSCHM_y * 100 / (BSCHM_y + BSCHM_n)
if BSCHM_n == 0:
    fig_13_d['BS in Chemistry - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Chemistry - ' + str(BSCHM_per)[0:2] + "%"] = int(str(BSCHM_per)[0:2])
    fig_13_perc.append(int(str(BSCHM_per)[0:2]))

BSGD_per = BSGD_y * 100 / (BSGD_y + BSGD_n)
if BSGD_n == 0:
    fig_13_d['BS in Graphic Design - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Graphic Design - ' + str(BSGD_per)[0:2] + "%"] = int(str(BSGD_per)[0:2])
    fig_13_perc.append(int(str(BSGD_per)[0:2]))

BSBIO_per = BSBIO_y * 100 / (BSBIO_y + BSBIO_n)
if BSBIO_n == 0:
    fig_13_d['BS in Biology - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Biology - ' + str(BSBIO_per)[0:2] + "%"] = int(str(BSBIO_per)[0:2])
    fig_13_perc.append(int(str(BSBIO_per)[0:2]))

BSBUS_per = BSBUS_y * 100 / (BSBUS_y + BSBUS_n)
if BSBUS_n == 0:
    fig_13_d['BS in Business - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Business - ' + str(BSBUS_per)[0:2] + "%"] = int(str(BSBUS_per)[0:2])
    fig_13_perc.append(int(str(BSBUS_per)[0:2]))

BSNUR_per = BSNUR_y * 100 / (BSNUR_y + BSNUR_n)
if BSNUR_n == 0:
    fig_13_d['BS in Nursing - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Nursing - ' + str(BSNUR_per)[0:2] + "%" ] = int(str(BSNUR_per)[0:2])
    fig_13_perc.append(str(BSNUR_per)[0:2])

BCOMM_per = BSNUR_y * 100 / (BSNUR_y + BSNUR_n)
if BSNUR_n == 0:
    fig_13_d['BA in Communication Arts - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Communication Arts - ' + str(BSNUR_per)[0:2] + "%"] = int(str(BSNUR_per)[0:2])
    fig_13_perc.append(int(str(BSNUR_per)[0:2]))

BSIND_per = BSIND_y * 100 / (BSIND_y + BSIND_n)
if BSIND_n == 0:
    fig_13_d['BS in Interior Design - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Interior Design - ' + str(BSIND_per)[0:2] + "%"] = int(str(BSIND_per)[0:2])
    fig_13_perc.append(int(str(BSIND_per)[0:2]))

BFAS_per = BFAS_y * 100 / (BFAS_y + BFAS_n)
if BFAS_n == 0:
    fig_13_d['BA in Fashion Design - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Fashion Design - ' + str(BFAS_per)[0:2] + "%"] = int(str(BFAS_per)[0:2])
    fig_13_perc.append(int(str(BFAS_per)[0:2]))

BCOMPS_per = BCOMPS_y * 100 / (BCOMPS_y + BCOMPS_n)
if BCOMPS_n == 0:
    fig_13_d['BS in Computer Science - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Computer Science - ' + str(BCOMPS_per)[0:2] + "%"] = int(str(BCOMPS_per)[0:2])
    fig_13_perc.append(int(str(BCOMPS_per)[0:2]))

BSECO_per = BSECO_y * 100 / (BSECO_y + BSECO_n)
if BSECO_n == 0:
    fig_13_d['BS in Economics - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BS in Economics - ' + str(BSECO_per)[0:2] + "%"] = int(str(BSECO_per)[0:2])
    fig_13_perc.append(int(str(BSECO_per)[0:2]))

BASW_per = BASW_y * 100 / (BASW_y + BASW_n)
if BASW_n == 0:
    fig_13_d['BA in Social Work - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Social Work - ' + str(BASW_per)[0:2] + "%"] = int(str(BASW_per)[0:2])
    fig_13_perc.append(int(str(BASW_per)[0:2]))

BAPSY_per = BAPSY_y * 100 / (BAPSY_y + BAPSY_n)
if BAPSY_n == 0:
    fig_13_d['BA in Psychology - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Psychology - ' + str(BAPSY_per)[0:2] + "%"] = int(str(BAPSY_per)[0:2])
    fig_13_perc.append(int(str(BAPSY_per)[0:2]))

BIFA_per = BIFA_y * 100 / (BIFA_y + BIFA_n)
if BIFA_n == 0:
    fig_13_d['BA in Fine Arts - ' + "100%"] = 100
    fig_13_perc.append(100)
else:
    fig_13_d['BA in Fine Arts - ' + str(BIFA_per)[0:2] + "%"] = int(str(BIFA_per)[0:2])
fig_13_perc.append(int(str(BIFA_per)[0:2]))

fig13_df_nw = pd.Series(fig_13_d)
fig13_df_nw = fig13_df_nw.sort_values(ascending=True)
plt.barh(range(len(fig13_df_nw)), fig13_df_nw.values, align='center')
plt.yticks(range(len(fig_13_perc)), fig13_df_nw.index.values, size='small')
plt.tight_layout()
plt.savefig('fig13.jpg')
plt.clf()

#  FIGURE 17 EMPLOYMENT RATES BY SCHOOL AND LOCATION
#  https://stackoverflow.com/questions/50160788/annotate-stacked-barplot-matplotlib-and-pandas

fig_17_sc = df['School'].to_list()
fig_17_loc = df['Q26_Company location_Company location'].to_list()

fig_17_sc_nw = []
fig_17_loc_nw = []
for fig_17_i in range(0,len(fig_17_sc)):
    if fig_17_loc[fig_17_i] != 'D/A':
        fig_17_sc_nw.append(fig_17_sc[fig_17_i])
        fig_17_loc_nw.append(fig_17_loc[fig_17_i])

df_17 = pd.DataFrame({"School":fig_17_sc_nw,"Company location":fig_17_loc_nw,'value': np.random.randint(0, int(1e2),len(fig_17_sc_nw))})
fig_17_sc_l = list(set(fig_17_sc))

# df_17_pct = (df_17.groupby(['School','Company location'])['value'].count()*100/df_17.groupby(['School'])['value'].count())
# ax_17 = df_17_pct.unstack().plot.barh(stacked=True)

counter = df_17.groupby('School')['Company location'].value_counts().unstack()
# #calculate the % for each age group
percentage_dist = 100 * counter.divide(counter.sum(axis = 1), axis = 0)
ax_17 = percentage_dist.plot.bar(stacked=True)

for p_17 in ax_17.patches:
    wid, hei = p_17.get_width(), p_17.get_height()
    x, y = p_17.get_xy()
    ax.text(x+wid/2,
            y+hei/2,
            '{:.0f} %'.format(hei),
            horizontalalignment='center',
            verticalalignment='center')
plt.tight_layout()
plt.savefig('fig17.jpg')
plt.clf()

# FIGURE 18 ALUMNI EMPLOYED ABROAD BY DEGREE
# https://seaborn.pydata.org/tutorial/categorical.html
# https://stackoverflow.com/questions/58977902/bar-plot-and-coloured-categorical-variable

fig_18_pg = df['Program'].to_list()
fig_18_loc = df['Q26_Company location_Company location'].to_list()

fig_18_pg_nw=[]
fig_18_loc_nw=[]
for df_18_i in range(0,len(fig_18_pg)):
    if fig_18_loc[df_18_i] != 'D/A' and fig_18_loc[df_18_i] != 'Lebanon' and fig_18_loc[df_18_i] != 'Other, specify':
        fig_18_pg_nw.append(fig_18_pg[df_18_i])
        fig_18_loc_nw.append(fig_18_loc[df_18_i])

df_18 = pd.DataFrame({"Program":fig_18_pg_nw,"Company location":fig_18_loc_nw,'value': np.random.randint(0, int(1e2),len(fig_18_loc_nw))})
# df_18 = pd.DataFrame({"Program":fig_18_pg_nw,"Company location":fig_18_loc_nw})

# g_18 = df_18.groupby(['Program','Company location']).count()
g_18 = df_18.groupby( [ "Program","Company location"] ).size().to_frame(name = 'count').reset_index()
g_18.to_excel('18_2.xlsx')
df_18_new = pd.read_excel("18_2.xlsx")

# # print(df_18_new[['Company location' == 'Europe']].value_counts())
# print(df_18_new[df_18_new['Company location']  == 'Europe'].)
#
# df_17.groupby(['School'])['value'].count()

df_18_new_pg = df_18_new['Program'].to_list()
df_18_new_loc = df_18_new['Company location'].to_list()
df_18_new_val = df_18_new['count'].to_list()

eu = []
gr = []
af = []
na = []
lev = []
for df_18_new_i in range(0,len(df_18_new)):
    if df_18_new_loc[df_18_new_i] == 'Europe':
        eu.append(df_18_new_val[df_18_new_i])
    if df_18_new_loc[df_18_new_i] == 'Gulf region':
        gr.append(df_18_new_val[df_18_new_i])
    if df_18_new_loc[df_18_new_i] == 'Africa':
        af.append(df_18_new_val[df_18_new_i])
    if df_18_new_loc[df_18_new_i] == 'North America':
        na.append(df_18_new_val[df_18_new_i])
    if df_18_new_loc[df_18_new_i] == 'Levant (Jordan, Syria, Palestine, Iraq)':
        lev.append(df_18_new_val[df_18_new_i])

eu = sum(eu)
gr = sum(gr)
af = sum(af)
na = sum(na)
lev = sum(lev)

prog_18 = []
for df_18_new_i in range(0,len(df_18_new)):
    if df_18_new_loc[df_18_new_i] == 'Europe':
        per_cal = str(df_18_new_val[df_18_new_i] * 100/eu)[0:2]
        prog_18.append(df_18_new_pg[df_18_new_i] + " - " +  per_cal + "%")
    if df_18_new_loc[df_18_new_i] == 'Gulf region':
        per_cal = str(df_18_new_val[df_18_new_i] * 100/gr)[0:2]
        prog_18.append(df_18_new_pg[df_18_new_i] + " - " +  per_cal + "%")
    if df_18_new_loc[df_18_new_i] == 'Africa':
        per_cal = str(df_18_new_val[df_18_new_i] * 100/af)[0:2]
        prog_18.append(df_18_new_pg[df_18_new_i] + " - " +  per_cal + "%")
    if df_18_new_loc[df_18_new_i] == 'North America':
        per_cal = str(df_18_new_val[df_18_new_i] * 100/na)[0:2]
        prog_18.append(df_18_new_pg[df_18_new_i] + " - " +  per_cal + "%")
    if df_18_new_loc[df_18_new_i] == 'Levant (Jordan, Syria, Palestine, Iraq)':
        per_cal = str(df_18_new_val[df_18_new_i] * 100/lev)[0:2]
        prog_18.append(df_18_new_pg[df_18_new_i] + " - " +  per_cal + "%")

prog_18_nw = [sub.replace('.', '') for sub in prog_18]

df_18_calc = pd.DataFrame({"Program":prog_18_nw,"Company Location":df_18_new_loc,"count":df_18_new_val})
df_18_calc.to_excel('18_cal.xlsx')
fig_18 = sns.catplot(x="Program", y="count", hue="Company Location", kind="bar", data=df_18_calc,legend_out=False)
plt.xticks(rotation=90,fontsize=8)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("fig18.jpg")
plt.clf()

# FIGURE 21 EMPLOYMENT BY COMPANY INDUSTRYFIGURE 21 EMPLOYMENT BY COMPANY INDUSTRY

fig_21_ind = df['Q23_Company industry sector_Company industry sector'].to_list()

fig_21_ind_nw=[]
cnt_21 = 0
c_21 = []
for df_21_i in range(0,len(fig_21_ind)):
    if fig_21_ind[df_21_i] != 'D/A' and fig_21_ind[df_21_i] != 'Other, specify':
        fig_21_ind_nw.append(fig_21_ind[df_21_i])
        c_21.append(cnt_21)
        cnt_21 += 1

df_21_tmp = pd.DataFrame({"count":c_21,"Industry":fig_21_ind_nw})
df_21_tmp.to_excel("21.xlsx")
msm_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Marketing, Sales & Services', 'Industry'])
arcc_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Architecture & Construction', 'Industry'])
edt_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Education & Training', 'Industry'])
hsm_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Health Science/Medical', 'Industry'])
sdcp_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Sales & Distribution of Consumer Products', 'Industry'])
hto_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Hospitality & Tourism', 'Industry'])
pha_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Pharmaceuticals', 'Industry'])
stem_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Science, Technology, Engineering & Mathematics', 'Industry'])
afnr_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Agriculture, Food & Natural Resources', 'Industry'])
manf_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Manufacturing', 'Industry'])
bma_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Business, Management & Administration', 'Industry'])
ngo_21 = len(df_21_tmp.loc[df_21_tmp['Industry'] == 'Non-Governmental Organization', 'Industry'])

fig_21_ind_nw_2 = []

for i_21 in range(0,len(fig_21_ind_nw)):
    if fig_21_ind_nw[i_21] == 'Marketing, Sales & Services':
        msm_21_per = msm_21 * 100/len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(msm_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Architecture & Construction':
        arcc_21_per = arcc_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(arcc_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Education & Training':
        edt_21_per = edt_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(edt_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Health Science/Medical':
        hsm_21_per = hsm_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(hsm_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Sales & Distribution of Consumer Products':
        sdcp_21_per = sdcp_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(sdcp_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Hospitality & Tourism':
        hto_21_per = hto_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(hto_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Pharmaceuticals':
        pha_21_per = pha_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(pha_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Science, Technology, Engineering & Mathematics':
        stem_21_per = stem_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(stem_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Agriculture, Food & Natural Resources':
        afnr_21_per = afnr_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(afnr_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Manufacturing':
        manf_21_per = manf_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(manf_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Business, Management & Administration':
        bma_21_per = bma_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(bma_21_per).split(".")[0] + '%')

    if fig_21_ind_nw[i_21] == 'Non-Governmental Organization':
        ngo_21_per = ngo_21 * 100 / len(df_21_tmp)
        fig_21_ind_nw_2.append(fig_21_ind_nw[i_21] + " : " + str(ngo_21_per).split(".")[0] + '%')


#  remove duplicates
fig_21_ind_nw_2 = list(set(list(fig_21_ind_nw_2)))

fig_21_per = []
for per_vi in range(0,len(fig_21_ind_nw_2)):
    fig_21_per.append(int(fig_21_ind_nw_2[per_vi].split(":")[1].strip('%')))
fig21_newdf = pd.DataFrame({'Company industry sector':fig_21_ind_nw_2,'Percentage':fig_21_per})
fig21_sort = fig21_newdf.sort_values('Percentage',ascending=True)
fig_21 = fig21_sort.plot.barh(x='Company industry sector', y='Percentage')
plt.savefig('fig21.jpg',bbox_inches='tight')
plt.clf()


# FIGURE 22 AVERAGE STARTING BASIC SALARY BY GENDER

fig_22_sal = df['Q21_What was your starting basic salary?_What was your starting basic salary?'].to_list()
fig_22_gen= df['Gender'].to_list()

fig_22_sal_1 = []
fig_22_gen_1 = []
for df_22_i in range(0,len(fig_22_sal)):
    if fig_22_sal[df_22_i] != 'D/A':
        fig_22_sal_1.append(fig_22_sal[df_22_i])
        fig_22_gen_1.append(fig_22_gen[df_22_i])

# salary avg calculation
sal_avgf_1 = []
sal_avgf_2 = []
sal_avgf_3 = []
sal_avgf_4 = []
sal_avgf_5 = []
sal_avgf_6 = []
sal_avgf_7 = []
f_1 = 0
f_2 = 0
f_3 = 0
f_4 = 0
f_5 = 0
f_6 = 0
f_7 = 0

m_1 = 0
m_2 = 0
m_3 = 0
m_4 = 0
m_5 = 0
m_6 = 0
m_7 = 0
sal_avgm_1 = []
sal_avgm_2 = []
sal_avgm_3 = []
sal_avgm_4 = []
sal_avgm_5 = []
sal_avgm_6 = []
sal_avgm_7 = []

for sal_i in range(0,len(fig_22_sal_1)):
    if fig_22_sal_1[sal_i] == '$1,001-$1,200' and fig_22_gen_1[sal_i] =='Female':
        sal_avgf_1.append(1100)
        f_1 += 1
    if fig_22_sal_1[sal_i] == '$1,001-$1,200' and fig_22_gen_1[sal_i] == 'Male':
        sal_avgm_1.append(1100)
        m_1 += 1

    if fig_22_sal_1[sal_i] == '$1,201-$1,500' and fig_22_gen_1[sal_i] =='Female':
        sal_avgf_2.append(1350)
        f_2 += 1
    if fig_22_sal_1[sal_i] == '$1,201-$1,500' and fig_22_gen_1[sal_i] == 'Male':
        sal_avgm_2.append(1350)
        m_2 += 1

    if fig_22_sal_1[sal_i] == '$1,501-$2,000'and fig_22_gen_1[sal_i] =='Female':
        sal_avgf_3.append(1750)
        f_3 += 1
    if fig_22_sal_1[sal_i] == '$1,501-$2,000' and fig_22_gen_1[sal_i] == 'Male':
        sal_avgm_3.append(1750)
        m_3 += 1

    if fig_22_sal_1[sal_i] == '$2,001-$3,000' and fig_22_gen_1[sal_i] =='Female':
        sal_avgf_4.append(2500)
        f_4 += 1
    if fig_22_sal_1[sal_i] == '$2,001-$3,000' and fig_22_gen_1[sal_i] == 'Male':
        sal_avgm_4.append(2500)
        m_4 += 1

    if fig_22_sal_1[sal_i] == 'Above $3,000' and fig_22_gen_1[sal_i] =='Female':
        sal_avgf_5.append(3000)
        f_5 += 1
    if fig_22_sal_1[sal_i] == 'Above $3,000' and fig_22_gen_1[sal_i] == 'Male':
        sal_avgm_5.append(3000)
        m_5 += 1

    if fig_22_sal_1[sal_i] == 'Below $700' and fig_22_gen_1[sal_i] =='Female':
        sal_avgf_6.append(700)
        f_6 += 1
    if fig_22_sal_1[sal_i] == 'Below $700' and fig_22_gen_1[sal_i] == 'Male':
        sal_avgm_6.append(700)
        m_6 += 1

    if fig_22_sal_1[sal_i] == '$700-$1,000' and fig_22_gen_1[sal_i] =='Female':
        sal_avgf_7.append(850)
        f_7 += 1
    if fig_22_sal_1[sal_i] == '$700-$1,000' and fig_22_gen_1[sal_i] == 'Male':
        sal_avgm_7.append(850)
        m_7 += 1

total_female_salary = sal_avgf_1[0] * f_1 + sal_avgf_2[0] * f_2 + sal_avgf_3[0] * f_3 + sal_avgf_4[0] * f_4 + sal_avgf_5[0] * f_5 + sal_avgf_6[0] * f_6 + sal_avgf_7[0] * f_7
total_females = sum([f_1,f_2,f_3,f_4,f_5,f_6,f_7])
female_avg = total_female_salary/total_females
female_avg_s = "Female : $" + str(female_avg).split(".")[0]
female_avg_int = int(str(female_avg).split(".")[0])

total_male_salary = sal_avgm_1[0] * m_1 + sal_avgm_2[0] * m_2 + sal_avgm_3[0] * m_3 + sal_avgm_4[0] * m_4 + sal_avgm_5[0] * m_5 + sal_avgm_6[0] * m_6 + sal_avgm_7[0] * m_7
total_males = sum([m_1,m_2,m_3,m_4,m_5,m_6,m_7])
male_avg = total_male_salary/total_males
male_avg_s = "Male : $" + str(male_avg).split(".")[0]
male_avg_int = int(str(male_avg).split(".")[0])

# print(m_1,m_2,m_3,m_4,m_5,m_6,m_7)
# print(sal_avgm_1[0] ,sal_avgm_2[0], sal_avgm_3[0] , sal_avgm_4[0] , sal_avgm_5[0] , sal_avgm_6[0] , sal_avgm_7[0])

df_22_avg = pd.DataFrame({"Gender":[female_avg_s,male_avg_s],"Salary by Gender":[female_avg_int,male_avg_int]})
fig_22_ax = sns.catplot(x="Gender", y="Salary by Gender", kind="bar", data=df_22_avg)
plt.savefig('fig22.jpg')
plt.clf()

# FIGURE 24 AVERAGE STARTING BASIC SALARY BY REGION

df_24_loc = df['Q26_Company location_Company location'].to_list()
df_24_sal = df['Q21_What was your starting basic salary?_What was your starting basic salary?'].to_list()

fig_24_sal_1 = []
fig_24_loc_1 = []
for df_24_i in range(0,len(df_24_sal)):
    if df_24_sal[df_24_i] != 'D/A':
        fig_24_sal_1.append(df_24_sal[df_24_i])
        fig_24_loc_1.append(df_24_loc[df_24_i])

df_24tmp = pd.DataFrame({"sal":fig_24_sal_1,"loc":fig_24_loc_1})
#df_24tmp.to_excel('24.xlsx')

#  for Africa
reg_1_1 = []
reg_1_2 = []
reg_1_3 = []
reg_1_4 = []
reg_1_5 = []
reg_1_6 = []
reg_1_7 = []

#  for Europe
reg_2_1 = []
reg_2_2 = []
reg_2_3 = []
reg_2_4 = []
reg_2_5 = []
reg_2_6 = []
reg_2_7 = []

#  for Other, specify
reg_3_1 = []
reg_3_2 = []
reg_3_3 = []
reg_3_4 = []
reg_3_5 = []
reg_3_6 = []
reg_3_7 = []

#  North America
reg_4_1 = []
reg_4_2 = []
reg_4_3 = []
reg_4_4 = []
reg_4_5 = []
reg_4_6 = []
reg_4_7 = []

#  Gulf region
reg_5_1 = []
reg_5_2 = []
reg_5_3 = []
reg_5_4 = []
reg_5_5 = []
reg_5_6 = []
reg_5_7 = []

#  Lebanon
reg_6_1 = []
reg_6_2 = []
reg_6_3 = []
reg_6_4 = []
reg_6_5 = []
reg_6_6 = []
reg_6_7 = []

#  Levant (Jordan, Syria, Palestine, Iraq)
reg_7_1 = []
reg_7_2 = []
reg_7_3 = []
reg_7_4 = []
reg_7_5 = []
reg_7_6 = []
reg_7_7 = []


def cal_sal_24(sal_l,loc_l,location,salrng,salavg,list_sal):

    for ind_rng in range(0,len(sal_l)):
        if sal_l[ind_rng] == salrng and loc_l[ind_rng] == location:
            list_sal.append(salavg)

cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Africa",'$1,001-$1,200',1100,reg_1_1)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Africa",'$1,201-$1,500',1350,reg_1_2)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Africa",'$1,501-$2,000',1750,reg_1_3)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Africa",'$2,001-$3,000',2500,reg_1_4)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Africa",'$700-$1,000',850,reg_1_5)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Africa",'Above $3,000',3000,reg_1_6)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Africa",'Below $700',700,reg_1_7)

cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Europe",'$1,001-$1,200',1100,reg_2_1)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Europe",'$1,201-$1,500',1350,reg_2_2)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Europe",'$1,501-$2,000',1750,reg_2_3)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Europe",'$2,001-$3,000',2500,reg_2_4)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Europe",'$700-$1,000',850,reg_2_5)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Europe",'Above $3,000',3000,reg_2_6)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Europe",'Below $700',700,reg_2_7)

cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Other, specify",'$1,001-$1,200',1100,reg_3_1)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Other, specify",'$1,201-$1,500',1350,reg_3_2)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Other, specify",'$1,501-$2,000',1750,reg_3_3)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Other, specify",'$2,001-$3,000',2500,reg_3_4)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Other, specify",'$700-$1,000',850,reg_3_5)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Other, specify",'Above $3,000',3000,reg_3_6)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Other, specify",'Below $700',700,reg_3_7)

cal_sal_24(fig_24_sal_1,fig_24_loc_1,"North America",'$1,001-$1,200',1100,reg_4_1)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"North America",'$1,201-$1,500',1350,reg_4_2)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"North America",'$1,501-$2,000',1750,reg_4_3)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"North America",'$2,001-$3,000',2500,reg_4_4)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"North America",'$700-$1,000',850,reg_4_5)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"North America",'Above $3,000',3000,reg_4_6)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"North America",'Below $700',700,reg_4_7)

cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Gulf region",'$1,001-$1,200',1100,reg_5_1)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Gulf region",'$1,201-$1,500',1350,reg_5_2)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Gulf region",'$1,501-$2,000',1750,reg_5_3)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Gulf region",'$2,001-$3,000',2500,reg_5_4)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Gulf region",'$700-$1,000',850,reg_5_5)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Gulf region",'Above $3,000',3000,reg_5_6)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Gulf region",'Below $700',700,reg_5_7)

cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Lebanon",'$1,001-$1,200',1100,reg_6_1)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Lebanon",'$1,201-$1,500',1350,reg_6_2)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Lebanon",'$1,501-$2,000',1750,reg_6_3)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Lebanon",'$2,001-$3,000',2500,reg_6_4)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Lebanon",'$700-$1,000',850,reg_6_5)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Lebanon",'Above $3,000',3000,reg_6_6)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Lebanon",'Below $700',700,reg_6_7)

cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Levant (Jordan, Syria, Palestine, Iraq)",'$1,001-$1,200',1100,reg_7_1)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Levant (Jordan, Syria, Palestine, Iraq)",'$1,201-$1,500',1300,reg_7_2)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Levant (Jordan, Syria, Palestine, Iraq)",'$1,501-$2,000',1750,reg_7_3)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Levant (Jordan, Syria, Palestine, Iraq)",'$2,001-$3,000',2500,reg_7_4)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Levant (Jordan, Syria, Palestine, Iraq)",'$700-$1,000',850,reg_7_5)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Levant (Jordan, Syria, Palestine, Iraq)",'Above $3,000',3000,reg_7_6)
cal_sal_24(fig_24_sal_1,fig_24_loc_1,"Levant (Jordan, Syria, Palestine, Iraq)",'Below $700',700,reg_7_7)

avg_africa = 1100 * len(reg_1_1) + 1300 * len(reg_1_2) + 1750 * len(reg_1_3) + 2500 * len(reg_1_4) + 850 * len(reg_1_5) + 3000 * len(reg_1_6) + 700 * len(reg_1_7)
total_africa = len(reg_1_1) + len(reg_1_2) + len(reg_1_3) + len(reg_1_4) + len(reg_1_5) +  len(reg_1_6) +  len(reg_1_7)
avg_africa = avg_africa / total_africa
avg_africa = int(str(avg_africa).split(".")[0])
avg_africa_s = "Africa : $" + str(avg_africa).split(".")[0]

avg_europe = 1100 * len(reg_2_1) + 1300 * len(reg_2_2) + 1750 * len(reg_2_3) + 2500 * len(reg_2_4) + 850 * len(reg_2_5) + 3000 * len(reg_2_6) + 700 * len(reg_2_7)
total_europe = len(reg_2_1) + len(reg_2_2) + len(reg_2_3) + len(reg_2_4) + len(reg_2_5) +  len(reg_2_6) +  len(reg_2_7)
avg_europe = avg_europe / total_europe
avg_europe = int(str(avg_europe).split(".")[0])
avg_europe_s = "Europe : $" + str(avg_europe).split(".")[0]

avg_Other = 1100 * len(reg_3_1) + 1300 * len(reg_3_2) + 1750 * len(reg_3_3) + 2500 * len(reg_3_4) + 850 * len(reg_3_5) + 3000 * len(reg_3_6) + 700 * len(reg_3_7)
total_Other = len(reg_3_1) + len(reg_3_2) + len(reg_3_3) + len(reg_3_4) + len(reg_3_5) +  len(reg_3_6) +  len(reg_3_7)
avg_Other = avg_Other / total_Other
avg_Other = int(str(avg_Other).split(".")[0])
avg_Other_s = "Other, specify : $" + str(avg_Other).split(".")[0]

avg_NAmerica = 1100 * len(reg_4_1) + 1300 * len(reg_4_2) + 1750 * len(reg_4_3) + 2500 * len(reg_4_4) + 850 * len(reg_4_5) + 3000 * len(reg_4_6) + 700 * len(reg_4_7)
total_Other = len(reg_4_1) + len(reg_4_2) + len(reg_4_3) + len(reg_4_4) + len(reg_4_5) +  len(reg_4_6) +  len(reg_4_7)
avg_NAmerica = avg_NAmerica / total_Other
avg_NAmerica = int(str(avg_NAmerica).split(".")[0])
avg_NAmerica_s = "North America : $" + str(avg_NAmerica).split(".")[0]

avg_Gulf = 1100 * len(reg_5_1) + 1300 * len(reg_5_2) + 1750 * len(reg_5_3) + 2500 * len(reg_5_4) + 850 * len(reg_5_5) + 3000 * len(reg_5_6) + 700 * len(reg_5_7)
total_Other = len(reg_5_1) + len(reg_5_2) + len(reg_5_3) + len(reg_5_4) + len(reg_5_5) +  len(reg_5_6) +  len(reg_5_7)
avg_Gulf = avg_Gulf / total_Other
avg_Gulf = int(str(avg_Gulf).split(".")[0])
avg_Gulf_s = "Gulf region : $" + str(avg_Gulf).split(".")[0]

avg_Lebanon = 1100 * len(reg_6_1) + 1300 * len(reg_6_2) + 1750 * len(reg_6_3) + 2500 * len(reg_6_4) + 850 * len(reg_6_5) + 3000 * len(reg_6_6) + 700 * len(reg_6_7)
total_Other = len(reg_6_1) + len(reg_6_2) + len(reg_6_3) + len(reg_6_4) + len(reg_6_5) +  len(reg_6_6) +  len(reg_6_7)
avg_Lebanon = avg_Lebanon / total_Other
avg_Lebanon = int(str(avg_Lebanon).split(".")[0])
avg_Lebanon_s = "Lebanon : $" + str(avg_Lebanon).split(".")[0]

avg_Levant = 1100 * len(reg_7_1) + 1300 * len(reg_7_2) + 1750 * len(reg_7_3) + 2500 * len(reg_7_4) + 850 * len(reg_7_5) + 3000 * len(reg_7_6) + 700 * len(reg_7_7)
total_Other = len(reg_7_1) + len(reg_7_2) + len(reg_7_3) + len(reg_7_4) + len(reg_7_5) +  len(reg_7_6) +  len(reg_7_7)
avg_Levant = avg_Levant / total_Other
avg_Levant = int(str(avg_Levant).split(".")[0])
avg_Levant_s = "Levant (Jordan, Syria, Palestine, Iraq) : $" + str(avg_Levant).split(".")[0]

df_24_avg = pd.DataFrame({"Region":[avg_africa_s,avg_europe_s,avg_Gulf_s,avg_NAmerica_s,avg_Lebanon_s,avg_Other_s,avg_Levant_s],"AVERAGE SALARY BY REGION":[avg_africa,avg_europe,avg_Gulf,avg_NAmerica,avg_Lebanon,avg_Other,avg_Levant]})
fig_24_ax = sns.catplot(x="Region", y="AVERAGE SALARY BY REGION", kind="bar", data=df_24_avg)
plt.xticks(rotation=90,fontsize=10)
plt.tight_layout()
plt.savefig('fig24.jpg')
plt.clf()

# FIGURE 25 AVERAGE STARTING BASIC SALARY BY DEGREE

df_25_prog = df['Program'].to_list()
df_25_sal = df['Q21_What was your starting basic salary?_What was your starting basic salary?'].to_list()

fig_25_prog_1 = []
fig_25_sal_1 = []
for fig_25_i in range(0, len(df_25_sal)):
    if df_25_sal[fig_25_i] != 'D/A':
        fig_25_sal_1.append(df_25_sal[fig_25_i])
        fig_25_prog_1.append(df_25_prog[fig_25_i])

df_25tmp = pd.DataFrame({"Program":fig_25_prog_1,"Salary":fig_25_sal_1})
# df_25tmp.to_excel('25.xlsx')

#  ['BE in Electrical Engineering', 'BS in Hosp. & Tourism Manag.', 'BS in Graphic Design', 'BS in Bioinformatics', 'BA in Psychology', 'BA in Political Sc/Int.Affairs', 'Teaching Diploma', 'Bachelor of Architecture', 'BS in Biology', 'BA in Education', 'BS in Nutrition', 'BS in Economics', 'BE in Computer Engineering', 'BA in Multimedia Journalism', 'BS in Business', 'BS in Chemistry', 'BS in Computer Science', 'BE in Civil Engineering', 'BS in Nursing', 'BA in Interior Architecture', 'BA in Fine Arts', 'BA in Fashion Design', 'BS in Mathematics', 'BS in Interior Design', 'BA in Translation', 'BA in Performing Arts', 'BA in Social Work', 'BA in Communication Arts', 'BE in Petroleum Engineering', 'BE in Mechanical Engineering', 'BA in Television and Film', 'BS in Nutr.&Diet. Coord. Prog.', 'BS in Pharmacy', 'Dip.in Learn. Dis.& Giftedness', 'BE in Industrial Engineering']

prog_1_1 = []
prog_1_2 = []
prog_1_3 = []
prog_1_4 = []
prog_1_5 = []
prog_1_6 = []
prog_1_7 = []

prog_2_1 = []
prog_2_2 = []
prog_2_3 = []
prog_2_4 = []
prog_2_5 = []
prog_2_6 = []
prog_2_7 = []

prog_3_1 = []
prog_3_2 = []
prog_3_3 = []
prog_3_4 = []
prog_3_5 = []
prog_3_6 = []
prog_3_7 = []

prog_4_1 = []
prog_4_2 = []
prog_4_3 = []
prog_4_4 = []
prog_4_5 = []
prog_4_6 = []
prog_4_7 = []

prog_5_1 = []
prog_5_2 = []
prog_5_3 = []
prog_5_4 = []
prog_5_5 = []
prog_5_6 = []
prog_5_7 = []

prog_6_1 = []
prog_6_2 = []
prog_6_3 = []
prog_6_4 = []
prog_6_5 = []
prog_6_6 = []
prog_6_7 = []

prog_7_1 = []
prog_7_2 = []
prog_7_3 = []
prog_7_4 = []
prog_7_5 = []
prog_7_6 = []
prog_7_7 = []

prog_8_1 = []
prog_8_2 = []
prog_8_3 = []
prog_8_4 = []
prog_8_5 = []
prog_8_6 = []
prog_8_7 = []

prog_9_1 = []
prog_9_2 = []
prog_9_3 = []
prog_9_4 = []
prog_9_5 = []
prog_9_6 = []
prog_9_7 = []

prog_10_1 = []
prog_10_2 = []
prog_10_3 = []
prog_10_4 = []
prog_10_5 = []
prog_10_6 = []
prog_10_7 = []

prog_11_1 = []
prog_11_2 = []
prog_11_3 = []
prog_11_4 = []
prog_11_5 = []
prog_11_6 = []
prog_11_7 = []

prog_12_1 = []
prog_12_2 = []
prog_12_3 = []
prog_12_4 = []
prog_12_5 = []
prog_12_6 = []
prog_12_7 = []

prog_13_1 = []
prog_13_2 = []
prog_13_3 = []
prog_13_4 = []
prog_13_5 = []
prog_13_6 = []
prog_13_7 = []

prog_14_1 = []
prog_14_2 = []
prog_14_3 = []
prog_14_4 = []
prog_14_5 = []
prog_14_6 = []
prog_14_7 = []

prog_15_1 = []
prog_15_2 = []
prog_15_3 = []
prog_15_4 = []
prog_15_5 = []
prog_15_6 = []
prog_15_7 = []

prog_16_1 = []
prog_16_2 = []
prog_16_3 = []
prog_16_4 = []
prog_16_5 = []
prog_16_6 = []
prog_16_7 = []

prog_17_1 = []
prog_17_2 = []
prog_17_3 = []
prog_17_4 = []
prog_17_5 = []
prog_17_6 = []
prog_17_7 = []

prog_18_1 = []
prog_18_2 = []
prog_18_3 = []
prog_18_4 = []
prog_18_5 = []
prog_18_6 = []
prog_18_7 = []

prog_19_1 = []
prog_19_2 = []
prog_19_3 = []
prog_19_4 = []
prog_19_5 = []
prog_19_6 = []
prog_19_7 = []

prog_20_1 = []
prog_20_2 = []
prog_20_3 = []
prog_20_4 = []
prog_20_5 = []
prog_20_6 = []
prog_20_7 = []

prog_21_1 = []
prog_21_2 = []
prog_21_3 = []
prog_21_4 = []
prog_21_5 = []
prog_21_6 = []
prog_21_7 = []

prog_22_1 = []
prog_22_2 = []
prog_22_3 = []
prog_22_4 = []
prog_22_5 = []
prog_22_6 = []
prog_22_7 = []

prog_23_1 = []
prog_23_2 = []
prog_23_3 = []
prog_23_4 = []
prog_23_5 = []
prog_23_6 = []
prog_23_7 = []

prog_24_1 = []
prog_24_2 = []
prog_24_3 = []
prog_24_4 = []
prog_24_5 = []
prog_24_6 = []
prog_24_7 = []

prog_25_1 = []
prog_25_2 = []
prog_25_3 = []
prog_25_4 = []
prog_25_5 = []
prog_25_6 = []
prog_25_7 = []

prog_26_1 = []
prog_26_2 = []
prog_26_3 = []
prog_26_4 = []
prog_26_5 = []
prog_26_6 = []
prog_26_7 = []

prog_27_1 = []
prog_27_2 = []
prog_27_3 = []
prog_27_4 = []
prog_27_5 = []
prog_27_6 = []
prog_27_7 = []

prog_28_1 = []
prog_28_2 = []
prog_28_3 = []
prog_28_4 = []
prog_28_5 = []
prog_28_6 = []
prog_28_7 = []

prog_29_1 = []
prog_29_2 = []
prog_29_3 = []
prog_29_4 = []
prog_29_5 = []
prog_29_6 = []
prog_29_7 = []

prog_30_1 = []
prog_30_2 = []
prog_30_3 = []
prog_30_4 = []
prog_30_5 = []
prog_30_6 = []
prog_30_7 = []

prog_31_1 = []
prog_31_2 = []
prog_31_3 = []
prog_31_4 = []
prog_31_5 = []
prog_31_6 = []
prog_31_7 = []

prog_32_1 = []
prog_32_2 = []
prog_32_3 = []
prog_32_4 = []
prog_32_5 = []
prog_32_6 = []
prog_32_7 = []

prog_33_1 = []
prog_33_2 = []
prog_33_3 = []
prog_33_4 = []
prog_33_5 = []
prog_33_6 = []
prog_33_7 = []

prog_34_1 = []
prog_34_2 = []
prog_34_3 = []
prog_34_4 = []
prog_34_5 = []
prog_34_6 = []
prog_34_7 = []

prog_35_1 = []
prog_35_2 = []
prog_35_3 = []
prog_35_4 = []
prog_35_5 = []
prog_35_6 = []
prog_35_7 = []

# Note will use same function we created for 24 so need get confused only the parameters changes:

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Communication Arts",'$1,001-$1,200',1100,prog_1_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Communication Arts",'$1,201-$1,500',1350,prog_1_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Communication Arts",'$1,501-$2,000',1750,prog_1_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Communication Arts",'$2,001-$3,000',2500,prog_1_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Communication Arts",'$700-$1,000',850,prog_1_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Communication Arts",'Above $3,000',3000,prog_1_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Communication Arts",'Below $700',700,prog_1_7)

avg_pg_1 = 1100 * len(prog_1_1) + 1300 * len(prog_1_2) + 1750 * len(prog_1_3) + 2500 * len(prog_1_4) + 850 * len(prog_1_5) + 3000 * len(prog_1_6) + 700 * len(prog_1_7)
total_pg_1 = len(prog_1_1) + len(prog_1_2) + len(prog_1_3) + len(prog_1_4) + len(prog_1_5) +  len(prog_1_6) +  len(prog_1_7)
avg_pg_1 = avg_pg_1 / total_pg_1
avg_pg_1 = int(str(avg_pg_1).split(".")[0])
avg_pg_1_s = "BA in Communication Arts : $" + str(avg_pg_1).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Electrical Engineering",'$1,001-$1,200',1100,prog_2_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Electrical Engineering",'$1,201-$1,500',1350,prog_2_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Electrical Engineering",'$1,501-$2,000',1750,prog_2_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Electrical Engineering",'$2,001-$3,000',2500,prog_2_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Electrical Engineering",'$700-$1,000',850,prog_2_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Electrical Engineering",'Above $3,000',3000,prog_2_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Electrical Engineering",'Below $700',700,prog_2_7)

avg_pg_2 = 1100 * len(prog_2_1) + 1300 * len(prog_2_2) + 1750 * len(prog_2_3) + 2500 * len(prog_2_4) + 850 * len(prog_2_5) + 3000 * len(prog_2_6) + 700 * len(prog_2_7)
total_pg_2 = len(prog_2_1) + len(prog_2_2) + len(prog_2_3) + len(prog_2_4) + len(prog_2_5) +  len(prog_2_6) +  len(prog_2_7)
avg_pg_2 = avg_pg_2 / total_pg_2
avg_pg_2 = int(str(avg_pg_2).split(".")[0])
avg_pg_2_s = "BE in Electrical Engineering : $" + str(avg_pg_2).split(".")[0]


cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Hosp. & Tourism Manag.",'$1,001-$1,200',1100,prog_3_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Hosp. & Tourism Manag.",'$1,201-$1,500',1350,prog_3_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Hosp. & Tourism Manag.",'$1,501-$2,000',1750,prog_3_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Hosp. & Tourism Manag.",'$2,001-$3,000',2500,prog_3_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Hosp. & Tourism Manag.",'$700-$1,000',850,prog_3_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Hosp. & Tourism Manag.",'Above $3,000',3000,prog_3_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Hosp. & Tourism Manag.",'Below $700',700,prog_3_7)

avg_pg_3 = 1100 * len(prog_3_1) + 1300 * len(prog_3_2) + 1750 * len(prog_3_3) + 2500 * len(prog_3_4) + 850 * len(prog_3_5) + 3000 * len(prog_3_6) + 700 * len(prog_3_7)
total_pg_3 = len(prog_3_1) + len(prog_3_2) + len(prog_3_3) + len(prog_3_4) + len(prog_3_5) +  len(prog_3_6) +  len(prog_3_7)
avg_pg_3 = avg_pg_3 / total_pg_3
avg_pg_3 = int(str(avg_pg_3).split(".")[0])
avg_pg_3_s = "BS in Hosp. & Tourism Manag. : $" + str(avg_pg_3).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Graphic Design",'$1,001-$1,200',1100,prog_4_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Graphic Design",'$1,201-$1,500',1350,prog_4_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Graphic Design",'$1,501-$2,000',1750,prog_4_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Graphic Design",'$2,001-$3,000',2500,prog_4_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Graphic Design",'$700-$1,000',850,prog_4_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Graphic Design",'Above $3,000',3000,prog_4_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Graphic Design",'Below $700',700,prog_4_7)

avg_pg_4 = 1100 * len(prog_4_1) + 1300 * len(prog_4_2) + 1750 * len(prog_4_3) + 2500 * len(prog_4_4) + 850 * len(prog_4_5) + 3000 * len(prog_4_6) + 700 * len(prog_4_7)
total_pg_4 = len(prog_4_1) + len(prog_4_2) + len(prog_4_3) + len(prog_4_4) + len(prog_4_5) +  len(prog_4_6) +  len(prog_4_7)
avg_pg_4 = avg_pg_4 / total_pg_4
avg_pg_4 = int(str(avg_pg_4).split(".")[0])
avg_pg_4_s = "BS in Graphic Design : $" + str(avg_pg_4).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Bioinformatics",'$1,001-$1,200',1100,prog_5_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Bioinformatics",'$1,201-$1,500',1350,prog_5_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Bioinformatics",'$1,501-$2,000',1750,prog_5_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Bioinformatics",'$2,001-$3,000',2500,prog_5_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Bioinformatics",'$700-$1,000',850,prog_5_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Bioinformatics",'Above $3,000',3000,prog_5_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Bioinformatics",'Below $700',700,prog_5_7)

avg_pg_5 = 1100 * len(prog_5_1) + 1300 * len(prog_5_2) + 1750 * len(prog_5_3) + 2500 * len(prog_5_4) + 850 * len(prog_5_5) + 3000 * len(prog_5_6) + 700 * len(prog_5_7)
total_pg_5 = len(prog_5_1) + len(prog_5_2) + len(prog_5_3) + len(prog_5_4) + len(prog_5_5) +  len(prog_5_6) +  len(prog_5_7)
avg_pg_5 = avg_pg_5 / total_pg_5
avg_pg_5 = int(str(avg_pg_5).split(".")[0])
avg_pg_5_s = "BS in Bioinformatics: $" + str(avg_pg_5).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Psychology",'$1,001-$1,200',1100,prog_6_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Psychology",'$1,201-$1,500',1350,prog_6_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Psychology",'$1,501-$2,000',1750,prog_6_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Psychology",'$2,001-$3,000',2500,prog_6_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Psychology",'$700-$1,000',850,prog_6_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Psychology",'Above $3,000',3000,prog_6_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Psychology",'Below $700',700,prog_6_7)

avg_pg_6 = 1100 * len(prog_6_1) + 1300 * len(prog_6_2) + 1750 * len(prog_6_3) + 2500 * len(prog_6_4) + 850 * len(prog_6_5) + 3000 * len(prog_6_6) + 700 * len(prog_6_7)
total_pg_6 = len(prog_6_1) + len(prog_6_2) + len(prog_6_3) + len(prog_6_4) + len(prog_6_5) +  len(prog_6_6) +  len(prog_6_7)
avg_pg_6 = avg_pg_6 / total_pg_6
avg_pg_6 = int(str(avg_pg_6).split(".")[0])
avg_pg_6_s = "BA in Psychology : $" + str(avg_pg_6).split(".")[0]


cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Political Sc/Int.Affairs",'$1,001-$1,200',1100,prog_7_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Political Sc/Int.Affairs",'$1,201-$1,500',1350,prog_7_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Political Sc/Int.Affairs",'$1,501-$2,000',1750,prog_7_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Political Sc/Int.Affairs",'$2,001-$3,000',2500,prog_7_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Political Sc/Int.Affairs",'$700-$1,000',850,prog_7_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Political Sc/Int.Affairs",'Above $3,000',3000,prog_7_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Political Sc/Int.Affairs",'Below $700',700,prog_7_7)

avg_pg_7 = 1100 * len(prog_7_1) + 1300 * len(prog_7_2) + 1750 * len(prog_7_3) + 2500 * len(prog_7_4) + 850 * len(prog_7_5) + 3000 * len(prog_7_6) + 700 * len(prog_7_7)
total_pg_7 = len(prog_7_1) + len(prog_7_2) + len(prog_7_3) + len(prog_7_4) + len(prog_7_5) +  len(prog_7_6) +  len(prog_7_7)
avg_pg_7 = avg_pg_7 / total_pg_7
avg_pg_7 = int(str(avg_pg_7).split(".")[0])
avg_pg_7_s = "BA in Political Sc/Int.Affairs : $" + str(avg_pg_7).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Teaching Diploma",'$1,001-$1,200',1100,prog_8_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Teaching Diploma",'$1,201-$1,500',1350,prog_8_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Teaching Diploma",'$1,501-$2,000',1750,prog_8_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Teaching Diploma",'$2,001-$3,000',2500,prog_8_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Teaching Diploma",'$700-$1,000',850,prog_8_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Teaching Diploma",'Above $3,000',3000,prog_8_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Teaching Diploma",'Below $700',700,prog_8_7)

avg_pg_8 = 1100 * len(prog_8_1) + 1300 * len(prog_8_2) + 1750 * len(prog_8_3) + 2500 * len(prog_8_4) + 850 * len(prog_8_5) + 3000 * len(prog_8_6) + 700 * len(prog_8_7)
total_pg_8 = len(prog_8_1) + len(prog_8_2) + len(prog_8_3) + len(prog_8_4) + len(prog_8_5) +  len(prog_8_6) +  len(prog_8_7)
avg_pg_8 = avg_pg_8 / total_pg_8
avg_pg_8 = int(str(avg_pg_8).split(".")[0])
avg_pg_8_s = "Teaching Diploma : $" + str(avg_pg_8).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Bachelor of Architecture",'$1,001-$1,200',1100,prog_9_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Bachelor of Architecture",'$1,201-$1,500',1350,prog_9_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Bachelor of Architecture",'$1,501-$2,000',1750,prog_9_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Bachelor of Architecture",'$2,001-$3,000',2500,prog_9_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Bachelor of Architecture",'$700-$1,000',850,prog_9_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Bachelor of Architecture",'Above $3,000',3000,prog_9_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Bachelor of Architecture",'Below $700',700,prog_9_7)

avg_pg_9 = 1100 * len(prog_9_1) + 1300 * len(prog_9_2) + 1750 * len(prog_9_3) + 2500 * len(prog_9_4) + 850 * len(prog_9_5) + 3000 * len(prog_9_6) + 700 * len(prog_9_7)
total_pg_9 = len(prog_9_1) + len(prog_9_2) + len(prog_9_3) + len(prog_9_4) + len(prog_9_5) +  len(prog_9_6) +  len(prog_9_7)
avg_pg_9 = avg_pg_9 / total_pg_9
avg_pg_9 = int(str(avg_pg_9).split(".")[0])
avg_pg_9_s = "Bachelor of Architecture : $" + str(avg_pg_9).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Biology",'$1,001-$1,200',1100,prog_10_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Biology",'$1,201-$1,500',1350,prog_10_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Biology",'$1,501-$2,000',1750,prog_10_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Biology",'$2,001-$3,000',2500,prog_10_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Biology",'$700-$1,000',850,prog_10_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Biology",'Above $3,000',3000,prog_10_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Biology",'Below $700',700,prog_10_7)

avg_pg_10 = 1100 * len(prog_10_1) + 1300 * len(prog_10_2) + 1750 * len(prog_10_3) + 2500 * len(prog_10_4) + 850 * len(prog_10_5) + 3000 * len(prog_10_6) + 700 * len(prog_10_7)
total_pg_10 = len(prog_10_1) + len(prog_10_2) + len(prog_10_3) + len(prog_10_4) + len(prog_10_5) +  len(prog_10_6) +  len(prog_10_7)
avg_pg_10 = avg_pg_10 / total_pg_10
avg_pg_10 = int(str(avg_pg_10).split(".")[0])
avg_pg_10_s = "BS in Biology : $" + str(avg_pg_10).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Education",'$1,001-$1,200',1100,prog_11_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Education",'$1,201-$1,500',1350,prog_11_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Education",'$1,501-$2,000',1750,prog_11_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Education",'$2,001-$3,000',2500,prog_11_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Education",'$700-$1,000',850,prog_11_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Education",'Above $3,000',3000,prog_11_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Education",'Below $700',700,prog_11_7)

avg_pg_11 = 1100 * len(prog_11_1) + 1300 * len(prog_11_2) + 1750 * len(prog_11_3) + 2500 * len(prog_11_4) + 850 * len(prog_11_5) + 3000 * len(prog_11_6) + 700 * len(prog_11_7)
total_pg_11 = len(prog_11_1) + len(prog_11_2) + len(prog_11_3) + len(prog_11_4) + len(prog_11_5) +  len(prog_11_6) +  len(prog_11_7)
avg_pg_11 = avg_pg_11 / total_pg_11
avg_pg_11 = int(str(avg_pg_11).split(".")[0])
avg_pg_11_s = "BA in Education : $" + str(avg_pg_11).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutrition",'$1,001-$1,200',1100,prog_12_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutrition",'$1,201-$1,500',1350,prog_12_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutrition",'$1,501-$2,000',1750,prog_12_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutrition",'$2,001-$3,000',2500,prog_12_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutrition",'$700-$1,000',850,prog_12_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutrition",'Above $3,000',3000,prog_12_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutrition",'Below $700',700,prog_12_7)

avg_pg_12 = 1100 * len(prog_12_1) + 1300 * len(prog_12_2) + 1750 * len(prog_12_3) + 2500 * len(prog_12_4) + 850 * len(prog_12_5) + 3000 * len(prog_12_6) + 700 * len(prog_12_7)
total_pg_12 = len(prog_12_1) + len(prog_12_2) + len(prog_12_3) + len(prog_12_4) + len(prog_12_5) +  len(prog_12_6) +  len(prog_12_7)
avg_pg_12 = avg_pg_12 / total_pg_12
avg_pg_12 = int(str(avg_pg_12).split(".")[0])
avg_pg_12_s = "BS in Nutrition : $" + str(avg_pg_12).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Economics",'$1,001-$1,200',1100,prog_13_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Economics",'$1,201-$1,500',1350,prog_13_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Economics",'$1,501-$2,000',1750,prog_13_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Economics",'$2,001-$3,000',2500,prog_13_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Economics",'$700-$1,000',850,prog_13_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Economics",'Above $3,000',3000,prog_13_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Economics",'Below $700',700,prog_13_7)

avg_pg_13 = 1100 * len(prog_13_1) + 1300 * len(prog_13_2) + 1750 * len(prog_13_3) + 2500 * len(prog_13_4) + 850 * len(prog_13_5) + 3000 * len(prog_13_6) + 700 * len(prog_13_7)
total_pg_13 = len(prog_13_1) + len(prog_13_2) + len(prog_13_3) + len(prog_13_4) + len(prog_13_5) +  len(prog_13_6) +  len(prog_13_7)
avg_pg_13 = avg_pg_13 / total_pg_13
avg_pg_13 = int(str(avg_pg_13).split(".")[0])
avg_pg_13_s = "BS in Economics : $" + str(avg_pg_13).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Computer Engineering",'$1,001-$1,200',1100,prog_14_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Computer Engineering",'$1,201-$1,500',1350,prog_14_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Computer Engineering",'$1,501-$2,000',1750,prog_14_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Computer Engineering",'$2,001-$3,000',2500,prog_14_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Computer Engineering",'$700-$1,000',850,prog_14_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Computer Engineering",'Above $3,000',3000,prog_14_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Computer Engineering",'Below $700',700,prog_14_7)

avg_pg_14 = 1100 * len(prog_14_1) + 1300 * len(prog_14_2) + 1750 * len(prog_14_3) + 2500 * len(prog_14_4) + 850 * len(prog_14_5) + 3000 * len(prog_14_6) + 700 * len(prog_14_7)
total_pg_14 = len(prog_14_1) + len(prog_14_2) + len(prog_14_3) + len(prog_14_4) + len(prog_14_5) +  len(prog_14_6) +  len(prog_14_7)
avg_pg_14 = avg_pg_14 / total_pg_14
avg_pg_14 = int(str(avg_pg_14).split(".")[0])
avg_pg_14_s = "BE in Computer Engineering : $" + str(avg_pg_14).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Multimedia Journalism",'$1,001-$1,200',1100,prog_15_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Multimedia Journalism",'$1,201-$1,500',1350,prog_15_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Multimedia Journalism",'$1,501-$2,000',1750,prog_15_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Multimedia Journalism",'$2,001-$3,000',2500,prog_15_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Multimedia Journalism",'$700-$1,000',850,prog_15_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Multimedia Journalism",'Above $3,000',3000,prog_15_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Multimedia Journalism",'Below $700',700,prog_15_7)

avg_pg_15 = 1100 * len(prog_15_1) + 1300 * len(prog_15_2) + 1750 * len(prog_15_3) + 2500 * len(prog_15_4) + 850 * len(prog_15_5) + 3000 * len(prog_15_6) + 700 * len(prog_15_7)
total_pg_15 = len(prog_15_1) + len(prog_15_2) + len(prog_15_3) + len(prog_15_4) + len(prog_15_5) +  len(prog_15_6) +  len(prog_15_7)
avg_pg_15 = avg_pg_15 / total_pg_15
avg_pg_15 = int(str(avg_pg_15).split(".")[0])
avg_pg_15_s = "BA in Multimedia Journalism : $" + str(avg_pg_15).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Business",'$1,001-$1,200',1100,prog_16_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Business",'$1,201-$1,500',1350,prog_16_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Business",'$1,501-$2,000',1750,prog_16_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Business",'$2,001-$3,000',2500,prog_16_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Business",'$700-$1,000',850,prog_16_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Business",'Above $3,000',3000,prog_16_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Business",'Below $700',700,prog_16_7)

avg_pg_16 = 1100 * len(prog_16_1) + 1300 * len(prog_16_2) + 1750 * len(prog_16_3) + 2500 * len(prog_16_4) + 850 * len(prog_16_5) + 3000 * len(prog_16_6) + 700 * len(prog_16_7)
total_pg_16 = len(prog_16_1) + len(prog_16_2) + len(prog_16_3) + len(prog_16_4) + len(prog_16_5) +  len(prog_16_6) +  len(prog_16_7)
avg_pg_16 = avg_pg_16 / total_pg_16
avg_pg_16 = int(str(avg_pg_16).split(".")[0])
avg_pg_16_s = "BS in Business : $" + str(avg_pg_16).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Chemistry",'$1,001-$1,200',1100,prog_17_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Chemistry",'$1,201-$1,500',1350,prog_17_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Chemistry",'$1,501-$2,000',1750,prog_17_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Chemistry",'$2,001-$3,000',2500,prog_17_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Chemistry",'$700-$1,000',850,prog_17_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Chemistry",'Above $3,000',3000,prog_17_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Chemistry",'Below $700',700,prog_17_7)

avg_pg_17 = 1100 * len(prog_17_1) + 1300 * len(prog_17_2) + 1750 * len(prog_17_3) + 2500 * len(prog_17_4) + 850 * len(prog_17_5) + 3000 * len(prog_17_6) + 700 * len(prog_17_7)
total_pg_17 = len(prog_17_1) + len(prog_17_2) + len(prog_17_3) + len(prog_17_4) + len(prog_17_5) +  len(prog_17_6) +  len(prog_17_7)
avg_pg_17 = avg_pg_17 / total_pg_17
avg_pg_17 = int(str(avg_pg_17).split(".")[0])
avg_pg_17_s = "BS in Chemistry : $" + str(avg_pg_17).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Computer Science",'$1,001-$1,200',1100,prog_18_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Computer Science",'$1,201-$1,500',1350,prog_18_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Computer Science",'$1,501-$2,000',1750,prog_18_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Computer Science",'$2,001-$3,000',2500,prog_18_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Computer Science",'$700-$1,000',850,prog_18_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Computer Science",'Above $3,000',3000,prog_18_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Computer Science",'Below $700',700,prog_18_7)

avg_pg_18 = 1100 * len(prog_18_1) + 1300 * len(prog_18_2) + 1750 * len(prog_18_3) + 2500 * len(prog_18_4) + 850 * len(prog_18_5) + 3000 * len(prog_18_6) + 700 * len(prog_18_7)
total_pg_18 = len(prog_18_1) + len(prog_18_2) + len(prog_18_3) + len(prog_18_4) + len(prog_18_5) +  len(prog_18_6) +  len(prog_18_7)
avg_pg_18 = avg_pg_18 / total_pg_18
avg_pg_18 = int(str(avg_pg_18).split(".")[0])
avg_pg_18_s = "BS in Computer Science : $" + str(avg_pg_18).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Civil Engineering",'$1,001-$1,200',1100,prog_19_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Civil Engineering",'$1,201-$1,500',1350,prog_19_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Civil Engineering",'$1,501-$2,000',1750,prog_19_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Civil Engineering",'$2,001-$3,000',2500,prog_19_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Civil Engineering",'$700-$1,000',850,prog_19_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Civil Engineering",'Above $3,000',3000,prog_19_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Civil Engineering",'Below $700',700,prog_19_7)

avg_pg_19 = 1100 * len(prog_19_1) + 1300 * len(prog_19_2) + 1750 * len(prog_19_3) + 2500 * len(prog_19_4) + 850 * len(prog_19_5) + 3000 * len(prog_19_6) + 700 * len(prog_19_7)
total_pg_19 = len(prog_19_1) + len(prog_19_2) + len(prog_19_3) + len(prog_19_4) + len(prog_19_5) +  len(prog_19_6) +  len(prog_19_7)
avg_pg_19 = avg_pg_19 / total_pg_19
avg_pg_19 = int(str(avg_pg_19).split(".")[0])
avg_pg_19_s = "BE in Civil Engineering : $" + str(avg_pg_19).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nursing",'$1,001-$1,200',1100,prog_20_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nursing",'$1,201-$1,500',1350,prog_20_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nursing",'$1,501-$2,000',1750,prog_20_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nursing",'$2,001-$3,000',2500,prog_20_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nursing",'$700-$1,000',850,prog_20_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nursing",'Above $3,000',3000,prog_20_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nursing",'Below $700',700,prog_20_7)

avg_pg_20 = 1100 * len(prog_20_1) + 1300 * len(prog_20_2) + 1750 * len(prog_20_3) + 2500 * len(prog_20_4) + 850 * len(prog_20_5) + 3000 * len(prog_20_6) + 700 * len(prog_20_7)
total_pg_20 = len(prog_20_1) + len(prog_20_2) + len(prog_20_3) + len(prog_20_4) + len(prog_20_5) +  len(prog_20_6) +  len(prog_20_7)
avg_pg_20 = avg_pg_20 / total_pg_20
avg_pg_20 = int(str(avg_pg_20).split(".")[0])
avg_pg_20_s = "BS in Nursing : $" + str(avg_pg_20).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Interior Architecture",'$1,001-$1,200',1100,prog_21_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Interior Architecture",'$1,201-$1,500',1350,prog_21_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Interior Architecture",'$1,501-$2,000',1750,prog_21_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Interior Architecture",'$2,001-$3,000',2500,prog_21_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Interior Architecture",'$700-$1,000',850,prog_21_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Interior Architecture",'Above $3,000',3000,prog_21_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Interior Architecture",'Below $700',700,prog_21_7)

avg_pg_21 = 1100 * len(prog_21_1) + 1300 * len(prog_21_2) + 1750 * len(prog_21_3) + 2500 * len(prog_21_4) + 850 * len(prog_21_5) + 3000 * len(prog_21_6) + 700 * len(prog_21_7)
total_pg_21 = len(prog_21_1) + len(prog_21_2) + len(prog_21_3) + len(prog_21_4) + len(prog_21_5) +  len(prog_21_6) +  len(prog_21_7)
avg_pg_21 = avg_pg_21 / total_pg_21
avg_pg_21 = int(str(avg_pg_21).split(".")[0])
avg_pg_21_s = "BA in Interior Architecture : $" + str(avg_pg_21).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fine Arts",'$1,001-$1,200',1100,prog_22_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fine Arts",'$1,201-$1,500',1350,prog_22_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fine Arts",'$1,501-$2,000',1750,prog_22_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fine Arts",'$2,001-$3,000',2500,prog_22_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fine Arts",'$700-$1,000',850,prog_22_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fine Arts",'Above $3,000',3000,prog_22_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fine Arts",'Below $700',700,prog_22_7)

avg_pg_22 = 1100 * len(prog_22_1) + 1300 * len(prog_22_2) + 1750 * len(prog_22_3) + 2500 * len(prog_22_4) + 850 * len(prog_22_5) + 3000 * len(prog_22_6) + 700 * len(prog_22_7)
total_pg_22 = len(prog_22_1) + len(prog_22_2) + len(prog_22_3) + len(prog_22_4) + len(prog_22_5) +  len(prog_22_6) +  len(prog_22_7)
avg_pg_22 = avg_pg_22 / total_pg_22
avg_pg_22 = int(str(avg_pg_22).split(".")[0])
avg_pg_22_s = "BA in Fine Arts : $" + str(avg_pg_22).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fashion Design",'$1,001-$1,200',1100,prog_23_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fashion Design",'$1,201-$1,500',1350,prog_23_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fashion Design",'$1,501-$2,000',1750,prog_23_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fashion Design",'$2,001-$3,000',2500,prog_23_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fashion Design",'$700-$1,000',850,prog_23_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fashion Design",'Above $3,000',3000,prog_23_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Fashion Design",'Below $700',700,prog_23_7)

avg_pg_23 = 1100 * len(prog_23_1) + 1300 * len(prog_23_2) + 1750 * len(prog_23_3) + 2500 * len(prog_23_4) + 850 * len(prog_23_5) + 3000 * len(prog_23_6) + 700 * len(prog_23_7)
total_pg_23 = len(prog_23_1) + len(prog_23_2) + len(prog_23_3) + len(prog_23_4) + len(prog_23_5) +  len(prog_23_6) +  len(prog_23_7)
avg_pg_23 = avg_pg_23 / total_pg_23
avg_pg_23 = int(str(avg_pg_23).split(".")[0])
avg_pg_23_s = "BA in Fashion Design : $" + str(avg_pg_23).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Mathematics",'$1,001-$1,200',1100,prog_24_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Mathematics",'$1,201-$1,500',1350,prog_24_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Mathematics",'$1,501-$2,000',1750,prog_24_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Mathematics",'$2,001-$3,000',2500,prog_24_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Mathematics",'$700-$1,000',850,prog_24_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Mathematics",'Above $3,000',3000,prog_24_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Mathematics",'Below $700',700,prog_24_7)

avg_pg_24 = 1100 * len(prog_24_1) + 1300 * len(prog_24_2) + 1750 * len(prog_24_3) + 2500 * len(prog_24_4) + 850 * len(prog_24_5) + 3000 * len(prog_24_6) + 700 * len(prog_24_7)
total_pg_24 = len(prog_24_1) + len(prog_24_2) + len(prog_24_3) + len(prog_24_4) + len(prog_24_5) +  len(prog_24_6) +  len(prog_24_7)
avg_pg_24 = avg_pg_24 / total_pg_24
avg_pg_24 = int(str(avg_pg_24).split(".")[0])
avg_pg_24_s = "BS in Mathematics : $" + str(avg_pg_24).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Interior Design",'$1,001-$1,200',1100,prog_25_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Interior Design",'$1,201-$1,500',1350,prog_25_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Interior Design",'$1,501-$2,000',1750,prog_25_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Interior Design",'$2,001-$3,000',2500,prog_25_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Interior Design",'$700-$1,000',850,prog_25_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Interior Design",'Above $3,000',3000,prog_25_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Interior Design",'Below $700',700,prog_25_7)

avg_pg_25 = 1100 * len(prog_25_1) + 1300 * len(prog_25_2) + 1750 * len(prog_25_3) + 2500 * len(prog_25_4) + 850 * len(prog_25_5) + 3000 * len(prog_25_6) + 700 * len(prog_25_7)
total_pg_25 = len(prog_25_1) + len(prog_25_2) + len(prog_25_3) + len(prog_25_4) + len(prog_25_5) +  len(prog_25_6) +  len(prog_25_7)
avg_pg_25 = avg_pg_25 / total_pg_25
avg_pg_25 = int(str(avg_pg_25).split(".")[0])
avg_pg_25_s = "BS in Interior Design : $" + str(avg_pg_25).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Translation",'$1,001-$1,200',1100,prog_26_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Translation",'$1,201-$1,500',1350,prog_26_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Translation",'$1,501-$2,000',1750,prog_26_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Translation",'$2,001-$3,000',2500,prog_26_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Translation",'$700-$1,000',850,prog_26_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Translation",'Above $3,000',3000,prog_26_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Translation",'Below $700',700,prog_26_7)

avg_pg_26 = 1100 * len(prog_26_1) + 1300 * len(prog_26_2) + 1750 * len(prog_26_3) + 2500 * len(prog_26_4) + 850 * len(prog_26_5) + 3000 * len(prog_26_6) + 700 * len(prog_26_7)
total_pg_26 = len(prog_26_1) + len(prog_26_2) + len(prog_26_3) + len(prog_26_4) + len(prog_26_5) +  len(prog_26_6) +  len(prog_26_7)
avg_pg_26 = avg_pg_26 / total_pg_26
avg_pg_26 = int(str(avg_pg_26).split(".")[0])
avg_pg_26_s = "BA in Translation : $" + str(avg_pg_26).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Performing Arts",'$1,001-$1,200',1100,prog_27_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Performing Arts",'$1,201-$1,500',1350,prog_27_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Performing Arts",'$1,501-$2,000',1750,prog_27_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Performing Arts",'$2,001-$3,000',2500,prog_27_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Performing Arts",'$700-$1,000',850,prog_27_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Performing Arts",'Above $3,000',3000,prog_27_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Performing Arts",'Below $700',700,prog_27_7)

avg_pg_27 = 1100 * len(prog_27_1) + 1300 * len(prog_27_2) + 1750 * len(prog_27_3) + 2500 * len(prog_27_4) + 850 * len(prog_27_5) + 3000 * len(prog_27_6) + 700 * len(prog_27_7)
total_pg_27 = len(prog_27_1) + len(prog_27_2) + len(prog_27_3) + len(prog_27_4) + len(prog_27_5) +  len(prog_27_6) +  len(prog_27_7)
avg_pg_27 = avg_pg_27 / total_pg_27
avg_pg_27 = int(str(avg_pg_27).split(".")[0])
avg_pg_27_s = "BA in Performing Arts : $" + str(avg_pg_27).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Social Work",'$1,001-$1,200',1100,prog_28_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Social Work",'$1,201-$1,500',1350,prog_28_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Social Work",'$1,501-$2,000',1750,prog_28_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Social Work",'$2,001-$3,000',2500,prog_28_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Social Work",'$700-$1,000',850,prog_28_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Social Work",'Above $3,000',3000,prog_28_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Social Work",'Below $700',700,prog_28_7)

avg_pg_28 = 1100 * len(prog_28_1) + 1300 * len(prog_28_2) + 1750 * len(prog_28_3) + 2500 * len(prog_28_4) + 850 * len(prog_28_5) + 3000 * len(prog_28_6) + 700 * len(prog_28_7)
total_pg_28 = len(prog_28_1) + len(prog_28_2) + len(prog_28_3) + len(prog_28_4) + len(prog_28_5) +  len(prog_28_6) +  len(prog_28_7)
avg_pg_28 = avg_pg_28 / total_pg_28
avg_pg_28 = int(str(avg_pg_28).split(".")[0])
avg_pg_28_s = "BA in Social Work : $" + str(avg_pg_28).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Petroleum Engineering",'$1,001-$1,200',1100,prog_29_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Petroleum Engineering",'$1,201-$1,500',1350,prog_29_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Petroleum Engineering",'$1,501-$2,000',1750,prog_29_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Petroleum Engineering",'$2,001-$3,000',2500,prog_29_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Petroleum Engineering",'$700-$1,000',850,prog_29_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Petroleum Engineering",'Above $3,000',3000,prog_29_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Petroleum Engineering",'Below $700',700,prog_29_7)

avg_pg_29 = 1100 * len(prog_29_1) + 1300 * len(prog_29_2) + 1750 * len(prog_29_3) + 2500 * len(prog_29_4) + 850 * len(prog_29_5) + 3000 * len(prog_29_6) + 700 * len(prog_29_7)
total_pg_29 = len(prog_29_1) + len(prog_29_2) + len(prog_29_3) + len(prog_29_4) + len(prog_29_5) +  len(prog_29_6) +  len(prog_29_7)
avg_pg_29 = avg_pg_29 / total_pg_29
avg_pg_29 = int(str(avg_pg_29).split(".")[0])
avg_pg_29_s = "BE in Petroleum Engineering : $" + str(avg_pg_29).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Mechanical Engineering",'$1,001-$1,200',1100,prog_30_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Mechanical Engineering",'$1,201-$1,500',1350,prog_30_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Mechanical Engineering",'$1,501-$2,000',1750,prog_30_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Mechanical Engineering",'$2,001-$3,000',2500,prog_30_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Mechanical Engineering",'$700-$1,000',850,prog_30_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Mechanical Engineering",'Above $3,000',3000,prog_30_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Mechanical Engineering",'Below $700',700,prog_30_7)

avg_pg_30 = 1100 * len(prog_30_1) + 1300 * len(prog_30_2) + 1750 * len(prog_30_3) + 2500 * len(prog_30_4) + 850 * len(prog_30_5) + 3000 * len(prog_30_6) + 700 * len(prog_30_7)
total_pg_30 = len(prog_30_1) + len(prog_30_2) + len(prog_30_3) + len(prog_30_4) + len(prog_30_5) +  len(prog_30_6) +  len(prog_30_7)
avg_pg_30 = avg_pg_30 / total_pg_30
avg_pg_30 = int(str(avg_pg_30).split(".")[0])
avg_pg_30_s = "BE in Mechanical Engineering : $" + str(avg_pg_30).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Television and Film",'$1,001-$1,200',1100,prog_31_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Television and Film",'$1,201-$1,500',1350,prog_31_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Television and Film",'$1,501-$2,000',1750,prog_31_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Television and Film",'$2,001-$3,000',2500,prog_31_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Television and Film",'$700-$1,000',850,prog_31_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Television and Film",'Above $3,000',3000,prog_31_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BA in Television and Film",'Below $700',700,prog_31_7)

avg_pg_31 = 1100 * len(prog_31_1) + 1300 * len(prog_31_2) + 1750 * len(prog_31_3) + 2500 * len(prog_31_4) + 850 * len(prog_31_5) + 3000 * len(prog_31_6) + 700 * len(prog_31_7)
total_pg_31 = len(prog_31_1) + len(prog_31_2) + len(prog_31_3) + len(prog_31_4) + len(prog_31_5) +  len(prog_31_6) +  len(prog_31_7)
avg_pg_31 = avg_pg_31 / total_pg_31
avg_pg_31 = int(str(avg_pg_31).split(".")[0])
avg_pg_31_s = "BA in Television and Film : $" + str(avg_pg_31).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutr.&Diet. Coord. Prog.",'$1,001-$1,200',1100,prog_32_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutr.&Diet. Coord. Prog.",'$1,201-$1,500',1350,prog_32_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutr.&Diet. Coord. Prog.",'$1,501-$2,000',1750,prog_32_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutr.&Diet. Coord. Prog.",'$2,001-$3,000',2500,prog_32_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutr.&Diet. Coord. Prog.",'$700-$1,000',850,prog_32_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutr.&Diet. Coord. Prog.",'Above $3,000',3000,prog_32_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Nutr.&Diet. Coord. Prog.",'Below $700',700,prog_32_7)

avg_pg_32 = 1100 * len(prog_32_1) + 1300 * len(prog_32_2) + 1750 * len(prog_32_3) + 2500 * len(prog_32_4) + 850 * len(prog_32_5) + 3000 * len(prog_32_6) + 700 * len(prog_32_7)
total_pg_32 = len(prog_32_1) + len(prog_32_2) + len(prog_32_3) + len(prog_32_4) + len(prog_32_5) +  len(prog_32_6) +  len(prog_32_7)
avg_pg_32 = avg_pg_32 / total_pg_32
avg_pg_32 = int(str(avg_pg_32).split(".")[0])
avg_pg_32_s = "BS in Nutr.&Diet. Coord. Prog. : $" + str(avg_pg_32).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Pharmacy",'$1,001-$1,200',1100,prog_33_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Pharmacy",'$1,201-$1,500',1350,prog_33_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Pharmacy",'$1,501-$2,000',1750,prog_33_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Pharmacy",'$2,001-$3,000',2500,prog_33_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Pharmacy",'$700-$1,000',850,prog_33_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Pharmacy",'Above $3,000',3000,prog_33_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BS in Pharmacy",'Below $700',700,prog_33_7)

avg_pg_33 = 1100 * len(prog_33_1) + 1300 * len(prog_33_2) + 1750 * len(prog_33_3) + 2500 * len(prog_33_4) + 850 * len(prog_33_5) + 3000 * len(prog_33_6) + 700 * len(prog_33_7)
total_pg_33 = len(prog_33_1) + len(prog_33_2) + len(prog_33_3) + len(prog_33_4) + len(prog_33_5) +  len(prog_33_6) +  len(prog_33_7)
avg_pg_33 = avg_pg_33 / total_pg_33
avg_pg_33 = int(str(avg_pg_33).split(".")[0])
avg_pg_33_s = "BS in Pharmacy : $" + str(avg_pg_33).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Dip.in Learn. Dis.& Giftedness",'$1,001-$1,200',1100,prog_34_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Dip.in Learn. Dis.& Giftedness",'$1,201-$1,500',1350,prog_34_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Dip.in Learn. Dis.& Giftedness",'$1,501-$2,000',1750,prog_34_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Dip.in Learn. Dis.& Giftedness",'$2,001-$3,000',2500,prog_34_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Dip.in Learn. Dis.& Giftedness",'$700-$1,000',850,prog_34_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Dip.in Learn. Dis.& Giftedness",'Above $3,000',3000,prog_34_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"Dip.in Learn. Dis.& Giftedness",'Below $700',700,prog_34_7)

avg_pg_34 = 1100 * len(prog_34_1) + 1300 * len(prog_34_2) + 1750 * len(prog_34_3) + 2500 * len(prog_34_4) + 850 * len(prog_34_5) + 3000 * len(prog_34_6) + 700 * len(prog_34_7)
total_pg_34 = len(prog_34_1) + len(prog_34_2) + len(prog_34_3) + len(prog_34_4) + len(prog_34_5) +  len(prog_34_6) +  len(prog_34_7)
avg_pg_34 = avg_pg_34 / total_pg_34
avg_pg_34 = int(str(avg_pg_34).split(".")[0])
avg_pg_34_s = "Dip.in Learn. Dis.& Giftedness : $" + str(avg_pg_34).split(".")[0]

cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Industrial Engineering",'$1,001-$1,200',1100,prog_35_1)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Industrial Engineering",'$1,201-$1,500',1350,prog_35_2)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Industrial Engineering",'$1,501-$2,000',1750,prog_35_3)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Industrial Engineering",'$2,001-$3,000',2500,prog_35_4)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Industrial Engineering",'$700-$1,000',850,prog_35_5)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Industrial Engineering",'Above $3,000',3000,prog_35_6)
cal_sal_24(fig_25_sal_1,fig_25_prog_1,"BE in Industrial Engineering",'Below $700',700,prog_35_7)

avg_pg_35 = 1100 * len(prog_35_1) + 1300 * len(prog_35_2) + 1750 * len(prog_35_3) + 2500 * len(prog_35_4) + 850 * len(prog_35_5) + 3000 * len(prog_35_6) + 700 * len(prog_35_7)
total_pg_35 = len(prog_35_1) + len(prog_35_2) + len(prog_35_3) + len(prog_35_4) + len(prog_35_5) +  len(prog_35_6) +  len(prog_35_7)
avg_pg_35 = avg_pg_35 / total_pg_35
avg_pg_35 = int(str(avg_pg_35).split(".")[0])
avg_pg_35_s = "BE in Industrial Engineering : $" + str(avg_pg_35).split(".")[0]

#  print below and manually created the sorted list
# final_25_prog = [avg_pg_1_s,avg_pg_2_s,avg_pg_3_s,avg_pg_4_s,avg_pg_5_s,avg_pg_6_s,avg_pg_7_s,avg_pg_8_s,avg_pg_9_s,avg_pg_10_s,avg_pg_11_s,avg_pg_12_s,avg_pg_13_s,avg_pg_14_s,avg_pg_15_s,avg_pg_16_s,avg_pg_17_s,avg_pg_18_s,avg_pg_19_s,avg_pg_20_s,avg_pg_21_s,avg_pg_22_s,avg_pg_23_s,avg_pg_24_s,avg_pg_25_s,avg_pg_26_s,avg_pg_27_s,avg_pg_28_s,avg_pg_29_s,avg_pg_30_s,avg_pg_31_s,avg_pg_32_s,avg_pg_33_s,avg_pg_34_s,avg_pg_35_s]
# final_25_sal = [avg_pg_1,avg_pg_2,avg_pg_3,avg_pg_4,avg_pg_5,avg_pg_6,avg_pg_7,avg_pg_8,avg_pg_9,avg_pg_10,avg_pg_11,avg_pg_12,avg_pg_13,avg_pg_14,avg_pg_15,avg_pg_16,avg_pg_17,avg_pg_18,avg_pg_19,avg_pg_20,avg_pg_21,avg_pg_22,avg_pg_23,avg_pg_24,avg_pg_25,avg_pg_26,avg_pg_27,avg_pg_28,avg_pg_29,avg_pg_30,avg_pg_31,avg_pg_32,avg_pg_33,avg_pg_34,avg_pg_35]

final_25_prog_sort = [
'BE in Electrical Engineering : $1781',
'BS in Computer Science : $1677',
'BE in Computer Engineering : $1459',
'BA in Translation : $1300',
'BA in Performing Arts : $1300',
'BE in Industrial Engineering : $1300',
'BE in Civil Engineering : $1234',
'Bachelor of Architecture : $1201',
'BA in Political Sc/Int.Affairs : $1200',
'BE in Mechanical Engineering : $1192',
'BS in Mathematics : $1190',
'BA in Television and Film : $1163',
'BS in Pharmacy : $1156',
'BS in Business : $1121',
'BS in Bioinformatics: $1100',
'BA in Interior Architecture : $1075',
'BS in Economics : $1057',
'BS in Nursing : $1050',
'BA in Psychology : $1037',
'BA in Multimedia Journalism : $1016',
'BS in Interior Design : $1000',
'BS in Graphic Design : $994',
'BA in Communication Arts : $975',
'BA in Education : $975',
'BS in Hosp. & Tourism Manag. : $960',
'Teaching Diploma : $920',
'BA in Fine Arts : $883',
'BA in Fashion Design : $850',
'Dip.in Learn. Dis.& Giftedness : $850',
'BS in Nutrition : $813',
'BS in Biology : $800',
'BS in Nutr.&Diet. Coord. Prog. : $800',
'BE in Petroleum Engineering : $775',
'BS in Chemistry : $700',
'BA in Social Work : $700'
]

final_25_sal_sort = [1781,1677,1459,1300,1300,1300,1234,1201,1200,1192,1190,1163,1156,1121,1100,1075,1057,1050,1037,1016,1000,994,975,975,960,920,883,850,850,813,800,800,775,700,700]

fig25_newdf = pd.DataFrame({'Program':final_25_prog_sort,'AVERAGE SALARY BY DEGREE':final_25_sal_sort})
fig25_sort = fig25_newdf.sort_values('AVERAGE SALARY BY DEGREE',ascending=True)
fig_25 = fig25_sort.plot.barh(x='Program', y='AVERAGE SALARY BY DEGREE')
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('fig25.jpg')


# FIGURE 26 AVERAGE STARTING BASIC SALARY BY INDUSTRY

df_26_indu = df['Q23_Company industry sector_Company industry sector'].to_list()
df_26_sal = df['Q21_What was your starting basic salary?_What was your starting basic salary?'].to_list()

fig_26_indus_1 = []
fig_26_sal_1 = []
for fig_26_i in range(0, len(df_26_sal)):
    if df_26_sal[fig_26_i] != 'D/A' and df_26_indu[fig_26_i] != 'D/A':
        fig_26_sal_1.append(df_26_sal[fig_26_i])
        fig_26_indus_1.append(df_26_indu[fig_26_i])

df_26_tmp = pd.DataFrame({"Industry":fig_26_indus_1,"Salary":fig_26_sal_1})
# df_26_tmp.to_excel("26.xlsx")

indus_1_1 = []
indus_1_2 = []
indus_1_3 = []
indus_1_4 = []
indus_1_5 = []
indus_1_6 = []
indus_1_7 = []

indus_2_1 = []
indus_2_2 = []
indus_2_3 = []
indus_2_4 = []
indus_2_5 = []
indus_2_6 = []
indus_2_7 = []

indus_3_1 = []
indus_3_2 = []
indus_3_3 = []
indus_3_4 = []
indus_3_5 = []
indus_3_6 = []
indus_3_7 = []

indus_4_1 = []
indus_4_2 = []
indus_4_3 = []
indus_4_4 = []
indus_4_5 = []
indus_4_6 = []
indus_4_7 = []

indus_5_1 = []
indus_5_2 = []
indus_5_3 = []
indus_5_4 = []
indus_5_5 = []
indus_5_6 = []
indus_5_7 = []

indus_6_1 = []
indus_6_2 = []
indus_6_3 = []
indus_6_4 = []
indus_6_5 = []
indus_6_6 = []
indus_6_7 = []

indus_7_1 = []
indus_7_2 = []
indus_7_3 = []
indus_7_4 = []
indus_7_5 = []
indus_7_6 = []
indus_7_7 = []

indus_8_1 = []
indus_8_2 = []
indus_8_3 = []
indus_8_4 = []
indus_8_5 = []
indus_8_6 = []
indus_8_7 = []

indus_9_1 = []
indus_9_2 = []
indus_9_3 = []
indus_9_4 = []
indus_9_5 = []
indus_9_6 = []
indus_9_7 = []

indus_10_1 = []
indus_10_2 = []
indus_10_3 = []
indus_10_4 = []
indus_10_5 = []
indus_10_6 = []
indus_10_7 = []

indus_11_1 = []
indus_11_2 = []
indus_11_3 = []
indus_11_4 = []
indus_11_5 = []
indus_11_6 = []
indus_11_7 = []

indus_12_1 = []
indus_12_2 = []
indus_12_3 = []
indus_12_4 = []
indus_12_5 = []
indus_12_6 = []
indus_12_7 = []

indus_13_1 = []
indus_13_2 = []
indus_13_3 = []
indus_13_4 = []
indus_13_5 = []
indus_13_6 = []
indus_13_7 = []

# Note again will use same function we created for 24 so need get confused only the parameters changes:

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Agriculture, Food & Natural Resources",'$1,001-$1,200',1100,indus_1_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Agriculture, Food & Natural Resources",'$1,201-$1,500',1350,indus_1_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Agriculture, Food & Natural Resources",'$1,501-$2,000',1750,indus_1_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Agriculture, Food & Natural Resources",'$2,001-$3,000',2500,indus_1_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Agriculture, Food & Natural Resources",'$700-$1,000',850,indus_1_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Agriculture, Food & Natural Resources",'Above $3,000',3000,indus_1_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Agriculture, Food & Natural Resources",'Below $700',700,indus_1_7)

avg_indus_1 = 1100 * len(indus_1_1) + 1300 * len(indus_1_2) + 1750 * len(indus_1_3) + 2500 * len(indus_1_4) + 850 * len(indus_1_5) + 3000 * len(indus_1_6) + 700 * len(indus_1_7)
total_indus_1 = len(indus_1_1) + len(indus_1_2) + len(indus_1_3) + len(indus_1_4) + len(indus_1_5) +  len(indus_1_6) +  len(indus_1_7)
avg_indus_1 = avg_indus_1 / total_indus_1
avg_indus_1 = int(str(avg_indus_1).split(".")[0])
avg_indus_1_s = "Agriculture, Food & Natural Resources : $" + str(avg_indus_1).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Education & Training",'$1,001-$1,200',1100,indus_2_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Education & Training",'$1,201-$1,500',1350,indus_2_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Education & Training",'$1,501-$2,000',1750,indus_2_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Education & Training",'$2,001-$3,000',2500,indus_2_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Education & Training",'$700-$1,000',850,indus_2_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Education & Training",'Above $3,000',3000,indus_2_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Education & Training",'Below $700',700,indus_2_7)

avg_indus_2 = 1100 * len(indus_2_1) + 1300 * len(indus_2_2) + 1750 * len(indus_2_3) + 2500 * len(indus_2_4) + 850 * len(indus_2_5) + 3000 * len(indus_2_6) + 700 * len(indus_2_7)
total_indus_2 = len(indus_2_1) + len(indus_2_2) + len(indus_2_3) + len(indus_2_4) + len(indus_2_5) +  len(indus_2_6) +  len(indus_2_7)
avg_indus_2 = avg_indus_2 / total_indus_2
avg_indus_2 = int(str(avg_indus_2).split(".")[0])
avg_indus_2_s = "Education & Training : $" + str(avg_indus_2).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Sales & Distribution of Consumer Products",'$1,001-$1,200',1100,indus_3_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Sales & Distribution of Consumer Products",'$1,201-$1,500',1350,indus_3_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Sales & Distribution of Consumer Products",'$1,501-$2,000',1750,indus_3_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Sales & Distribution of Consumer Products",'$2,001-$3,000',2500,indus_3_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Sales & Distribution of Consumer Products",'$700-$1,000',850,indus_3_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Sales & Distribution of Consumer Products",'Above $3,000',3000,indus_3_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Sales & Distribution of Consumer Products",'Below $700',700,indus_3_7)

avg_indus_3 = 1100 * len(indus_3_1) + 1300 * len(indus_3_2) + 1750 * len(indus_3_3) + 2500 * len(indus_3_4) + 850 * len(indus_3_5) + 3000 * len(indus_3_6) + 700 * len(indus_3_7)
total_indus_3 = len(indus_3_1) + len(indus_3_2) + len(indus_3_3) + len(indus_3_4) + len(indus_3_5) +  len(indus_3_6) +  len(indus_3_7)
avg_indus_3 = avg_indus_3 / total_indus_3
avg_indus_3 = int(str(avg_indus_3).split(".")[0])
avg_indus_3_s = "Sales & Distribution of Consumer Products  : $" + str(avg_indus_3).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Manufacturing",'$1,001-$1,200',1100,indus_4_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Manufacturing",'$1,201-$1,500',1350,indus_4_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Manufacturing",'$1,501-$2,000',1750,indus_4_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Manufacturing",'$2,001-$3,000',2500,indus_4_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Manufacturing",'$700-$1,000',850,indus_4_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Manufacturing",'Above $3,000',3000,indus_4_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Manufacturing",'Below $700',700,indus_4_7)

avg_indus_4 = 1100 * len(indus_4_1) + 1300 * len(indus_4_2) + 1750 * len(indus_4_3) + 2500 * len(indus_4_4) + 850 * len(indus_4_5) + 3000 * len(indus_4_6) + 700 * len(indus_4_7)
total_indus_4 = len(indus_4_1) + len(indus_4_2) + len(indus_4_3) + len(indus_4_4) + len(indus_4_5) +  len(indus_4_6) +  len(indus_4_7)
avg_indus_4 = avg_indus_4 / total_indus_4
avg_indus_4 = int(str(avg_indus_4).split(".")[0])
avg_indus_4_s = "Manufacturing  : $" + str(avg_indus_4).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Business, Management & Administration",'$1,001-$1,200',1100,indus_5_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Business, Management & Administration",'$1,201-$1,500',1350,indus_5_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Business, Management & Administration",'$1,501-$2,000',1750,indus_5_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Business, Management & Administration",'$2,001-$3,000',2500,indus_5_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Business, Management & Administration",'$700-$1,000',850,indus_5_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Business, Management & Administration",'Above $3,000',3000,indus_5_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Business, Management & Administration",'Below $700',700,indus_5_7)

avg_indus_5 = 1100 * len(indus_5_1) + 1300 * len(indus_5_2) + 1750 * len(indus_5_3) + 2500 * len(indus_5_4) + 850 * len(indus_5_5) + 3000 * len(indus_5_6) + 700 * len(indus_5_7)
total_indus_5 = len(indus_5_1) + len(indus_5_2) + len(indus_5_3) + len(indus_5_4) + len(indus_5_5) +  len(indus_5_6) +  len(indus_5_7)
avg_indus_5 = avg_indus_5 / total_indus_5
avg_indus_5 = int(str(avg_indus_5).split(".")[0])
avg_indus_5_s = "Business, Management & Administration  : $" + str(avg_indus_5).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Science, Technology, Engineering & Mathematics",'$1,001-$1,200',1100,indus_6_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Science, Technology, Engineering & Mathematics",'$1,201-$1,500',1350,indus_6_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Science, Technology, Engineering & Mathematics",'$1,501-$2,000',1750,indus_6_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Science, Technology, Engineering & Mathematics",'$2,001-$3,000',2500,indus_6_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Science, Technology, Engineering & Mathematics",'$700-$1,000',850,indus_6_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Science, Technology, Engineering & Mathematics",'Above $3,000',3000,indus_6_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Science, Technology, Engineering & Mathematics",'Below $700',700,indus_6_7)

avg_indus_6 = 1100 * len(indus_6_1) + 1300 * len(indus_6_2) + 1750 * len(indus_6_3) + 2500 * len(indus_6_4) + 850 * len(indus_6_5) + 3000 * len(indus_6_6) + 700 * len(indus_6_7)
total_indus_6 = len(indus_6_1) + len(indus_6_2) + len(indus_6_3) + len(indus_6_4) + len(indus_6_5) +  len(indus_6_6) +  len(indus_6_7)
avg_indus_6 = avg_indus_6 / total_indus_6
avg_indus_6 = int(str(avg_indus_6).split(".")[0])
avg_indus_6_s = "Science, Technology, Engineering & Mathematics  : $" + str(avg_indus_6).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Architecture & Construction",'$1,001-$1,200',1100,indus_7_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Architecture & Construction",'$1,201-$1,500',1350,indus_7_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Architecture & Construction",'$1,501-$2,000',1750,indus_7_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Architecture & Construction",'$2,001-$3,000',2500,indus_7_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Architecture & Construction",'$700-$1,000',850,indus_7_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Architecture & Construction",'Above $3,000',3000,indus_7_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Architecture & Construction",'Below $700',700,indus_7_7)

avg_indus_7 = 1100 * len(indus_7_1) + 1300 * len(indus_7_2) + 1750 * len(indus_7_3) + 2500 * len(indus_7_4) + 850 * len(indus_7_5) + 3000 * len(indus_7_6) + 700 * len(indus_7_7)
total_indus_7 = len(indus_7_1) + len(indus_7_2) + len(indus_7_3) + len(indus_7_4) + len(indus_7_5) +  len(indus_7_6) +  len(indus_7_7)
avg_indus_7 = avg_indus_7 / total_indus_7
avg_indus_7 = int(str(avg_indus_7).split(".")[0])
avg_indus_7_s = "Architecture & Construction  : $" + str(avg_indus_7).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Health Science/Medical",'$1,001-$1,200',1100,indus_8_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Health Science/Medical",'$1,201-$1,500',1350,indus_8_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Health Science/Medical",'$1,501-$2,000',1750,indus_8_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Health Science/Medical",'$2,001-$3,000',2500,indus_8_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Health Science/Medical",'$700-$1,000',850,indus_8_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Health Science/Medical",'Above $3,000',3000,indus_8_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Health Science/Medical",'Below $700',700,indus_8_7)

avg_indus_8 = 1100 * len(indus_8_1) + 1300 * len(indus_8_2) + 1750 * len(indus_8_3) + 2500 * len(indus_8_4) + 850 * len(indus_8_5) + 3000 * len(indus_8_6) + 700 * len(indus_8_7)
total_indus_8 = len(indus_8_1) + len(indus_8_2) + len(indus_8_3) + len(indus_8_4) + len(indus_8_5) +  len(indus_8_6) +  len(indus_8_7)
avg_indus_8 = avg_indus_8 / total_indus_8
avg_indus_8 = int(str(avg_indus_8).split(".")[0])
avg_indus_8_s = "Health Science/Medical  : $" + str(avg_indus_8).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Marketing, Sales & Services",'$1,001-$1,200',1100,indus_9_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Marketing, Sales & Services",'$1,201-$1,500',1350,indus_9_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Marketing, Sales & Services",'$1,501-$2,000',1750,indus_9_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Marketing, Sales & Services",'$2,001-$3,000',2500,indus_9_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Marketing, Sales & Services",'$700-$1,000',850,indus_9_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Marketing, Sales & Services",'Above $3,000',3000,indus_9_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Marketing, Sales & Services",'Below $700',700,indus_9_7)

avg_indus_9 = 1100 * len(indus_9_1) + 1300 * len(indus_9_2) + 1750 * len(indus_9_3) + 2500 * len(indus_9_4) + 850 * len(indus_9_5) + 3000 * len(indus_9_6) + 700 * len(indus_9_7)
total_indus_9 = len(indus_9_1) + len(indus_9_2) + len(indus_9_3) + len(indus_9_4) + len(indus_9_5) +  len(indus_9_6) +  len(indus_9_7)
avg_indus_9 = avg_indus_9 / total_indus_9
avg_indus_9 = int(str(avg_indus_9).split(".")[0])
avg_indus_9_s = "Marketing, Sales & Services  : $" + str(avg_indus_9).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Pharmaceuticals",'$1,001-$1,200',1100,indus_10_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Pharmaceuticals",'$1,201-$1,500',1350,indus_10_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Pharmaceuticals",'$1,501-$2,000',1750,indus_10_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Pharmaceuticals",'$2,001-$3,000',2500,indus_10_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Pharmaceuticals",'$700-$1,000',850,indus_10_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Pharmaceuticals",'Above $3,000',3000,indus_10_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Pharmaceuticals",'Below $700',700,indus_10_7)

avg_indus_10 = 1100 * len(indus_10_1) + 1300 * len(indus_10_2) + 1750 * len(indus_10_3) + 2500 * len(indus_10_4) + 850 * len(indus_10_5) + 3000 * len(indus_10_6) + 700 * len(indus_10_7)
total_indus_10 = len(indus_10_1) + len(indus_10_2) + len(indus_10_3) + len(indus_10_4) + len(indus_10_5) +  len(indus_10_6) +  len(indus_10_7)
avg_indus_10 = avg_indus_10 / total_indus_10
avg_indus_10 = int(str(avg_indus_10).split(".")[0])
avg_indus_10_s = "Pharmaceuticals  : $" + str(avg_indus_10).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Non-Governmental Organization",'$1,001-$1,200',1100,indus_11_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Non-Governmental Organization",'$1,201-$1,500',1350,indus_11_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Non-Governmental Organization",'$1,501-$2,000',1750,indus_11_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Non-Governmental Organization",'$2,001-$3,000',2500,indus_11_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Non-Governmental Organization",'$700-$1,000',850,indus_11_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Non-Governmental Organization",'Above $3,000',3000,indus_11_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Non-Governmental Organization",'Below $700',700,indus_11_7)

avg_indus_11 = 1100 * len(indus_11_1) + 1300 * len(indus_11_2) + 1750 * len(indus_11_3) + 2500 * len(indus_11_4) + 850 * len(indus_11_5) + 3000 * len(indus_11_6) + 700 * len(indus_11_7)
total_indus_11 = len(indus_11_1) + len(indus_11_2) + len(indus_11_3) + len(indus_11_4) + len(indus_11_5) +  len(indus_11_6) +  len(indus_11_7)
avg_indus_11 = avg_indus_11 / total_indus_11
avg_indus_11 = int(str(avg_indus_11).split(".")[0])
avg_indus_11_s = "Non-Governmental Organization  : $" + str(avg_indus_11).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Hospitality & Tourism",'$1,001-$1,200',1100,indus_12_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Hospitality & Tourism",'$1,201-$1,500',1350,indus_12_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Hospitality & Tourism",'$1,501-$2,000',1750,indus_12_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Hospitality & Tourism",'$2,001-$3,000',2500,indus_12_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Hospitality & Tourism",'$700-$1,000',850,indus_12_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Hospitality & Tourism",'Above $3,000',3000,indus_12_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Hospitality & Tourism",'Below $700',700,indus_12_7)

avg_indus_12 = 1100 * len(indus_12_1) + 1300 * len(indus_12_2) + 1750 * len(indus_12_3) + 2500 * len(indus_12_4) + 850 * len(indus_12_5) + 3000 * len(indus_12_6) + 700 * len(indus_12_7)
total_indus_12 = len(indus_12_1) + len(indus_12_2) + len(indus_12_3) + len(indus_12_4) + len(indus_12_5) +  len(indus_12_6) +  len(indus_12_7)
avg_indus_12 = avg_indus_12 / total_indus_12
avg_indus_12 = int(str(avg_indus_12).split(".")[0])
avg_indus_12_s = "Hospitality & Tourism  : $" + str(avg_indus_12).split(".")[0]

cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Other, specify",'$1,001-$1,200',1100,indus_13_1)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Other, specify",'$1,201-$1,500',1350,indus_13_2)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Other, specify",'$1,501-$2,000',1750,indus_13_3)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Other, specify",'$2,001-$3,000',2500,indus_13_4)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Other, specify",'$700-$1,000',850,indus_13_5)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Other, specify",'Above $3,000',3000,indus_13_6)
cal_sal_24(fig_26_sal_1,fig_26_indus_1,"Other, specify",'Below $700',700,indus_13_7)

avg_indus_13 = 1100 * len(indus_13_1) + 1300 * len(indus_13_2) + 1750 * len(indus_13_3) + 2500 * len(indus_13_4) + 850 * len(indus_13_5) + 3000 * len(indus_13_6) + 700 * len(indus_13_7)
total_indus_13 = len(indus_13_1) + len(indus_13_2) + len(indus_13_3) + len(indus_13_4) + len(indus_13_5) +  len(indus_13_6) +  len(indus_13_7)
avg_indus_13 = avg_indus_13 / total_indus_13
avg_indus_13 = int(str(avg_indus_13).split(".")[0])
avg_indus_13_s = "Other, specify  : $" + str(avg_indus_13).split(".")[0]

industry_26 = [avg_indus_1_s,avg_indus_2_s,avg_indus_3_s,avg_indus_4_s,avg_indus_5_s,avg_indus_6_s,avg_indus_7_s,avg_indus_8_s,avg_indus_9_s,avg_indus_10_s,avg_indus_11_s,avg_indus_12_s,avg_indus_13_s]
# print below and manually sorted and created final_26_sal_sort,final_26_indus_sort
# print(industry_26)

final_26_sal_sort = [2500,2375,1400,1300,1300,1300,1100,1100,1100,890,750,700,700]
final_26_indus_sort = ['Manufacturing  : $2500','Health Science/Medical  : $2375','Other, specify  : $1400','Non-Governmental Organization  : $1300','Pharmaceuticals  : $1300','Non-Governmental Organization  : $1300','Architecture & Construction  : $1100','Sales & Distribution of Consumer Products  : $1100','Hospitality & Tourism  : $1100','Marketing, Sales & Services  : $890', 'Education & Training : $750','Agriculture, Food & Natural Resources : $700','Science, Technology, Engineering & Mathematics  : $700']

fig26_newdf = pd.DataFrame({'Industry':final_26_indus_sort,'AVERAGE SALARY BY INDUSTRY':final_26_sal_sort})
fig26_sort = fig26_newdf.sort_values('AVERAGE SALARY BY INDUSTRY',ascending=True)
fig_26 = fig26_sort.plot.barh(x='Industry', y='AVERAGE SALARY BY INDUSTRY')
#  remove legend
plt.legend('',frameon=False)
plt.tight_layout()
plt.savefig('fig26.jpg')
plt.clf()

# FIGURE 27 AVERAGE STARTING BASIC SALARY WITH RESPECT TO TIME FROM GRADUATION
# https://stackoverflow.com/questions/52385428/plot-point-markers-and-lines-in-different-hues-but-the-same-style-with-seaborn

df_27_long = df['Q17_How long did it take you to find your first job?_How long did it take you to find your first job?'].to_list()
df_27_sal = df['Q21_What was your starting basic salary?_What was your starting basic salary?'].to_list()

fig_27_long_1 = []
fig_27_sal_1 = []
for fig_27_i in range(0, len(df_27_sal)):
    if df_27_sal[fig_27_i] != 'D/A' and df_27_sal[fig_27_i] != 'D/A':
        fig_27_sal_1.append(df_27_sal[fig_27_i])
        fig_27_long_1.append(df_27_long[fig_27_i])

df_27_tmp = pd.DataFrame({"howlong":fig_27_long_1,"Salary":fig_27_sal_1})
# df_27_tmp.to_excel('27.xlsx')

hwlng_1_1 = []
hwlng_1_2 = []
hwlng_1_3 = []
hwlng_1_4 = []
hwlng_1_5 = []
hwlng_1_6 = []
hwlng_1_7 = []

hwlng_2_1 = []
hwlng_2_2 = []
hwlng_2_3 = []
hwlng_2_4 = []
hwlng_2_5 = []
hwlng_2_6 = []
hwlng_2_7 = []

hwlng_3_1 = []
hwlng_3_2 = []
hwlng_3_3 = []
hwlng_3_4 = []
hwlng_3_5 = []
hwlng_3_6 = []
hwlng_3_7 = []

hwlng_4_1 = []
hwlng_4_2 = []
hwlng_4_3 = []
hwlng_4_4 = []
hwlng_4_5 = []
hwlng_4_6 = []
hwlng_4_7 = []

hwlng_5_1 = []
hwlng_5_2 = []
hwlng_5_3 = []
hwlng_5_4 = []
hwlng_5_5 = []
hwlng_5_6 = []
hwlng_5_7 = []

cal_sal_24(fig_27_sal_1,fig_27_long_1,"1-2 years",'$1,001-$1,200',1100,hwlng_1_1)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"1-2 years",'$1,201-$1,500',1350,hwlng_1_2)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"1-2 years",'$1,501-$2,000',1750,hwlng_1_3)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"1-2 years",'$2,001-$3,000',2500,hwlng_1_4)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"1-2 years",'$700-$1,000',850,hwlng_1_5)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"1-2 years",'Above $3,000',3000,hwlng_1_6)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"1-2 years",'Below $700',700,hwlng_1_7)

avg_hwlng_1 = 1100 * len(hwlng_1_1) + 1300 * len(hwlng_1_2) + 1850 * len(hwlng_1_3) + 2500 * len(hwlng_1_4) + 850 * len(hwlng_1_5) + 3000 * len(hwlng_1_6) + 700 * len(hwlng_1_7)
total_hwlng_1 = len(hwlng_1_1) + len(hwlng_1_2) + len(hwlng_1_3) + len(hwlng_1_4) + len(hwlng_1_5) +  len(hwlng_1_6) +  len(hwlng_1_7)
avg_hwlng_1 = avg_hwlng_1 / total_hwlng_1
avg_hwlng_1 = int(str(avg_hwlng_1).split(".")[0])
avg_hwlng_1_s = "1-2 years : $" + str(avg_hwlng_1).split(".")[0]

cal_sal_24(fig_27_sal_1,fig_27_long_1,"6-12 months",'$1,001-$1,200',1100,hwlng_2_1)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"6-12 months",'$1,201-$1,500',1350,hwlng_2_2)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"6-12 months",'$1,501-$2,000',1750,hwlng_2_3)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"6-12 months",'$2,001-$3,000',2500,hwlng_2_4)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"6-12 months",'$700-$1,000',850,hwlng_2_5)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"6-12 months",'Above $3,000',3000,hwlng_2_6)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"6-12 months",'Below $700',700,hwlng_2_7)

avg_hwlng_2 = 1100 * len(hwlng_2_1) + 1300 * len(hwlng_2_2) + 1750 * len(hwlng_2_3) + 2500 * len(hwlng_2_4) + 850 * len(hwlng_2_5) + 3000 * len(hwlng_2_6) + 700 * len(hwlng_2_7)
total_hwlng_2 = len(hwlng_2_1) + len(hwlng_2_2) + len(hwlng_2_3) + len(hwlng_2_4) + len(hwlng_2_5) +  len(hwlng_2_6) +  len(hwlng_2_7)
avg_hwlng_2 = avg_hwlng_2 / total_hwlng_2
avg_hwlng_2 = int(str(avg_hwlng_2).split(".")[0])
avg_hwlng_2_s = "6-12 months : $" + str(avg_hwlng_2).split(".")[0]

cal_sal_24(fig_27_sal_1,fig_27_long_1,"I found the job before graduating from LAU",'$1,001-$1,200',1100,hwlng_3_1)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"I found the job before graduating from LAU",'$1,201-$1,500',1350,hwlng_3_2)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"I found the job before graduating from LAU",'$1,501-$2,000',1750,hwlng_3_3)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"I found the job before graduating from LAU",'$2,001-$3,000',2500,hwlng_3_4)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"I found the job before graduating from LAU",'$700-$1,000',850,hwlng_3_5)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"I found the job before graduating from LAU",'Above $3,000',3000,hwlng_3_6)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"I found the job before graduating from LAU",'Below $700',700,hwlng_3_7)

avg_hwlng_3 = 1100 * len(hwlng_3_1) + 1300 * len(hwlng_3_2) + 1750 * len(hwlng_3_3) + 2500 * len(hwlng_3_4) + 850 * len(hwlng_3_5) + 3000 * len(hwlng_3_6) + 700 * len(hwlng_3_7)
total_hwlng_3 = len(hwlng_3_1) + len(hwlng_3_2) + len(hwlng_3_3) + len(hwlng_3_4) + len(hwlng_3_5) +  len(hwlng_3_6) +  len(hwlng_3_7)
avg_hwlng_3 = avg_hwlng_3 / total_hwlng_3
avg_hwlng_3 = int(str(avg_hwlng_3).split(".")[0])
avg_hwlng_3_s = "I found the job before graduating from LAU : $" + str(avg_hwlng_3).split(".")[0]

cal_sal_24(fig_27_sal_1,fig_27_long_1,"0-3 months",'$1,001-$1,200',1100,hwlng_4_1)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"0-3 months",'$1,201-$1,500',1350,hwlng_4_2)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"0-3 months",'$1,501-$2,000',1750,hwlng_4_3)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"0-3 months",'$2,001-$3,000',2500,hwlng_4_4)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"0-3 months",'$700-$1,000',850,hwlng_4_5)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"0-3 months",'Above $3,000',3000,hwlng_4_6)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"0-3 months",'Below $700',700,hwlng_4_7)

avg_hwlng_4 = 1100 * len(hwlng_4_1) + 1300 * len(hwlng_4_2) + 1750 * len(hwlng_4_3) + 2500 * len(hwlng_4_4) + 850 * len(hwlng_4_5) + 3000 * len(hwlng_4_6) + 700 * len(hwlng_4_7)
total_hwlng_4 = len(hwlng_4_1) + len(hwlng_4_2) + len(hwlng_4_3) + len(hwlng_4_4) + len(hwlng_4_5) +  len(hwlng_4_6) +  len(hwlng_4_7)
avg_hwlng_4 = avg_hwlng_4 / total_hwlng_4
avg_hwlng_4 = int(str(avg_hwlng_4).split(".")[0])
avg_hwlng_4_s = "0-3 months : $" + str(avg_hwlng_4).split(".")[0]

cal_sal_24(fig_27_sal_1,fig_27_long_1,"3-6 months",'$1,001-$1,200',1100,hwlng_5_1)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"3-6 months",'$1,201-$1,500',1350,hwlng_5_2)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"3-6 months",'$1,501-$2,000',1750,hwlng_5_3)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"3-6 months",'$2,001-$3,000',2500,hwlng_5_4)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"3-6 months",'$700-$1,000',850,hwlng_5_5)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"3-6 months",'Above $3,000',3000,hwlng_5_6)
cal_sal_24(fig_27_sal_1,fig_27_long_1,"3-6 months",'Below $700',700,hwlng_5_7)

avg_hwlng_5 = 1100 * len(hwlng_5_1) + 1300 * len(hwlng_5_2) + 1750 * len(hwlng_5_3) + 2500 * len(hwlng_5_4) + 850 * len(hwlng_5_5) + 3000 * len(hwlng_5_6) + 700 * len(hwlng_5_7)
total_hwlng_5 = len(hwlng_5_1) + len(hwlng_5_2) + len(hwlng_5_3) + len(hwlng_5_4) + len(hwlng_5_5) +  len(hwlng_5_6) +  len(hwlng_5_7)
avg_hwlng_5 = avg_hwlng_5 / total_hwlng_5
avg_hwlng_5 = int(str(avg_hwlng_5).split(".")[0])
avg_hwlng_5_s = "3-6 months : $" + str(avg_hwlng_5).split(".")[0]

fig_27_long_nw = list(set(fig_27_long_1))
fig_27_avg_sal_int= [avg_hwlng_1,avg_hwlng_2,avg_hwlng_3,avg_hwlng_4,avg_hwlng_5]
fig_27_avg_sal = [avg_hwlng_1_s,avg_hwlng_2_s,avg_hwlng_3_s,avg_hwlng_4_s,avg_hwlng_5_s]

# print(fig_27_long_nw)
# print(fig_27_avg_sal_int)
# print(fig_27_avg_sal)

fig_27_x = [fig_27_avg_sal[2] , fig_27_avg_sal[3] , fig_27_avg_sal[4] , fig_27_avg_sal[1] , fig_27_avg_sal[0]]
fig_27_y = [fig_27_avg_sal_int[2] , fig_27_avg_sal_int[3] , fig_27_avg_sal_int[4] , fig_27_avg_sal_int[1] , fig_27_avg_sal_int[0]]

# plt.rcParams["figure.figsize"] = (20,3)
plt.plot(fig_27_x,fig_27_y, 'r', lw=3)
plt.scatter(fig_27_x,fig_27_y, s=120, zorder=2)
plt.xticks(rotation=90,fontsize=10)
plt.tight_layout()
plt.savefig("fig27.jpg")
plt.clf()

# FIGURE 30 ALUMNI WHO WERE OFFERED A FULL-TIME JOB AFTER COMPLETION OF INTERNSHIP BY DEGREE

fig_30_prog = df['Program'].to_list()
fig_30_intern = df["Q5_After completing your internship, did the company offer you a full time job?_After completing your internship, did the company offer you a full time job?"].to_list()

fig_30_prog_nw = []
fig_30_intern_nw = []
for fig_30_i in range(0,len(fig_30_intern)):
    if fig_30_intern[fig_30_i] != 'D/A':
        fig_30_prog_nw.append(fig_30_prog[fig_30_i])
        fig_30_intern_nw.append(fig_30_intern[fig_30_i])

l_30 = list(set(fig_30_prog_nw))
df_30_tmp = pd.DataFrame({"Program":fig_30_prog_nw,"Inters":fig_30_intern_nw})
# df_30_tmp.to_excel("30.xlsx")


y_30_1 = 0
n_30_1 = 0

y_30_2 = 0
n_30_2 = 0

y_30_3 = 0
n_30_3 = 0

y_30_4 = 0
n_30_4 = 0

y_30_5 = 0
n_30_5 = 0

y_30_6 = 0
n_30_6 = 0

y_30_7 = 0
n_30_7 = 0

y_30_8 = 0
n_30_8 = 0

y_30_9 = 0
n_30_9 = 0

y_30_10 = 0
n_30_10 = 0

y_30_11 = 0
n_30_11 = 0

y_30_12 = 0
n_30_12 = 0

y_30_13 = 0
n_30_13 = 0

y_30_14 = 0
n_30_14 = 0

y_30_15 = 0
n_30_15 = 0

y_30_16 = 0
n_30_16 = 0

y_30_17 = 0
n_30_17 = 0

y_30_18 = 0
n_30_18 = 0

y_30_19 = 0
n_30_19 = 0

y_30_20 = 0
n_30_20 = 0

y_30_21 = 0
n_30_21 = 0

y_30_22 = 0
n_30_22 = 0

y_30_23 = 0
n_30_23 = 0

y_30_24 = 0
n_30_24 = 0

y_30_25 = 0
n_30_25 = 0

y_30_26 = 0
n_30_26 = 0

y_30_27 = 0
n_30_27 = 0

y_30_28 = 0
n_30_28 = 0

y_30_29 = 0
n_30_29 = 0

y_30_30 = 0
n_30_30 = 0

y_30_31 = 0
n_30_31 = 0

y_30_32 = 0
n_30_32 = 0

y_30_33 = 0
n_30_33 = 0

y_30_34 = 0
n_30_34 = 0


for v_30 in range(0,len(fig_30_prog_nw)):

    if fig_30_prog_nw[v_30] == 'BA in Fashion Design' and fig_30_intern_nw[v_30] == 'Yes':y_30_1 += 1
    if fig_30_prog_nw[v_30] == 'BA in Fashion Design' and fig_30_intern_nw[v_30] == 'No':n_30_1 += 1

    if fig_30_prog_nw[v_30] == 'BE in Electrical Engineering' and fig_30_intern_nw[v_30] == 'Yes':y_30_2 += 1
    if fig_30_prog_nw[v_30] == 'BE in Electrical Engineering' and fig_30_intern_nw[v_30] == 'No':n_30_2 += 1

    if fig_30_prog_nw[v_30] == 'BS in Mathematics' and fig_30_intern_nw[v_30] == 'Yes':y_30_3 += 1
    if fig_30_prog_nw[v_30] == 'BS in Mathematics' and fig_30_intern_nw[v_30] == 'No':n_30_3 += 1

    if fig_30_prog_nw[v_30] == 'BS in Business' and fig_30_intern_nw[v_30] == 'Yes':y_30_4 += 1
    if fig_30_prog_nw[v_30] == 'BS in Business' and fig_30_intern_nw[v_30] == 'No':n_30_4 += 1

    if fig_30_prog_nw[v_30] == 'BE in Civil Engineering' and fig_30_intern_nw[v_30] == 'Yes':y_30_5 += 1
    if fig_30_prog_nw[v_30] == 'BE in Civil Engineering' and fig_30_intern_nw[v_30] == 'No':n_30_5 += 1

    if fig_30_prog_nw[v_30] == 'BA in Television and Film' and fig_30_intern_nw[v_30] == 'Yes':y_30_6 += 1
    if fig_30_prog_nw[v_30] == 'BA in Television and Film' and fig_30_intern_nw[v_30] == 'No':n_30_6 += 1

    if fig_30_prog_nw[v_30] == 'BS in Interior Design' and fig_30_intern_nw[v_30] == 'Yes':y_30_7 += 1
    if fig_30_prog_nw[v_30] == 'BS in Interior Design' and fig_30_intern_nw[v_30] == 'No':n_30_7 += 1

    if fig_30_prog_nw[v_30] == 'BA in Fine Arts' and fig_30_intern_nw[v_30] == 'Yes':y_30_8 += 1
    if fig_30_prog_nw[v_30] == 'BA in Fine Arts' and fig_30_intern_nw[v_30] == 'No':n_30_8 += 1

    if fig_30_prog_nw[v_30] == 'BA in Psychology' and fig_30_intern_nw[v_30] == 'Yes':y_30_9 += 1
    if fig_30_prog_nw[v_30] == 'BA in Psychology' and fig_30_intern_nw[v_30] == 'No':n_30_9 += 1

    if fig_30_prog_nw[v_30] == 'BA in Education' and fig_30_intern_nw[v_30] == 'Yes':y_30_10 += 1
    if fig_30_prog_nw[v_30] == 'BA in Education' and fig_30_intern_nw[v_30] == 'No':n_30_10 += 1

    if fig_30_prog_nw[v_30] == 'Bachelor of Architecture' and fig_30_intern_nw[v_30] == 'Yes':y_30_11 += 1
    if fig_30_prog_nw[v_30] == 'Bachelor of Architecture' and fig_30_intern_nw[v_30] == 'No':n_30_11 += 1

    if fig_30_prog_nw[v_30] == 'BA in Interior Architecture' and fig_30_intern_nw[v_30] == 'Yes':y_30_12 += 1
    if fig_30_prog_nw[v_30] == 'BA in Interior Architecture' and fig_30_intern_nw[v_30] == 'No':n_30_12 += 1

    if fig_30_prog_nw[v_30] == 'BS in Economics' and fig_30_intern_nw[v_30] == 'Yes':y_30_13 += 1
    if fig_30_prog_nw[v_30] == 'BS in Economics' and fig_30_intern_nw[v_30] == 'No':n_30_13 += 1

    if fig_30_prog_nw[v_30] == 'BS in Biology' and fig_30_intern_nw[v_30] == 'Yes':y_30_14 += 1
    if fig_30_prog_nw[v_30] == 'BS in Biology' and fig_30_intern_nw[v_30] == 'No':n_30_14 += 1

    if fig_30_prog_nw[v_30] == 'BE in Computer Engineering' and fig_30_intern_nw[v_30] == 'Yes':y_30_15 += 1
    if fig_30_prog_nw[v_30] == 'BE in Computer Engineering' and fig_30_intern_nw[v_30] == 'No':n_30_15 += 1

    if fig_30_prog_nw[v_30] == 'BE in Petroleum Engineering' and fig_30_intern_nw[v_30] == 'Yes':y_30_16 += 1
    if fig_30_prog_nw[v_30] == 'BE in Petroleum Engineering' and fig_30_intern_nw[v_30] == 'No':n_30_16 += 1

    if fig_30_prog_nw[v_30] == 'BS in Hosp. & Tourism Manag.' and fig_30_intern_nw[v_30] == 'Yes':y_30_17 += 1
    if fig_30_prog_nw[v_30] == 'BS in Hosp. & Tourism Manag.' and fig_30_intern_nw[v_30] == 'No':n_30_17 += 1

    if fig_30_prog_nw[v_30] == 'BS in Computer Science' and fig_30_intern_nw[v_30] == 'Yes':y_30_18 += 1
    if fig_30_prog_nw[v_30] == 'BS in Computer Science' and fig_30_intern_nw[v_30] == 'No':n_30_18 += 1

    if fig_30_prog_nw[v_30] == 'BE in Mechanical Engineering' and fig_30_intern_nw[v_30] == 'Yes':y_30_19 += 1
    if fig_30_prog_nw[v_30] == 'BE in Mechanical Engineering' and fig_30_intern_nw[v_30] == 'No':n_30_19 += 1

    if fig_30_prog_nw[v_30] == 'BA in Performing Arts' and fig_30_intern_nw[v_30] == 'Yes':y_30_20 += 1
    if fig_30_prog_nw[v_30] == 'BA in Performing Arts' and fig_30_intern_nw[v_30] == 'No':n_30_20 += 1

    if fig_30_prog_nw[v_30] == 'BS in Nutrition' and fig_30_intern_nw[v_30] == 'Yes':y_30_21 += 1
    if fig_30_prog_nw[v_30] == 'BS in Nutrition' and fig_30_intern_nw[v_30] == 'No':n_30_21 += 1

    if fig_30_prog_nw[v_30] == 'BA in Political Sc/Int.Affairs' and fig_30_intern_nw[v_30] == 'Yes':y_30_22 += 1
    if fig_30_prog_nw[v_30] == 'BA in Political Sc/Int.Affairs' and fig_30_intern_nw[v_30] == 'No':n_30_22 += 1

    if fig_30_prog_nw[v_30] == 'BE in Industrial Engineering' and fig_30_intern_nw[v_30] == 'Yes':y_30_23 += 1
    if fig_30_prog_nw[v_30] == 'BE in Industrial Engineering' and fig_30_intern_nw[v_30] == 'No':n_30_23 += 1

    if fig_30_prog_nw[v_30] == 'BA in Multimedia Journalism' and fig_30_intern_nw[v_30] == 'Yes':y_30_24 += 1
    if fig_30_prog_nw[v_30] == 'BA in Multimedia Journalism' and fig_30_intern_nw[v_30] == 'No':n_30_24 += 1

    if fig_30_prog_nw[v_30] == 'BS in Nutr.&Diet. Coord. Prog.' and fig_30_intern_nw[v_30] == 'Yes':y_30_25 += 1
    if fig_30_prog_nw[v_30] == 'BS in Nutr.&Diet. Coord. Prog.' and fig_30_intern_nw[v_30] == 'No':n_30_25 += 1

    if fig_30_prog_nw[v_30] == 'BA in Social Work' and fig_30_intern_nw[v_30] == 'Yes':y_30_26 += 1
    if fig_30_prog_nw[v_30] == 'BA in Social Work' and fig_30_intern_nw[v_30] == 'No':n_30_26 += 1

    if fig_30_prog_nw[v_30] == 'BS in Chemistry' and fig_30_intern_nw[v_30] == 'Yes':y_30_27 += 1
    if fig_30_prog_nw[v_30] == 'BS in Chemistry' and fig_30_intern_nw[v_30] == 'No':n_30_27 += 1

    if fig_30_prog_nw[v_30] == 'BA in Communication Arts' and fig_30_intern_nw[v_30] == 'Yes':y_30_28 += 1
    if fig_30_prog_nw[v_30] == 'BA in Communication Arts' and fig_30_intern_nw[v_30] == 'No':n_30_28 += 1

    if fig_30_prog_nw[v_30] == 'Teaching Diploma' and fig_30_intern_nw[v_30] == 'Yes':y_30_29 += 1
    if fig_30_prog_nw[v_30] == 'Teaching Diploma' and fig_30_intern_nw[v_30] == 'No':n_30_29 += 1

    if fig_30_prog_nw[v_30] == 'Dip.in Learn. Dis.& Giftedness' and fig_30_intern_nw[v_30] == 'Yes':y_30_30 += 1
    if fig_30_prog_nw[v_30] == 'Dip.in Learn. Dis.& Giftedness' and fig_30_intern_nw[v_30] == 'No':n_30_30 += 1

    if fig_30_prog_nw[v_30] == 'BS in Pharmacy' and fig_30_intern_nw[v_30] == 'Yes':y_30_31 += 1
    if fig_30_prog_nw[v_30] == 'BS in Pharmacy' and fig_30_intern_nw[v_30] == 'No':n_30_31 += 1

    if fig_30_prog_nw[v_30] == 'BS in Nursing' and fig_30_intern_nw[v_30] == 'Yes':y_30_32 += 1
    if fig_30_prog_nw[v_30] == 'BS in Nursing' and fig_30_intern_nw[v_30] == 'No':n_30_32 += 1

    if fig_30_prog_nw[v_30] == 'BA in Translation' and fig_30_intern_nw[v_30] == 'Yes':y_30_33 += 1
    if fig_30_prog_nw[v_30] == 'BA in Translation' and fig_30_intern_nw[v_30] == 'No':n_30_33 += 1

    if fig_30_prog_nw[v_30] == 'BS in Graphic Design' and fig_30_intern_nw[v_30] == 'Yes':y_30_34 += 1
    if fig_30_prog_nw[v_30] == 'BS in Graphic Design' and fig_30_intern_nw[v_30] == 'No':n_30_34 += 1

per_30_1_int = int(str(y_30_1 * 100 / (y_30_1 + n_30_1)).split(".")[0])
per_30_1_s = 'BA in Fashion Design : ' + str(per_30_1_int) + "%"

per_30_2_int = int(str(y_30_2 * 100 / (y_30_2 + n_30_2)).split(".")[0])
per_30_2_s = 'BE in Electrical Engineering : ' + str(per_30_2_int) + "%"

per_30_3_int = int(str(y_30_3 * 100 / (y_30_3 + n_30_3)).split(".")[0])
per_30_3_s = 'BS in Mathematics : ' + str(per_30_3_int) + "%"

per_30_4_int = int(str(y_30_4 * 100 / (y_30_4 + n_30_4)).split(".")[0])
per_30_4_s = 'BS in Business : ' + str(per_30_4_int) + "%"

per_30_5_int = int(str(y_30_5 * 100 / (y_30_5 + n_30_5)).split(".")[0])
per_30_5_s = 'BE in Civil Engineering : ' + str(per_30_5_int) + "%"

per_30_6_int = int(str(y_30_6 * 100 / (y_30_6 + n_30_6)).split(".")[0])
per_30_6_s = 'BA in Television and Film : ' + str(per_30_6_int) + "%"

per_30_7_int = int(str(y_30_7 * 100 / (y_30_7 + n_30_7)).split(".")[0])
per_30_7_s = 'BS in Interior Design : ' + str(per_30_7_int) + "%"

per_30_8_int = int(str(y_30_8 * 100 / (y_30_8 + n_30_8)).split(".")[0])
per_30_8_s = 'BA in Fine Arts : ' + str(per_30_8_int) + "%"

per_30_9_int = int(str(y_30_9 * 100 / (y_30_9 + n_30_9)).split(".")[0])
per_30_9_s = 'BA in Psychology : ' + str(per_30_9_int) + "%"

per_30_10_int = int(str(y_30_10 * 100 / (y_30_10 + n_30_10)).split(".")[0])
per_30_10_s = 'BA in Education : ' + str(per_30_10_int) + "%"

per_30_11_int = int(str(y_30_11 * 100 / (y_30_11 + n_30_11)).split(".")[0])
per_30_11_s = 'Bachelor of Architecture : ' + str(per_30_11_int) + "%"

per_30_12_int = int(str(y_30_12 * 100 / (y_30_12 + n_30_12)).split(".")[0])
per_30_12_s = 'BA in Interior Architecture : ' + str(per_30_12_int) + "%"

per_30_13_int = int(str(y_30_13 * 100 / (y_30_13 + n_30_13)).split(".")[0])
per_30_13_s = 'BS in Economics : ' + str(per_30_13_int) + "%"

per_30_14_int = int(str(y_30_14 * 100 / (y_30_14 + n_30_14)).split(".")[0])
per_30_14_s = 'BS in Biology : ' + str(per_30_14_int) + "%"

per_30_15_int = int(str(y_30_15 * 100 / (y_30_15 + n_30_15)).split(".")[0])
per_30_15_s = 'BE in Computer Engineering : ' + str(per_30_15_int) + "%"

per_30_16_int = int(str(y_30_16 * 100 / (y_30_16 + n_30_16)).split(".")[0])
per_30_16_s = 'BE in Petroleum Engineering : ' + str(per_30_16_int) + "%"

per_30_17_int = int(str(y_30_17 * 100 / (y_30_17 + n_30_17)).split(".")[0])
per_30_17_s = 'BS in Hosp. & Tourism Manag. : ' + str(per_30_17_int) + "%"

per_30_18_int = int(str(y_30_18 * 100 / (y_30_18 + n_30_18)).split(".")[0])
per_30_18_s = 'BS in Computer Science : ' + str(per_30_18_int) + "%"

per_30_19_int = int(str(y_30_19 * 100 / (y_30_19 + n_30_19)).split(".")[0])
per_30_19_s = 'BE in Mechanical Engineering : ' + str(per_30_19_int) + "%"

per_30_20_int = int(str(y_30_20 * 100 / (y_30_20 + n_30_20)).split(".")[0])
per_30_20_s = 'BA in Performing Arts : ' + str(per_30_20_int) + "%"

per_30_21_int = int(str(y_30_21 * 100 / (y_30_21 + n_30_21)).split(".")[0])
per_30_21_s = 'BS in Nutrition : ' + str(per_30_21_int) + "%"

per_30_22_int = int(str(y_30_22 * 100 / (y_30_22 + n_30_22)).split(".")[0])
per_30_22_s = 'BA in Political Sc/Int.Affairs : ' + str(per_30_22_int) + "%"

per_30_23_int = int(str(y_30_23 * 100 / (y_30_23 + n_30_23)).split(".")[0])
per_30_23_s = 'BE in Industrial Engineering : ' + str(per_30_23_int) + "%"

per_30_24_int = int(str(y_30_24 * 100 / (y_30_24 + n_30_24)).split(".")[0])
per_30_24_s = 'BA in Multimedia Journalism : ' + str(per_30_24_int) + "%"

per_30_25_int = int(str(y_30_25 * 100 / (y_30_25 + n_30_25)).split(".")[0])
per_30_25_s = 'BS in Nutr.&Diet. Coord. Prog. : ' + str(per_30_25_int) + "%"

per_30_26_int = int(str(y_30_26 * 100 / (y_30_26 + n_30_26)).split(".")[0])
per_30_26_s = 'BA in Social Work : ' + str(per_30_26_int) + "%"

per_30_27_int = int(str(y_30_27 * 100 / (y_30_27 + n_30_27)).split(".")[0])
per_30_27_s = 'BS in Chemistry : ' + str(per_30_27_int) + "%"

per_30_28_int = int(str(y_30_28 * 100 / (y_30_28 + n_30_28)).split(".")[0])
per_30_28_s = 'BA in Communication Arts : ' + str(per_30_28_int) + "%"

per_30_29_int = int(str(y_30_29 * 100 / (y_30_29 + n_30_29)).split(".")[0])
per_30_29_s = 'Teaching Diploma : ' + str(per_30_29_int) + "%"

per_30_30_int = int(str(y_30_30 * 100 / (y_30_30 + n_30_30)).split(".")[0])
per_30_30_s = 'Dip.in Learn. Dis.& Giftedness : ' + str(per_30_30_int) + "%"

per_30_31_int = int(str(y_30_31 * 100 / (y_30_31 + n_30_31)).split(".")[0])
per_30_31_s = 'BS in Pharmacy : ' + str(per_30_31_int) + "%"

per_30_32_int = int(str(y_30_32 * 100 / (y_30_32 + n_30_32)).split(".")[0])
per_30_32_s = 'BS in Nursing : ' + str(per_30_32_int) + "%"

per_30_33_int = int(str(y_30_33 * 100 / (y_30_33 + n_30_33)).split(".")[0])
per_30_33_s = 'BA in Translation : ' + str(per_30_33_int) + "%"

per_30_34_int = int(str(y_30_34 * 100 / (y_30_34 + n_30_34)).split(".")[0])
per_30_34_s = 'BS in Graphic Design : ' + str(per_30_34_int) + "%"

final_30_prog_sort = [per_30_1_s , per_30_2_s , per_30_3_s , per_30_4_s , per_30_5_s , per_30_6_s , per_30_7_s , per_30_8_s , per_30_9_s , per_30_10_s , per_30_11_s , per_30_12_s , per_30_13_s , per_30_14_s , per_30_15_s , per_30_16_s , per_30_17_s , per_30_18_s ,
per_30_19_s , per_30_20_s , per_30_21_s , per_30_22_s , per_30_23_s , per_30_24_s , per_30_25_s , per_30_26_s , per_30_27_s ,
per_30_28_s , per_30_29_s , per_30_30_s , per_30_31_s , per_30_32_s , per_30_33_s , per_30_34_s]

final_30_intern_sort = [per_30_1_int , per_30_2_int , per_30_3_int , per_30_4_int , per_30_5_int , per_30_6_int , per_30_7_int , per_30_8_int , per_30_9_int , per_30_10_int , per_30_11_int , per_30_12_int , per_30_13_int , per_30_14_int , per_30_15_int , per_30_16_int , per_30_17_int , per_30_18_int ,
per_30_19_int , per_30_20_int , per_30_21_int , per_30_22_int , per_30_23_int , per_30_24_int , per_30_25_int , per_30_26_int , per_30_27_int ,
per_30_28_int , per_30_29_int , per_30_30_int , per_30_31_int , per_30_32_int , per_30_33_int , per_30_34_int]

# print(final_30_prog_sort)
# print(final_30_intern_sort)

# remove 0%
for sort_i in range(len(final_30_intern_sort) - 1, -1, -1):
    if final_30_intern_sort[sort_i] == 0:
        del final_30_intern_sort[sort_i]
        del final_30_prog_sort[sort_i]

fig30_newdf = pd.DataFrame({'Program':final_30_prog_sort,'INTERNSHIP BY DEGREE':final_30_intern_sort})
fig30_sort = fig30_newdf.sort_values('INTERNSHIP BY DEGREE',ascending=True)
fig_30 = fig30_sort.plot.barh(x='Program', y='INTERNSHIP BY DEGREE')
plt.xticks(rotation=30,fontsize=10)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('fig30.jpg',bbox_inches='tight')

# FIGURE 33 ALUMNI WHO BELIEVED THEY WERE SUFFICIENTLY PREPARED TO OBTAIN FIRST JOB BY GENDERFIGURE 33 ALUMNI WHO BELIEVED THEY WERE SUFFICIENTLY PREPARED TO OBTAIN FIRST JOB BY GENDER

fig_33_gend = df['Gender'].to_list()
fig_33_objob = df["Q47_Were you sufficiently prepared at LAU to obtain your first job?_Were you sufficiently prepared at LAU to obtain your first job?"].to_list()

fig_33_gend_nw = []
fig_33_objob_nw = []
for fig_33_i in range(0,len(fig_33_objob)):
    if fig_33_objob[fig_33_i] != 'D/A':
        fig_33_gend_nw.append(fig_33_gend[fig_33_i])
        fig_33_objob_nw.append(fig_33_objob[fig_33_i])

df_33_tmp = pd.DataFrame({"Gender":fig_33_gend_nw,"obtain_job":fig_33_objob_nw})
# df_33_tmp.to_excel("33.xlsx")

f_33_y = 0
m_33_y = 0
f_33_n = 0
m_33_n = 0
for yn_33_i in range(0,len(fig_33_objob_nw)):
    if fig_33_gend_nw[yn_33_i] == 'Female' and fig_33_objob_nw[yn_33_i] == 'Yes':
        f_33_y += 1
    if fig_33_gend_nw[yn_33_i] == 'Female' and fig_33_objob_nw[yn_33_i] == 'No':
        f_33_n += 1
    if fig_33_gend_nw[yn_33_i] == 'Male' and fig_33_objob_nw[yn_33_i] == 'Yes':
        m_33_y += 1
    if fig_33_gend_nw[yn_33_i] == 'Male' and fig_33_objob_nw[yn_33_i] == 'No':
        m_33_n += 1

female_33 = int(str(f_33_y * 100 / (f_33_y + f_33_n)).split(".")[0])
female_33_s = "Female : " + str(female_33) + "%"
male_33 = int(str(m_33_y * 100 / (m_33_y + m_33_n)).split(".")[0])
male_33_s = "Male : " + str(male_33) + "%"

df_33_final = pd.DataFrame({"Gender":[female_33_s,male_33_s],"FIRST JOB BY GENDER":[female_33,male_33]})
fig_33_ax = sns.catplot(x="Gender", y="FIRST JOB BY GENDER", kind="bar", data=df_33_final)
plt.savefig('fig33.jpg')
plt.clf()

# https://stackoverflow.com/questions/16653815/horizontal-stacked-bar-chart-in-matplotlib
# https://stackoverflow.com/questions/21397549/stack-bar-plot-in-matplotlib-and-add-label-to-each-section-and-suggestions

# FIGURE 36 LAU’S CONTRIBUTION TO ACQUISITION OF SKILLS BY ALUMNI

fig_36_tm = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Functioning as a team member'].to_list()
fig_36_tcrit = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Ability to think critically and approach new problems with an open and analytical mind'].to_list()
fig_36_oral= df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Developing oral communication skills'].to_list()
fig_36_writ = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Developing written communication skills']
fig_36_learn = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Instilling commitment for life-long learning'].to_list()
fig_36_eissue = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Becoming aware of ethical issues inherent in your discipline'].to_list()
fig_36_mlead = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Developing management/leadership capacities'].to_list()
fig_36_tskill =df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Acquiring theoretical skills to pursue a career path or post bachelor education related to your major field of study'].to_list()
fig_36_lsissue = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Becoming aware of  legal and social issues inherent in your discipline'].to_list()
fig_36_mtech = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Using effectively modern technology'].to_list()
fig_36_pursu = df['Q50_To what extent do you think your LAU education contributed to the acquisition of knowledge, skills, and development in each of the following areas?_Acquiring technical skills to pursue a career path post bachelor education related to your major field of study'].to_list()

def filter_da_36(list_36,list_36_nw):
    for i_36 in range(0,len(list_36)):
        if list_36[i_36] != 'D/A':
            list_36_nw.append(list_36[i_36])

fig_36_tm_nw = []
fig_36_tcrit_nw = []
fig_36_oral_nw = []
fig_36_writ_nw = []
fig_36_learn_nw = []
filter_da_36_nw = []
fig_36_eissue_nw = []
fig_36_mlead_nw = []
fig_36_tskill_nw = []
fig_36_lsissue_nw = []
fig_36_mtech_nw = []
fig_36_pursu_nw = []

filter_da_36(fig_36_tm,fig_36_tm_nw)
filter_da_36(fig_36_tcrit,fig_36_tcrit_nw)
filter_da_36(fig_36_oral,fig_36_oral_nw)
filter_da_36(fig_36_writ,fig_36_writ_nw)
filter_da_36(fig_36_learn,fig_36_learn_nw)
filter_da_36(fig_36_eissue,fig_36_eissue_nw)
filter_da_36(fig_36_mlead,fig_36_mlead_nw)
filter_da_36(fig_36_tskill,fig_36_tskill_nw)
filter_da_36(fig_36_lsissue,fig_36_lsissue_nw)
filter_da_36(fig_36_mtech,fig_36_mtech_nw)
filter_da_36(fig_36_pursu,fig_36_pursu_nw)

c_36_1_1 = fig_36_tm_nw.count('Major contribution')
c_36_1_2 = fig_36_tm_nw.count('Strong contribution')
c_36_1_3 = fig_36_tm_nw.count('Moderate contribution')
c_36_1_4 = fig_36_tm_nw.count('Minor contribution')

s_36_1 = c_36_1_1 + c_36_1_2 + c_36_1_3 + c_36_1_4

c_36_1_1_p = int(str(round(c_36_1_1 * 100 / s_36_1)).split(".")[0])
c_36_1_1_s = str(c_36_1_1_p)
c_36_1_2_p = int(str(round(c_36_1_2 * 100 / s_36_1)).split(".")[0])
c_36_1_2_s = str(c_36_1_2_p)
c_36_1_3_p = int(str(round(c_36_1_3 * 100 / s_36_1)).split(".")[0])
c_36_1_3_s = str(c_36_1_3_p)
c_36_1_4_p = int(str(round(c_36_1_4 * 100 / s_36_1)).split(".")[0])
c_36_1_4_s = str(c_36_1_4_p)

c_36_2_1 = fig_36_tcrit_nw.count('Major contribution')
c_36_2_2 = fig_36_tcrit_nw.count('Strong contribution')
c_36_2_3 = fig_36_tcrit_nw.count('Moderate contribution')
c_36_2_4 = fig_36_tcrit_nw.count('Minor contribution')

s_36_2 = c_36_2_1 + c_36_2_2 + c_36_2_3 + c_36_2_4

c_36_2_1_p = int(str(round(c_36_2_1 * 100 / s_36_2)).split(".")[0])
c_36_2_1_s = str(c_36_2_1_p)
c_36_2_2_p = int(str(round(c_36_2_2 * 100 / s_36_2)).split(".")[0])
c_36_2_2_s = str(c_36_2_2_p)
c_36_2_3_p = int(str(round(c_36_2_3 * 100 / s_36_2)).split(".")[0])
c_36_2_3_s = str(c_36_2_3_p)
c_36_2_4_p = int(str(round(c_36_2_4 * 100 / s_36_2)).split(".")[0])
c_36_2_4_s = str(c_36_2_4_p)

c_36_3_1 = fig_36_oral_nw.count('Major contribution')
c_36_3_2 = fig_36_oral_nw.count('Strong contribution')
c_36_3_3 = fig_36_oral_nw.count('Moderate contribution')
c_36_3_4 = fig_36_oral_nw.count('Minor contribution')

s_36_3 = c_36_3_1 + c_36_3_2 + c_36_3_3 + c_36_3_4

c_36_3_1_p = int(str(round(c_36_3_1 * 100 / s_36_3)).split(".")[0])
c_36_3_1_s = str(c_36_3_1_p)
c_36_3_2_p = int(str(round(c_36_3_2 * 100 / s_36_3)).split(".")[0])
c_36_3_2_s = str(c_36_3_2_p)
c_36_3_3_p = int(str(round(c_36_3_3 * 100 / s_36_3)).split(".")[0])
c_36_3_3_s = str(c_36_3_3_p)
c_36_3_4_p = int(str(round(c_36_3_4 * 100 / s_36_3)).split(".")[0])
c_36_3_4_s = str(c_36_3_4_p)

c_36_4_1 = fig_36_writ_nw.count('Major contribution')
c_36_4_2 = fig_36_writ_nw.count('Strong contribution')
c_36_4_3 = fig_36_writ_nw.count('Moderate contribution')
c_36_4_4 = fig_36_writ_nw.count('Minor contribution')

s_36_4 = c_36_4_1 + c_36_4_2 + c_36_4_3 + c_36_4_4

c_36_4_1_p = int(str(round(c_36_4_1 * 100 / s_36_4)).split(".")[0])
c_36_4_1_s = str(c_36_4_1_p)
c_36_4_2_p = int(str(round(c_36_4_2 * 100 / s_36_4)).split(".")[0])
c_36_4_2_s = str(c_36_4_2_p)
c_36_4_3_p = int(str(round(c_36_4_3 * 100 / s_36_4)).split(".")[0])
c_36_4_3_s = str(c_36_4_3_p)
c_36_4_4_p = int(str(round(c_36_4_4 * 100 / s_36_4)).split(".")[0])
c_36_4_4_s = str(c_36_4_4_p)

c_36_5_1 = fig_36_learn_nw.count('Major contribution')
c_36_5_2 = fig_36_learn_nw.count('Strong contribution')
c_36_5_3 = fig_36_learn_nw.count('Moderate contribution')
c_36_5_4 = fig_36_learn_nw.count('Minor contribution')

s_36_5 = c_36_5_1 + c_36_5_2 + c_36_5_3 + c_36_5_4

c_36_5_1_p = int(str(round(c_36_5_1 * 100 / s_36_5)).split(".")[0])
c_36_5_1_s = str(c_36_5_1_p)
c_36_5_2_p = int(str(round(c_36_5_2 * 100 / s_36_5)).split(".")[0])
c_36_5_2_s = str(c_36_5_2_p)
c_36_5_3_p = int(str(round(c_36_5_3 * 100 / s_36_5)).split(".")[0])
c_36_5_3_s = str(c_36_5_3_p)
c_36_5_4_p = int(str(round(c_36_5_4 * 100 / s_36_5)).split(".")[0])
c_36_5_4_s = str(c_36_5_4_p)

c_36_6_1 = fig_36_eissue_nw.count('Major contribution')
c_36_6_2 = fig_36_eissue_nw.count('Strong contribution')
c_36_6_3 = fig_36_eissue_nw.count('Moderate contribution')
c_36_6_4 = fig_36_eissue_nw.count('Minor contribution')

s_36_6 = c_36_5_1 + c_36_5_2 + c_36_5_3 + c_36_5_4

c_36_6_1_p = int(str(round(c_36_6_1 * 100 / s_36_6)).split(".")[0])
c_36_6_1_s = str(c_36_6_1_p)
c_36_6_2_p = int(str(round(c_36_6_2 * 100 / s_36_6)).split(".")[0])
c_36_6_2_s = str(c_36_6_2_p)
c_36_6_3_p = int(str(round(c_36_6_3 * 100 / s_36_6)).split(".")[0])
c_36_6_3_s = str(c_36_6_3_p)
c_36_6_4_p = int(str(round(c_36_6_4 * 100 / s_36_6)).split(".")[0])
c_36_6_4_s = str(c_36_6_4_p)

c_36_7_1 = fig_36_mlead_nw.count('Major contribution')
c_36_7_2 = fig_36_mlead_nw.count('Strong contribution')
c_36_7_3 = fig_36_mlead_nw.count('Moderate contribution')
c_36_7_4 = fig_36_mlead_nw.count('Minor contribution')

s_36_7 = c_36_7_1 + c_36_7_2 + c_36_7_3 + c_36_7_4

c_36_7_1_p = int(str(round(c_36_7_1 * 100 / s_36_7)).split(".")[0])
c_36_7_1_s = str(c_36_7_1_p)
c_36_7_2_p = int(str(round(c_36_7_2 * 100 / s_36_7)).split(".")[0])
c_36_7_2_s = str(c_36_7_2_p)
c_36_7_3_p = int(str(round(c_36_7_3 * 100 / s_36_7)).split(".")[0])
c_36_7_3_s = str(c_36_7_3_p)
c_36_7_4_p = int(str(round(c_36_7_4 * 100 / s_36_7)).split(".")[0])
c_36_7_4_s = str(c_36_7_4_p)

c_36_8_1 = fig_36_tskill_nw.count('Major contribution')
c_36_8_2 = fig_36_tskill_nw.count('Strong contribution')
c_36_8_3 = fig_36_tskill_nw.count('Moderate contribution')
c_36_8_4 = fig_36_tskill_nw.count('Minor contribution')

s_36_8 = c_36_8_1 + c_36_8_2 + c_36_8_3 + c_36_8_4

c_36_8_1_p = int(str(round(c_36_8_1 * 100 / s_36_8)).split(".")[0])
c_36_8_1_s = str(c_36_8_1_p)
c_36_8_2_p = int(str(round(c_36_8_2 * 100 / s_36_8)).split(".")[0])
c_36_8_2_s = str(c_36_8_2_p)
c_36_8_3_p = int(str(round(c_36_8_3 * 100 / s_36_8)).split(".")[0])
c_36_8_3_s = str(c_36_8_3_p)
c_36_8_4_p = int(str(round(c_36_8_4 * 100 / s_36_8)).split(".")[0])
c_36_8_4_s = str(c_36_8_4_p)

c_36_9_1 = fig_36_lsissue_nw.count('Major contribution')
c_36_9_2 = fig_36_lsissue_nw.count('Strong contribution')
c_36_9_3 = fig_36_lsissue_nw.count('Moderate contribution')
c_36_9_4 = fig_36_lsissue_nw.count('Minor contribution')

s_36_9 = c_36_9_1 + c_36_9_2 + c_36_9_3 + c_36_9_4

c_36_9_1_p = int(str(round(c_36_9_1 * 100 / s_36_9)).split(".")[0])
c_36_9_1_s = str(c_36_9_1_p)
c_36_9_2_p = int(str(round(c_36_9_2 * 100 / s_36_9)).split(".")[0])
c_36_9_2_s = str(c_36_9_2_p)
c_36_9_3_p = int(str(round(c_36_9_3 * 100 / s_36_9)).split(".")[0])
c_36_9_3_s = str(c_36_9_3_p)
c_36_9_4_p = int(str(round(c_36_9_4 * 100 / s_36_9)).split(".")[0])
c_36_9_4_s = str(c_36_9_4_p)

c_36_10_1 = fig_36_mtech_nw.count('Major contribution')
c_36_10_2 = fig_36_mtech_nw.count('Strong contribution')
c_36_10_3 = fig_36_mtech_nw.count('Moderate contribution')
c_36_10_4 = fig_36_mtech_nw.count('Minor contribution')

s_36_10 = c_36_10_1 + c_36_10_2 + c_36_10_3 + c_36_10_4

c_36_10_1_p = int(str(round(c_36_10_1 * 100 / s_36_10)).split(".")[0])
c_36_10_1_s = str(c_36_10_1_p)
c_36_10_2_p = int(str(round(c_36_10_2 * 100 / s_36_10)).split(".")[0])
c_36_10_2_s = str(c_36_10_2_p)
c_36_10_3_p = int(str(round(c_36_10_3 * 100 / s_36_10)).split(".")[0])
c_36_10_3_s = str(c_36_10_3_p)
c_36_10_4_p = int(str(round(c_36_10_4 * 100 / s_36_10)).split(".")[0])
c_36_10_4_s = str(c_36_10_4_p)

c_36_11_1 = fig_36_pursu_nw.count('Major contribution')
c_36_11_2 = fig_36_pursu_nw.count('Strong contribution')
c_36_11_3 = fig_36_pursu_nw.count('Moderate contribution')
c_36_11_4 = fig_36_pursu_nw.count('Minor contribution')

s_36_11 = c_36_11_1 + c_36_11_2 + c_36_11_3 + c_36_11_4

c_36_11_1_p = int(str(round(c_36_11_1 * 100 / s_36_11)).split(".")[0])
c_36_11_1_s = str(c_36_11_1_p)
c_36_11_2_p = int(str(round(c_36_11_2 * 100 / s_36_11)).split(".")[0])
c_36_11_2_s = str(c_36_11_2_p)
c_36_11_3_p = int(str(round(c_36_11_3 * 100 / s_36_11)).split(".")[0])
c_36_11_3_s = str(c_36_11_3_p)
c_36_11_4_p = int(str(round(c_36_11_4 * 100 / s_36_11)).split(".")[0])
c_36_11_4_s = str(c_36_11_4_p)

# print(c_36_1_1_p,c_36_1_2_p,c_36_1_3_p,c_36_1_4_p)
# print(c_36_2_1_p,c_36_2_2_p,c_36_2_3_p,c_36_2_4_p)
# print(c_36_3_1_p,c_36_3_2_p,c_36_3_3_p,c_36_3_4_p)
# print(c_36_4_1_p,c_36_4_2_p,c_36_4_3_p,c_36_4_4_p)
# print(c_36_5_1_p,c_36_5_2_p,c_36_5_3_p,c_36_5_4_p)
# print(c_36_6_1_p,c_36_6_2_p,c_36_6_3_p,c_36_6_4_p)
# print(c_36_7_1_p,c_36_7_2_p,c_36_7_3_p,c_36_7_4_p)
# print(c_36_8_1_p,c_36_8_2_p,c_36_8_3_p,c_36_8_4_p)
# print(c_36_9_1_p,c_36_9_2_p,c_36_9_3_p,c_36_9_4_p)
# print(c_36_10_1_p,c_36_10_2_p,c_36_10_3_p,c_36_10_4_p)
# print(c_36_11_1_p,c_36_11_2_p,c_36_11_3_p,c_36_11_4_p)

label_36_1 = 'Functioning as a team member'
label_36_2 = 'Ability to think critically and approach new problems with an open and analytical mind'
label_36_3 = 'Developing oral communication skills'
label_36_4 = 'Developing written communication skills'
label_36_5 = 'Instilling commitment for life-long learning'
label_36_6 = 'Becoming aware of ethical issues inherent in your discipline'
label_36_7 = 'Acquiring theoretical skills to pursue a career path or post bachelor education related to your major field of study'
label_36_8 = 'Becoming aware of  legal and social issues inherent in your discipline'
label_36_9 = 'Developing management/leadership capacities'
label_36_10 = 'Using effectively modern technology'
label_36_11 = 'Acquiring technical skills to pursue a career path post bachelor education related to your major field of study'

label_36_int_1 = [c_36_1_1_p,c_36_1_2_p,c_36_1_3_p,c_36_1_4_p]
label_36_int_2 = [c_36_2_1_p,c_36_2_2_p,c_36_2_3_p,c_36_2_4_p]
label_36_int_3 = [c_36_3_1_p,c_36_3_2_p,c_36_3_3_p,c_36_3_4_p]
label_36_int_4 = [c_36_4_1_p,c_36_4_2_p,c_36_4_3_p,c_36_4_4_p]
label_36_int_5 = [c_36_5_1_p,c_36_5_2_p,c_36_5_3_p,c_36_5_4_p]
label_36_int_6 = [c_36_6_1_p,c_36_6_2_p,c_36_6_3_p,c_36_6_4_p]
label_36_int_7 = [c_36_7_1_p,c_36_7_2_p,c_36_7_3_p,c_36_7_4_p]
label_36_int_8 = [c_36_8_1_p,c_36_8_2_p,c_36_8_3_p,c_36_8_4_p]
label_36_int_9 = [c_36_9_1_p,c_36_9_2_p,c_36_9_3_p,c_36_9_4_p]
label_36_int_10 = [c_36_10_1_p,c_36_10_2_p,c_36_10_3_p,c_36_10_4_p]
label_36_int_11 = [c_36_11_1_p,c_36_11_2_p,c_36_11_3_p,c_36_11_4_p]

# some labels for each row
skills_36 = (label_36_11,label_36_10,label_36_9,label_36_8,label_36_7,label_36_6,label_36_5,label_36_4,label_36_3,label_36_2,label_36_1)
r = len(skills_36)
segments = 4
# generate some multi-dimensional data & arbitrary labels
data = 3 + 10* np.random.rand(segments, len(skills_36))
perlist_36 = (label_36_int_11,label_36_int_10,label_36_int_9,label_36_int_8,label_36_int_7,label_36_int_6,label_36_int_5,label_36_int_4,label_36_int_3,label_36_int_2,label_36_int_1)
percentages = np.array(perlist_36)
y_pos_36 = np.arange(len(skills_36))
fig_36 = plt.figure(figsize=(20,12))
ax_36 = fig_36.add_subplot(111)
colors ='bcgr'
patch_handles = []
left = np.zeros(len(skills_36)) # left alignment of data starts at zero
for i, d in enumerate(data):
    patch_handles.append(ax_36.barh(y_pos_36, d,
      color=colors[i%len(colors)], align='center',
      left=left))
    # accumulate the left-hand offsets
    left += d
# go through all of the bar segments and annotate
for j in range(len(patch_handles)):
    for i, patch in enumerate(patch_handles[j].get_children()):
        bl = patch.get_xy()
        x = 0.5*patch.get_width() + bl[0]
        y = 0.5*patch.get_height() + bl[1]
        ax_36.text(x,y, "%d%%" % (percentages[i,j]), ha='center')

ax_36.set_yticks(y_pos_36)
ax_36.set_yticklabels(skills_36)
ax_36.set_xlabel('LAU’S CONTRIBUTION TO ACQUISITION OF SKILLS BY ALUMNI')
plt.yticks(rotation=60,fontsize=9)
plt.legend(['Major contribution','Strong contribution','Minor contribution','Moderate contribution'],loc='best')
plt.tight_layout()
plt.savefig('fig36.jpg')
plt.clf()