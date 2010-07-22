# -*- coding: utf-8 -*-
"""
    settings

    description

    @copyright: 2010 DiogenesAugusto <diofeher@gmail.com>
    @license: GNU GPL.
"""
from sqlalchemy import create_engine

engine = create_engine('sqlite:////tmp/banco.db', echo=True)
path = ''  #TODO: Move path to here