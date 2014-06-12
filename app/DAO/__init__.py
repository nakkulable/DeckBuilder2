import ConfigParser
import os
from mongokit import Connection

__author__ = 'Davor Obilinovic'


configParser = ConfigParser.RawConfigParser()
root_dir = os.path.abspath(os.path.dirname(__file__))
configParser.read(root_dir+"/../../configuration.txt")

def get_connection():
    conn = Connection("localhost", 27017)
    dbauth = conn.Magic2.authenticate(configParser.get("Mongo","username"),configParser.get("Mongo","password"))
    return conn

mongo = get_connection()