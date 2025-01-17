"""
Created on Wed Dec 22 17:48 2021
@author: pg
This is a database of all of the Principal components saved
"""

# Modules used
from PrincipalComponent import PrincipalComponent

class PrincipalComponentDB(object):
    """PCs database"""

    #Constructor
    def __init__(self):
        self.principalComponents = [] #List of principal components

    def addPC(self, originArray):
        """Creates and adds PC to the database"""
        self.principalComponents.append(PrincipalComponent(originArray))
