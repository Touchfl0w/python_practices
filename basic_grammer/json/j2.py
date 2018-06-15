import json
#json对象:key必须为双引号，数字不加引号
#这样的格式之所以被称为对象，是因为JS中对象是这样定义的

json_object = '{"name":"wakak","age":18}'
#对象类型的json字符串
json_str_object = '{"name":"wakak","age":18}'
r = json.loads(json_str_object)
print(type(r))
print(r)

#json数组:字符串必须使用双引号
json_array = ["hello","world",18]
#数组类型的json字符串
json_str_array = '["hello","world",18,true,null,1.3]'
r = json.loads(json_str_array)
print(type(r))
print(r)

#json数组嵌套json对象
#具体的json字符串,所以说，字符串是json的表现形式
json_str = '[{"name":"wakaka"},{"age":18},{"index":true}]'
r = json.loads(json_str)
print(type(r))
print(r)