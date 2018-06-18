import json

json_string = '[1,2,"abc",{"hello":3,"world":2}]'
python_obj = json.loads(json_string)
print(python_obj)
print(type(python_obj))

python_obj = {'hello':[1,2,3],'works':18}
json_string = json.dumps(python_obj)
print(json_string)
print(type(json_string))