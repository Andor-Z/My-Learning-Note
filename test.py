import re
 
p = re.compile(r'\d+')
for m in p.finditer('one1two2three5four4'):
    print (type(m.group()))
 
### output ###
# 1 2 3 4