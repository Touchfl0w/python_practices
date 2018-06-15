from random import randint
from collections import Counter

l = [randint(0,10) for _ in range(20)]
print(l)

countdict = Counter(l)
#countdict是一个类字典对象，因为Counter继承了内置Dict类，所以countdict拥有所有字典的方法！
#countdict还有新方法most_common
print(countdict)
#返回3个频率最高的单元，默认由高到低
print(countdict.most_common(3))