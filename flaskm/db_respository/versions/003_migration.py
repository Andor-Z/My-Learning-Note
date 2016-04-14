from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
alembic_version = Table('alembic_version', pre_meta,
    Column('version_num', VARCHAR(length=32), nullable=False),
)

users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('location', String(length=64)),
    Column('about_me', Text),
    Column('member_since', DateTime, default=ColumnDefault(<function ColumnDefault._maybe_wrap_callable.<locals>.<lambda> at 0x000000000347CAE8>)),
    Column('last_seen', DateTime, default=ColumnDefault(<function ColumnDefault._maybe_wrap_callable.<locals>.<lambda> at 0x0000000004CDF268>)),
    Column('email', String(length=64)),
    Column('username', String(length=64)),
    Column('role_id', Integer),
    Column('password_hash', String(length=128)),
    Column('confirmed', Boolean, default=ColumnDefault(False)),
    Column('avatar_hash', String(length=32)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alembic_version'].drop()
    post_meta.tables['users'].columns['avatar_hash'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alembic_version'].create()
    post_meta.tables['users'].columns['avatar_hash'].drop()
