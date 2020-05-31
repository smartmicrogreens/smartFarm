from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from tastehood_server.backend.databases import Base


class IotDevice(Base):
    """ Datalogging table for raw sensor data  """

    __tablename__ = 'iot_devices'

    ## --- Keys --- ##
    id = Column(String(128), primary_key=True, nullable=False,  comment='A unique identification for the IoT device.')

    ## --- IoT Device information --- ##
    name = Column(String(64), nullable=False,
                  comment='Name of IOT device.')
    description = Column('description', String(128), nullable=False,
                         comment='Description of IoT device.')

    slot_id = Column(Integer(), ForeignKey('slots.id'), nullable=True)
    slot = relationship('Slot', foreign_keys=[slot_id], back_populates='iot_devices')
    environment_data = relationship('EnvironmentData', foreign_keys=[], back_populates='iot_device')
