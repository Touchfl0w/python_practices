import subprocess
from collections import Counter
out_bytes = subprocess.check_output(['netstat','-a'])
out_text = out_bytes.decode('utf-8')
print(type(out_text))
print(out_text)

out_text = out_text.split()
wordcounter = Counter(out_text)
print(wordcounter.most_common(10))