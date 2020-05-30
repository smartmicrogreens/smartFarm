from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Float, Boolean, Sequence, MetaData, DateTime, Time, TIMESTAMP

from base import Base

class tb_iot_devices(Base):
    """ Datalogging table for raw sensor data  """

    __tablename__ = 'iot_devices'

    ## --- Keys --- ##
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)

    ## --- IoT Device information --- ##
    name = Column('name', String(64), nullable=False,
                                comment='Name of IOT device.')
    description = Column('description', String(128), nullable=False,
                                comment='Description of IoT device.')
    ip_address = Column('ip_address', String(16), nullable=False,
                                comment='Name of IOT device.')


