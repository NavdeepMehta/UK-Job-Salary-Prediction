import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'ContractTime':2, 'Category':9, 'SalaryRaw':21127})

print(r.json())