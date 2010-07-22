#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Diogenes Herminio on 2010-07-21.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

from models import Song

from sqlalchemy import create_engine
engine = create_engine('sqlite:////tmp/banco.db', echo=True)

if __name__=="__main__":        
    metadata = Song.metadata
    metadata.create_all(engine)