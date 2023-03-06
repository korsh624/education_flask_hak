import requests
def readData():
    r=requests.get('https://reqres.in/api/users?per_page=12').json()
    print(r)
    return r['data']
data=readData()
print(data)