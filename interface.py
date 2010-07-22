# -*- coding: utf-8 -*-
"""
    Player

    @copyright: 2010 Diogenes Augusto <diofeher@gmail.com>
    @license: GNU GPL.
"""

import os
from models import Song
from sqlalchemy.orm import sessionmaker
from settings import engine
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