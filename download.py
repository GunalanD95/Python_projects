import requests
import os

fp =  os.path.abspath(__file__)

BASE_DIR =  os.path.dirname(fp)
DOWNLADS = os.path.join(BASE_DIR,"downloads")

os.makedirs(DOWNLADS,exist_ok = True)

download_img_path = os.path.join(DOWNLADS,'1.jpg')

url = "https://images.daznservices.com/di/library/GOAL/67/64/lionel-messi-barcelona-2020-21_1epkbxe4akqa61alyadwopnzxn.jpg?t=-674771132&quality=100"


r = requests.get(url, stream = True)
r.raise_for_status()

with open(download_img_path,'wb') as f:
	f.write(r.content)



