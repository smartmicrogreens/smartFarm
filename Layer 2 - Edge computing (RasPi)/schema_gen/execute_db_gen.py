
from sqlalchemy import MetaData, create_engine

meta = MetaData()
from mg_db_crop import *
from mg_db_units import *
engine = create_engine('sqlite:///microgreens.db', echo=True)

meta.create_all(engine, Base.metadata.tables.values(), checkfirst=True)