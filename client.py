#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by Diogenes Herminio on 2010-07-21.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from interface import get_musics, create_musics, update_count
from sqlalchemy.orm import sessionmaker
from base import engine
Session = sessionmaker(bind=engine)
session = Session()

if __name__=="__main__":
    create_musics('/home/flavio/devel/tw/musics')