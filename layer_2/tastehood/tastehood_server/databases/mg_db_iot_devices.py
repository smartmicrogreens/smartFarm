from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from tastehood_server.databases.base import Base


class IotDevice(Base):
    """ Datalogging table for raw sensor data  """

    __tablename__ = 'iot_devices'

    ## --- Keys --- ##
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)

    ## --- IoT Device information --- ##
    name = Column('name', String(64), nullable=False,
                  comment='Name of IOT device.')
    description = Column('description', String(128), nullable=False,
                         comment='Description of IoT device.')
    identification_id = Column('identification_id', String(128), nullable=False,
                               comment='A unique identification for the IoT device.')

    slot_id = Column('slot_id', Integer(), ForeignKey('slots.id'), nullable=True)
    slot = relationship('Slot', foreign_keys=[slot_id], back_populates='iot_devices')
    environment_data = relationship('EnvironmentData', foreign_keys=[], back_populates='iot_device')
