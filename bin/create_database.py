# /usr/bin/env python2.6
# -*- coding: utf-8 -*-
"""
    Create DataBase

    @copyright: 2010 Diogenes Augusto <diofeher@gmail.com>
    @license: GNU GPL.
"""

from song_fighter.models import Song
import settings

if __name__=="__main__":        
    metadata = Song.metadata
    metadata.create_all(settings.engine)