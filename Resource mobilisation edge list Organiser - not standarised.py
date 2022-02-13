# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:51:51 2021

@author: Edvard August Eggen Sveum 
FU Berlin - 5501132
"""
import pandas as pd
 #import data sets 
df1 = pd.read_json('D:/OneDrive/Python/Social network/SEMIC EV Germany/json/json/organization.json')
df_time = pd.read_json('D:/OneDrive/Python/Social network/SEMIC EV Germany/json/json/project.json')
df_SPD = pd.read_excel('D:/OneDrive/Python/Octo scrape/ev semie test/CORDIS _ European Commission - funding semi ev.xlsx')
df_time = df_time.set_index('id')
actors = []
s = df1.shape

#clean the data obtained from Ocoparse 8, but this part is not generalised, 
#any attempt to use a new dataset must manully specefy the rows for missing values in the Info1 column

for i in range(df_SPD.shape[0]):
    df_SPD['Unnamed: 5'][i] = df_SPD['Project ID'][i][20:26]
df_SPD = df_SPD.dropna(axis = 0, how='any')


for i in range(df_SPD.shape[0]):
    if i in [406,407,408,409,410]:
        print('')
    else:
        df_SPD['col12'][i] = df_SPD['col12'][i].replace('€', '') 
        df_SPD['col12'][i] = df_SPD['col12'][i].replace(' ', '')
        df_SPD['col12'][i] = df_SPD['col12'][i].replace(',', '.')
for i in range(1180,1185):
        df_SPD['col12'][i] = df_SPD['col12'][i].replace('€', '') 
        df_SPD['col12'][i] = df_SPD['col12'][i].replace(' ', '')
        df_SPD['col12'][i] = df_SPD['col12'][i].replace(',', '.')
df_SPD.rename(columns = {'col12':'ECC'}, inplace=True)
df_SPD.rename(columns = {'Unnamed: 5':'ID'}, inplace=True)

dic_list = {} 
ID_list = []
for i in range(df_SPD.shape[0]):
    if i in [406,407,408,409,410]:
        pass
    else:
        if df_SPD['ID'][i] not in  ID_list:
            ID_list.append(df_SPD['ID'][i])
for ID in ID_list:
    temp = []
    for i in range(df_SPD.shape[0]):
        if i in [406,407,408,409,410]:
            print('')
        else:
            if df_SPD['ID'][i] == ID:
                temp_d = {}
                temp_d[df_SPD['Title'][i]] = df_SPD['ECC'][i]
                temp.append(temp_d)
    dic_list[ID] = temp
'''
The cleaning of the datasets from Cordis starts her and redefine df_1 into df_edge_resource which selects  only the name, projectID, ecContribution and totalCost columns.
'''

            #df.loc[df['Actor/ Partner'] == actor_list[j], actor_list[j]] = 0
df_time = df_time.reset_index()

df_edge_resource = df1[['name', 'projectID', 'ecContribution', 'totalCost']]
for i in range(df_edge_resource.shape[0]):
    if df_edge_resource['ecContribution'][i] == '':  
        for j in range(len(dic_list[str(df_edge_resource['projectID'][i])])):
            if dic_list[str(df_edge_resource['projectID'][i])][j] == df_edge_resource['name'][i]:
                df_edge_resource.at[i, 'ecContribution'] =(dic_list[[str(df_edge_resource['projectID'][i])][j][df_edge_resource['name'][i]]])
    elif df_edge_resource['totalCost'][i] == '':
        df_edge_resource.at[i, 'totalCost'] = (df_edge_resource['ecContribution'][i])
start = []
end = []

df_time = df_time.set_index('id')
for i in range(df_edge_resource.shape[0]):
    df_edge_resource.at[i, 'Funding Source'] = df_time['fundingScheme'][df_edge_resource['projectID'][i]]
    end.append(str(df_time['endDate'][[df_edge_resource['projectID'][i]]])[13:23])
    start.append(str(df_time['startDate'][[df_edge_resource['projectID'][i]]])[13:23])
df_edge_resource['endDate'] = end
df_edge_resource['startDate'] = start
drop_list = []
for i in range(df_edge_resource.shape[0]):
    if df_edge_resource['ecContribution'][i] == '' or df_edge_resource['totalCost'][i] == 0:
        drop_list.append(i)
df_edge_resource = df_edge_resource.drop(df_edge_resource.index[drop_list])

df_edge_resource = df_edge_resource.astype({'ecContribution':int,'totalCost': int})


A_to_P = df_edge_resource[['name', 'projectID','totalCost','endDate', 'startDate']]
A_to_P.rename( columns = {'name':'Source', 'projectID':'Target', 'totalCost':'Weight',  'startDate':'start date', 'endDate':'end date'}, inplace = True)
A_to_P.to_excel('Resource_edge_list_part1r.xlsx', index = True)

EU_to_A = df_edge_resource[['Funding Source','name','ecContribution', 'startDate','endDate']]
EU_to_A.rename( columns = {'Funding Source':'Source', 'name':'Target', 'ecContribution':'Weight',  'startDate':'start date', 'endDate':'end date'}, inplace = True)
EU_to_A.to_excel('Resource_edge_list_part2r.xlsx', index= True)

