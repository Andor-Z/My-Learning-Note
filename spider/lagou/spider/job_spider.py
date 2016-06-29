import os
import requests

lagou_url = 'http://www.lagou.com/jobs/positionAjax.json?'
headers = {'content-type':'application/json;charset=UTF-8'}
basedir = os.path.abspath(os.path.dirname(__file__))

# def get_job_list(jobname = None, city = None):
# jobname = None
# city = None
jobname = 'python'
city = '杭州'

num = 1
payload = {'first': 'false', 'pn': num, 'kd': jobname, 'city' : city}
r = requests.post(lagou_url, params=payload, headers=headers)
maxpagenum = int(r.json()['content']["positionResult"]["totalCount"] /  15) + 1 
for num in range(1, maxpagenum + 1):
    payload = {'first': 'false', 'pn': num, 'kd': jobname, 'city' : city}
    r = requests.post(lagou_url, params=payload, headers=headers)
    if r.status_code == 200:
        job_dict = r.json()['content']['positionResult']['result']
        print('正在爬取第 ' + str(num) + ' 页的数据...')
        # print(type(job_dict))
        print(job_dict[0])
        # for i in job_dict:
        #     print(i)


    #     filedir = os.path.join(basedir, jobname, (str(num) + '.json'))
    #     with open(filedir, 'wt', encoding='utf-8') as f:
    #         f.write(str(job_json))
    #         f.flush()
    #         f.close()
    # else:
    #     print('爬取第' + str(num) + '页出现错误')
