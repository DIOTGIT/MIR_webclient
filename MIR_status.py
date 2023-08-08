import requests, json, csv
import logging as l

import streamlit as st

#http://172.22.141.60/api/v2.0.0/status

#curl -X GET "http://172.22.141.60/api/v2.0.0/status" -H "accept: application/json" -H "Authorization: Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA==" -H "Accept-Language: en_US"


ip = '172.22.141.60'
host = 'http://' + ip + '/api/v2.0.0/'

headers = {}
headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='

def send2charger():
    json = {}
    json['mission_id'] ="cdd35c73-e603-11ea-a47f-94c691189ac0" #Töltés1500
    post_misson = requests.post(host + 'mission_queue', json =  json, headers = headers)
    print(post_misson.status_code)

def delete_queue():
    del_mission = requests.delete(host + 'mission_queue', headers=headers)
    print(del_mission.status_code)

def get_status_uptime():
    mir_get_status = requests.get(host + 'status', headers=headers)
    jsondata = json.loads(mir_get_status.content)    
    #print(jsondata['uptime'])
    return jsondata['uptime']
    
    

while False:
    mir_get_status = requests.get(host + 'status', headers=headers)
    jsondata = json.loads(mir_get_status.content)

    file_name = r'.//a.csv'
    data_file = open(file_name, 'a', newline='')
    csv_writer = csv.writer(data_file, delimiter=';')

    if data_file.tell() == 0:
        header = jsondata.keys()
        csv_writer.writerow(header)

    csv_writer.writerow(jsondata.values())

    data_file.close()

