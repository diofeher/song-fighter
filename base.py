# -*- coding: utf-8 -*-
"""
    Base

    @copyright: 2010 Diogenes Augusto <diofeher@gmail.com>
    @license: GNU GPL.
"""

from models import Song

from sqlalchemy import create_engine
engine = create_engine('sqlite:////tmp/banco.db', echo=True)

if __name__=="__main__":        
    metadata = Song.metadata
    metadata.create_all(engine)