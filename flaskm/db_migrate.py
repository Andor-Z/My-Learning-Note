#!
import imp 
import os
from migrate.versioning import api 
from app import db 
from config import config 

DB_URI = config[os.getenv('FLASK_CONFIG') or 'default'].SQLALCHEMY_DATABASE_URI
MG_REPO = config[os.getenv('FLASK_CONFIG') or 'default'].SQLALCHEMY_MIGRATE_REPO

def create_mg():
    '''
    初始化数据迁移仓库
    '''
    if not os.path.exists(MG_REPO):
        api.create(MG_REPO, 'database respository')
        api.version_control(DB_URI, MG_REPO)
    else:
        api.version_control(DB_URI, MG_REPO, api.version(MG_REPO))


def migrate_db():
    migration = os.path.join(MG_REPO, 'versions', '%03d_migration.py' % (api.db_version(DB_URI, MG_REPO) + 1))
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(DB_URI, MG_REPO)
    exec(old_model, tmp_module.__dict__)
    script = api.make_update_script_for_model(DB_URI, MG_REPO, tmp_module.meta, db.metadata)
    # ?
    open(migration, 'wt').write(script)
    api.upgrade(DB_URI, MG_REPO)
    print('New migration saved as ' + migration)
    print('Current database version: ' + str(api.db_version(DB_URI, MG_REPO)))


def upgrade_db():
    api.upgrade(DB_URI, MG_REPO)
    print('Current database version: ' +  str(api.db_version(DB_URI, MG_REPO)))
    