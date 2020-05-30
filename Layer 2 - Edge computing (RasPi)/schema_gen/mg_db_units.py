from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Float, Boolean, Sequence, MetaData, DateTime, Time, create_engine
from base import Base
from sqlalchemy.orm import relationship


class tb_node(Base):
    """ Creates the table that will contain node(Container or what ever space you want) information """

    __tablename__ = 'node'

    ## --- Keys --- ##
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)

    ## --- Temperature and humidity Thresholds --- ##
    temperature_th = Column('temperature_threshold', Integer(), nullable=False,
                                comment='Over this threshold, core program will start cooling system. '
                                        'Default value should be 24.')
    humidity_th = Column('humidity_threshold', Integer(), nullable=False,
                                comment='Over this threshold, start mechanism to reduce humidity. '
                                        'Default value should be 40.')

class tb_shelf(Base):
    """ Creates the table that will contain information for each shelf as a unit """

    __tablename__ = 'shelf'

    ## --- Keys --- ##
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    id_node = Column('node_id', Integer(), ForeignKey('node.id'), nullable=False)

    ## --- Light times --- ##
    sunrise_t = Column('sunrise_time', Time(), nullable=False,
                     comment='Time to turn on shelf light.')
    sunset_t = Column('sunset_time', Time(), nullable=False,
                     comment='Time to turn off shelf light.')

    ## --- Moisture Threshold --- ##
    soil_moisture_th = Column('soil_moisture_threshold', Integer(), nullable=False,
                              comment='This threshold will define when the irrigation system should act. '
                                      'Default value = .')

class tb_trays(Base):
    """ Main table containing information of the current crops being cultavated. It has valuable status data. """

    __tablename__ = 'trays'
    ## --- Keys --- ##
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    shelf_id = Column('shelf_id', Integer(), ForeignKey('shelf.id'), nullable=False)
    crop_id = Column('crop_id', Integer(), ForeignKey('crop.id'), nullable=False)

    ## --- Dates --- ##
    grow_start_date = Column('grow_start_date', DateTime(), nullable=False,
                                        comment='Date the tray is inserted in the rack.')
    estimated_germination_date = Column('estimated_germination_date', DateTime(), nullable=False,
                                        comment='Date when germination is estimated to be over.')
    germination_end_date = Column('germination_end_date', DateTime(), nullable=False,
                                        comment='Actual date when tray was moved to next station.')
    estimated_harvest_date = Column('estimated_harvest_date', DateTime(), nullable=False,
                                        comment='Estimated date when crop can be harvested.')
    harvest_date = Column('harvest_date', DateTime(), nullable=False,
                                        comment='Actual date when crop was harvested.')

    ## --- Weights --- ##
    initial_tray_weight = Column('initial_tray_weight', Float(), nullable=False,
                                        comment='Tray weight before inserting in the rack. '
                                                'This should include only plastic tray and substrate, '
                                                'nothing else(No seeds also).')
    final_tray_weight = Column('final_tray_weight', Float(), nullable=False,
                                        comment='Tray weight right before harvesting. ')

    ## --- Cost and profit --- ##
    unit_cost = Column('unit_cost', Float(), nullable=False,
                                        comment='Total costs for growing one microgreens tray/unit.')
    unit_profit = Column('unit_profit', Float(), nullable=False,
                                        comment='Profit per tray/unit.')

