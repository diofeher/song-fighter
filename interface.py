#!/usr/bin/env python
# encoding: utf-8
"""
interface.py

Created by Diogenes Herminio on 2010-07-21.
Copyright (c) 2010 All rights reserved.
"""

import os
from models import Song
from sqlalchemy.orm import sessionmaker
from base import engine
import random

def get_musics():
    Session = sessionmaker(bind=engine)
    session = Session()
    music_list = session.query(Song).all()
    random.shuffle(music_list)
    return tuple(music_list[:2])
    
def create_musics(path):
    Session = sessionmaker(bind=engine)
    session = Session()
    file_list = os.listdir(path)
    for filename in file_list:
        song = Song(filename) 
        session.add(song)
    session.commit()

def get_ranking():
    Session = sessionmaker(bind=engine)
    session = Session()
    ranking_list = session.query(Song).order_by('path').all()
    return ranking_list

def update_count(obj):
    Session = sessionmaker(bind=engine)
    session = Session()
    obj.update_count()
    session.add(obj)
    session.commit()