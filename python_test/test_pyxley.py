SELF = 0x01  # 查看和自己有关的费用条目
DEPT = 0x02  # 查看本部门的费用条目
ALL = 0x04   # 查看所有的费用条目
A = 0x80
a = 1
b = 3
c = 7




def can(p, permission):
    return  (p & permission) == permission

# print(c)
print(can(c,ALL ))