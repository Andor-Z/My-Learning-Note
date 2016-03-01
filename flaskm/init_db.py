
from app.models import Role, User 
from app import  db
#db.drop_all()
db.create_all()

# 创建角色
role_admin = Role(name = 'Admin')
role_mod = Role(name = 'Moderator')
role_user = Role(name = 'User')

user_zhao = User(email='zyfsta@163.com', password = 'zhao',username= 'zhao', role = role_admin)
user_susan = User(username = 'susan', role = role_mod)
user_david = User(username = 'david', role = role_user)

db.session.add_all([role_admin, role_mod, role_user, user_david, user_susan,user_zhao])

db.session.commit()

#print(role_admin.id)