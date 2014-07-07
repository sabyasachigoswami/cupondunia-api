import hashlib
import time
import requests
import json
base_url="http://staging.couponapitest.com/"       

ts=int(time.time())                      
ts = str(ts)							
partner_id = "15"						
partial_qs = "pi="+partner_id+"&ts="+ts+"&category_id=1"		
partner_api_key = "F6ED0CCB-61F3-C222-54D0-BA4748C788C2"		
checksum = hashlib.md5(partner_api_key+partial_qs).hexdigest()		
queryString = partial_qs+"&cs="+checksum							
selected_api_method = "coupons_by_category"								
api_call_url = base_url+"api/"+selected_api_method+"?"+queryString		
print api_call_url
x=requests.get(api_call_url)
x=x.json()
with open('categories.txt', 'w') as outfile:
  json.dump(x, outfile)

						

