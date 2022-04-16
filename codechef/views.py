import json
from django.shortcuts import render
import requests
import pandas as pd

# Create your views here.
def display_data_codechef(request):

    #HTTP Request

    s = requests.session()
    url_codechef='https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=premium'
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    data={
        "searchCondition":
        {
            "limit":100,
            "offset":0,
            "language":"en",
            "dataType":"new"
        }
    }

    req=s.get(url_codechef,headers=headers,json=data)

    #Raw .json file

    codechef_data =req.json()

    codechef_contest_code = []
    codechef_contest_duration = []
    codechef_contest_end_date = []
    codechef_contest_name = []
    codechef_contest_start_date = []

    # Appending fields in lists

    for item in codechef_data['future_contests']:
        codechef_contest_code.append(item['contest_code'])
        codechef_contest_duration.append(item['contest_duration'])
        codechef_contest_end_date.append(item['contest_end_date'])
        codechef_contest_name.append(item['contest_name'])
        codechef_contest_start_date.append(item['contest_start_date'])

    codechef_contest_duration_hrs = [str(int(int(x)/60))+" hrs" for x in codechef_contest_duration] # Converting minutes to hours

    #Creating dataframe out of fields

    codechef_output = pd.DataFrame({'contest_code':codechef_contest_code,'contest_name':codechef_contest_name, 'contest_start_date':codechef_contest_start_date,'contest_end_date':codechef_contest_end_date,'contest_duration':codechef_contest_duration_hrs})

    # Writing final .json file

    with open('codechef_contest_data.json', 'w') as f:
        f.write(codechef_output.to_json(orient='records'))

    return(render(request,'codechef/index.html', {'data':json.load(open('codechef_contest_data.json'))}))


def display_data_codeforces(request):

    #HTTP Request
    s = requests.session()
    url_codeforces='https://codeforces.com/api/contest.list?gym=false'
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    data={
        "searchCondition":
        {
            "limit":100,
            "offset":0,
            "language":"en",
            "dataType":"new"
        }
    }

    req_codeforces = s.get(url_codeforces,headers=headers,json=data)

    #Raw .json file

    codeforces_data = req_codeforces.json()


    codeforces_contest_id = []
    codeforces_contest_name = []
    codeforces_contest_start_time = []
    codeforces_contest_registration_time = []
    codeforces_contest_duration = []
    codeforces_contest_type = []

    # Appending fields in lists

    for item in codeforces_data['result']:
        if item['phase'] == 'FINISHED':
            break
        codeforces_contest_id.append(item['id'])
        codeforces_contest_name.append(item['name'])
        codeforces_contest_start_time.append(abs(item['relativeTimeSeconds']))
        codeforces_contest_duration.append(item['durationSeconds'])
        codeforces_contest_type.append(item['type'])

    codeforces_contest_duration = [str(int(x/3600))+" hrs" for x in codeforces_contest_duration] # Converting minutes to hours

    #Conversion of seconds left (integer) into Date-Time format

    from datetime import datetime, timedelta
    import time

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    codeforces_contest_start_time = [(now + timedelta(seconds = n)).strftime("%d/%m/%Y %H:%M") for n in codeforces_contest_start_time]

    #Creating dataframe out of fields

    output_cf = pd.DataFrame({'codeforces_contest_id':codeforces_contest_id,'codeforces_contest_name':codeforces_contest_name, 'codeforces_contest_start_time':codeforces_contest_start_time,'codeforces_contest_duration':codeforces_contest_duration, 'codeforces_contest_type': codeforces_contest_type})

    #Writing final .json file

    with open('codeforces_contest_data.json', 'w') as f:
        f.write(output_cf.to_json(orient='records'))

    return(render(request,'codeforces/index.html', {'data':json.load(open('codeforces_contest_data.json'))}))