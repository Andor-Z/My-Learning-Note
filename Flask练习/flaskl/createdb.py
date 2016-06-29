from hello import db, Role, User
db.create_all()
# db.drop_all()

admin_role = Role(name = 'Admin')
mod_role = Role(name = 'Moderator')
user_role = Role(name = 'User')

user_admin = User(username = 'admin', role = admin_role)
user_zhao = User(username = 'zhao', role = user_role)

db.session.add_all([admin_role, mod_role,user_role, user_admin, user_zhao ])
db.session.commit()

'''
db.session.rollback()
回滚，调用 db.session.rollback() 后，添加到数据库会话中的所有对象都会还原到它们在数据库时的状态。
'''