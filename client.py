# -*- coding: utf-8 -*-
"""
    Player

    @copyright: 2010 Diogenes Augusto <diofeher@gmail.com>
    @license: GNU GPL.
"""

from interface import get_musics, create_musics, update_count
from sqlalchemy.orm import sessionmaker
from base import engine
Session = sessionmaker(bind=engine)
session = Session()

if __name__=="__main__":
    create_musics('/home/flavio/devel/tw/musics')