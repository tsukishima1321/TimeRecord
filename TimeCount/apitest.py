import requests

url="http://127.0.0.1:1096/api/"

print("1")

req={"method":"addRecord", 'timezone':"timezone_", 'classroom':"classroom_",'writer':"writer_"}
res=requests.post(url=url,data=req)
print(res.text)