import requests
import thread
from multiprocessing import Pool
import random
import os

def download_result(regno):
    reg = "ETAOECS"+str(regno).zfill(3)
    try:
        id = (str(random.random())[2:]*27)[:26]
        print reg,id
        headers = {"Cookie": "PHPSESSID="+id}
        data = {"regno": reg, 'sum': '111', 'id': '6021', 'sessionok': 'yes'}  #The id should be updated.

        r = requests.post('http://61.0.254.181/CuPbhavan/res_newregentry.php', data=data, headers=headers)
        r = requests.get('http://61.0.254.181/CuPbhavan/rs_newcheck.php', headers=headers)
        r = requests.get('http://61.0.254.181/CuPbhavan/cubtech7/btechcss_res.php', headers=headers)  #This URL might need to be updated

        with open("PDF/"+str(regno)+".pdf", 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
        print "Saved : "+reg
    except Exception as e:
        print e
        print "Failed : "+reg        

try:
    if not os.path.exists("PDF"):
        os.makedirs("PDF")
    rolls = list(set(range(1, 70)) - set(map(lambda x: int(x[:-4]), (os.listdir("PDF")))))
    print rolls
    p = Pool(20)
    p.map(download_result,rolls)
except Exception as e:
    print e.message