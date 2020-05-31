from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from tastehood_server.databases.base import Base


class CropType(Base):
    """Table containing different crop types and key information about them."""
    __tablename__ = 'crop_types'

    ## --- Keys --- ##
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    tray = relationship('Tray', back_populates='crop')
    ## --- Crop names --- ##
    crop_name = Column('crop_name', String(64), nullable=False,
                       comment='Date the tray is inserted in the rack.')

    ## --- Preferred media --- ##
    preferred_media = Column('preferred_media', String(64), nullable=False,
                             comment='Media type preferred by the crop for maximize growing.')

    ## --- Seeding density --- ##
    seeding_density = Column('seeding_density', Float(), nullable=False,
                             comment='Density (gram/cm2): Defines amount of seeds per cm2')

    ## --- Booleans --- ##
    pre_soak = Column('pre_soak', Boolean(), nullable=False,
                      comment='Is pre-soak required or not condition')
    blackout = Column('blackout', Boolean(), nullable=False,
                      comment='Is blackout required or not condition')

    ## --- Variable times (Days / hours) --- ##
    pre_soak_time = Column('pre_soak_time', Integer(), nullable=False,
                           comment='Time in HOURS of soaking')
    germination_time = Column('germination_time', Integer(), nullable=False,
                              comment='Total DAYS for completing germination stage')
    blackout_time = Column('blackout_time', Integer(), nullable=False,
                           comment='Total DAYS crop needs to be away from any light source')
    harvest_time = Column('harvest_time', Integer(), nullable=False,
                          comment='Total DAYS for harvesting')

    ## --- Costs and stock --- ##
    kilogram_cost = Column('kilogram_cost', Integer(), nullable=False,
                           comment='Cost per kilogram of seeds')
    kilograms_available = Column('kilograms_available', Integer(), nullable=False,
                                 comment='Kilograms available in stock')
