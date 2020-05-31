from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, Time, Boolean, String, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from tastehood_server.databases.base import Base


class Node(Base):
    """Creates the table that will contain node(Container or what ever space you want) information."""

    __tablename__ = 'node'

    ## --- Keys --- ##
    id = Column(String(128), primary_key=True, nullable=False, comment='A unique identification for the node')
    ## --- Temperature and humidity Thresholds --- ##
    temperature_th = Column('temperature_threshold', Integer(), nullable=False,
                            comment='Over this threshold, core program will start cooling system. '
                                    'Default value should be 24.')
    humidity_th = Column('humidity_threshold', Integer(), nullable=False,
                         comment='Over this threshold, start mechanism to reduce humidity. '
                                 'Default value should be 40.')

    shelves = relationship('Shelf', back_populates='node')


class Shelf(Base):
    """ Creates the table that will contain information for each shelf as a unit """

    __tablename__ = 'shelf'
    id = Column(String(128), primary_key=True, nullable=False, comment='A unique identification for the shelf')
    ## --- Keys --- ##

    node_identification_id = Column(String(128), ForeignKey('node.id'),
                                    nullable=False)
    node = relationship('Node', back_populates='shelves')
    slots = relationship('Slot', back_populates='shelf')
    ## --- Light times --- ##
    sunrise_t = Column('sunrise_time', Time(), nullable=False,
                       comment='Time to turn on shelf light.')
    sunset_t = Column('sunset_time', Time(), nullable=False,
                      comment='Time to turn off shelf light..')

    ## --- Moisture Threshold --- ##
    soil_moisture_th = Column('soil_moisture_threshold', Integer(), nullable=False,
                              comment='This threshold will define when the irrigation system should act. '
                                      'Default value = .')


class Slot(Base):
    """Slits inside each shelf."""
    __tablename__ = 'slots'
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    shelf_id = Column(String(128), ForeignKey('shelf.id'), nullable=False)
    shelf = relationship('Shelf', back_populates='slots')
    index = Column(Integer(), nullable=False, comment='The column index of where in the shelf the slot is')
    available = Column(Boolean(), comment='Whether a given slot is available')
    iot_devices = relationship('IotDevice', back_populates='slot')


class Tray(Base):
    """ Main table containing information of the current crops being cultavated. It has valuable status data. """

    __tablename__ = 'trays'
    ## --- Keys --- ##
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)

    shelf_id = Column(String(128), nullable=False)
    slot_index = Column(Integer(), nullable=False)
    slot = relationship('Slot')
    __table_args__ = (ForeignKeyConstraint((shelf_id, slot_index),
                                           (Slot.shelf_id, Slot.index)),
                      {})
    crop_name = Column(String(128), ForeignKey('crop_types.crop_name'), nullable=False)
    crop = relationship('CropType', foreign_keys=[crop_name])

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
