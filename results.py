import requests
import thread
import md5
from multiprocessing import Pool
import random
import os

# Define a function for the thread
def download_result(regno):
    id = str(md5.new(str(random.random())).hexdigest())[:26]
    reg = "ETAOECS"+str(regno).zfill(3)
    print reg,id
    headers = {"Cookie": "PHPSESSID="+id}
    data = {"regno": reg, 'sum': '111', 'id': '5659', 'sessionok': 'yes'}

    r = requests.post('http://61.0.254.181/CuPbhavan/res_newregentry.php', data=data, headers=headers)
    r = requests.post('http://61.0.254.181/CuPbhavan/rs_newcheck.php', headers=headers)
    r = requests.post('http://61.0.254.181/CuPbhavan/cubtech7/barch_res.php', headers=headers)

    with open("PDF/"+str(regno)+".pdf", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    print "Saved : "+reg

try:
    os.mkdir("PDF")
    p = Pool(10)
    p.map(download_result,range(1,70))
except Exception as e:
    print e.message