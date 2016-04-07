
from app.models import Role, User 
from app import  db
db.drop_all()
db.create_all()
'''
# 创建角色
role_admin = Role(name = 'Administrator')
role_mod = Role(name = 'Moderator')
role_user = Role(name = 'User')

user_admin = User(email='zyfsta@163.com', password = '7852',username= 'zhao')
user_susan = User(username = 'susan')
user_david = User(username = 'david', role = role_user)

db.session.add_all([role_admin, role_mod, role_user, user_david, user_susan,user_zhao])

db.session.commit()

#print(role_admin.id)


user_1 = User(email='user1@andor.com', password = '7852',username= 'user1',role = Role.query.)
db.session.add(user_1)
db.session.commit()
'''