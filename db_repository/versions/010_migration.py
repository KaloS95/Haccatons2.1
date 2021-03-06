from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
transition = Table('transition', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('buyer_id', Integer),
    Column('seller_id', Integer),
    Column('order_id', Integer),
    Column('quantity', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['transition'].columns['buyer_id'].create()
    post_meta.tables['transition'].columns['order_id'].create()
    post_meta.tables['transition'].columns['quantity'].create()
    post_meta.tables['transition'].columns['seller_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['transition'].columns['buyer_id'].drop()
    post_meta.tables['transition'].columns['order_id'].drop()
    post_meta.tables['transition'].columns['quantity'].drop()
    post_meta.tables['transition'].columns['seller_id'].drop()
