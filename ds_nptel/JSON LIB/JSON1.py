import json

#python to js
dic = {"fname":"alex", "age":"22", "job" : "developer"}
js = json.dumps(dic)
print(js)

#json to python
dic2 ='{"fname":"alex", "age":"22", "job" : "developer"}'
y = json.loads(dic2)
print(y)

#practise
print(json.dumps({"name":"john","age":30}))
print(json.dumps([11,12]))
print(json.dumps((20,30)))
print(json.dumps(True))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=1,separators=(".","=")))