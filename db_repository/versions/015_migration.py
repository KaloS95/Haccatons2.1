from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('buyer_id', INTEGER),
    Column('order_id', INTEGER),
    Column('quantity', INTEGER),
    Column('seller_id', INTEGER),
    Column('buyer_accepted', BOOLEAN),
    Column('seller_accepted', BOOLEAN),
)

transition = Table('transition', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('buyer_id', Integer),
    Column('seller_id', Integer),
    Column('order_id', Integer),
    Column('quantity', Integer),
    Column('concluded', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()
    post_meta.tables['transition'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    post_meta.tables['transition'].drop()
