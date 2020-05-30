from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Float, Boolean, Sequence, MetaData, DateTime, Time, TIMESTAMP

from base import Base

class tb_env_data(Base):
    """ Datalogging table for raw sensor data  """

    __tablename__ = 'env_data'

    date = Column('date', TIMESTAMP(), nullable=False,
                  comment='Timestamp with date and time of logged data.')
    temperature = Column('temperature', Integer(), nullable=False,
                         comment='Node temperature')
    humidity = Column('humidity', Integer(), nullable=False,
                      comment='Node humidity')
    soil_moisture = Column('soil_moisture', Integer(), nullable=False,
                           comment='soil_moisture')
    water_consumption = Column('water_consumption', Float(),
                               comment='Water consumption in L/hour. ')
    energy_consumption = Column('energy_consumption', Float(),
                                comment='Energy consumption in Wh')