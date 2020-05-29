import request
from data_input import data_in

URL = "http://127.0.0.1:5000/predict"

# defining a params dict for the parameters to be sent to the API 
headers = {"content-Type":"application/json"} 
data = {"input":data_in}
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, headers = headers, json=data)

r.json()
