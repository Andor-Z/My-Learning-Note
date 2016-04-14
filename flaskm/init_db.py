
from app.models import Role, User, Post
from app import  db
def create_db():
    db.drop_all()
    db.create_all()
    Role.insert_roles()
    user_admin = User(email='zyfsta@outlook.com', password = '7852',username= 'admin', confirmed= True)
    user_mod = User(email='zyfsta@163.com', password = '7852',username= 'zhao', confirmed= True ,role = Role.query.filter_by(name = 'Moderator').first())
    user_1 = User(email='user1@andor.com', password = '7852',username= 'user1', confirmed= True,role = Role.query.filter_by(name = 'User').first())
    #post_1 = Post(body = "asdgjkjjksdjgkljsdkljgksdjgkjk", timestamp = '2016-04-07 12:03:27.544195', author = 'user1' )



    db.session.add_all([user_1, user_admin, user_mod])
    db.session.commit()
    User.generate_fake(100)
    Post.generate_fake(500)



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