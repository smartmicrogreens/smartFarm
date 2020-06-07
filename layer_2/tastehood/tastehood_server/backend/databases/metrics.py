from sqlalchemy import Column, Integer, Float, TIMESTAMP, String, ForeignKey
from sqlalchemy.orm import relationship

from tastehood_server.backend.databases import Base


class EnvironmentData(Base):
    """ Datalogging table for raw environment and consumption sensor data  """

    __tablename__ = 'env_data'

    ## --- TIMESTAMP --- ##
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    iot_identification_id = Column(String(128), ForeignKey('iot_devices.id'),
                                   nullable=False)

    iot_device = relationship('IotDevice')
    ## --- TIMESTAMP --- ##
    date = Column('date', TIMESTAMP(), nullable=False,
                  comment='Timestamp with date and time of logged data.')

    ## --- Enviroment sensor data --- ##
    temperature = Column('temperature', Float(), nullable=False,
                         comment='Node temperature')
    humidity = Column('humidity', Float(), nullable=False,
                      comment='Node humidity')
    soil_moisture = Column('soil_moisture', Float(), nullable=False,
                           comment='soil_moisture')

    ## --- Consumption lvl sensor data --- ##
    water_consumption = Column('water_consumption', Float(),
                               comment='Water consumption in L/hour. ')
    energy_consumption = Column('energy_consumption', Float(),
                                comment='Energy consumption in Wh')
