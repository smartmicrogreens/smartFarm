from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from tastehood_server.backend.databases import Base
from tastehood_server.backend.databases.metrics import EnvironmentData


class IotDevice(Base):
    """ Datalogging table for raw sensor data  """

    __tablename__ = 'iot_devices'

    ## --- Keys --- ##
    id = Column(String(128), primary_key=True, nullable=False,
                comment='A unique identification for the IoT device item, in the format <iot_id>/<index>, e.g.,'
                        '{"127.3.4./1"}')
    ## --- IoT Device information --- ##
    name = Column(String(64), nullable=False,
                  comment='Name of IOT device.')
    description = Column('description', String(128), nullable=False,
                         comment='Description of IoT device.')

    shelf = relationship('Shelf', back_populates='iot_devices')
    environment_data = relationship(EnvironmentData, foreign_keys=[], back_populates='iot_device')
