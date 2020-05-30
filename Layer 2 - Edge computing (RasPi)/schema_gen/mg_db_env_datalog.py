from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Float, Boolean, Sequence, MetaData, DateTime, Time

from base import Base

class tb_crop_types(Base):
    """ Datalogging table for inputing  """
    __tablename__ = 'crop_types'