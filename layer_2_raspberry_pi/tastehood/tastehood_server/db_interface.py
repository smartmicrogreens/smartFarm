#!python3
# -*- coding: utf-8 -*-
"""An interface for communicating with SQL database."""

import contextlib

from sqlalchemy import orm, create_engine

from tastehood_server.databases.base import Base
from tastehood_server.settings import DATABASE, DEBUG


def get_session(do_create=True):
    """
    A context manager for communication with SQL database. Automatically create all tables which dont currently exist
    when this function is envoked. Automatically commit changes to database and rollback if an error occurs.
    Example:

    >> with get_session() as session:
    >>      # do something with session

    :param do_create: whether to create tables if they don't exists, default True
    :return:
    """
    eng = create_engine(DATABASE, echo=DEBUG)
    if do_create:
        Base.metadata.create_all(eng)
    sm = orm.session.sessionmaker(eng)

    @contextlib.contextmanager
    def managed_sm():
        sess = sm()  # type: orm.session.Session
        try:
            yield sess
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    return managed_sm()
