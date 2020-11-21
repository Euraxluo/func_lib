import requests
x = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
print(requests.post(url="http://localhost:5000/service/xixixi/mimimi/base", json=x).text)


data = {
    "arr":[1,4,5,2,41,4,24,5]
}
print(requests.post(url="http://localhost:5000/service/sort/quickSort/base", json=data).text)