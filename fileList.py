# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 00:29:25 2022

@author: FM

Globals file, prevents them from being initialised more than once, but can be used among different files
"""
def init():
    global List
    List = []
    global File
    File = None
    global method
    method = 0