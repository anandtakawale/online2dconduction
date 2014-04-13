from google.appengine.ext import db
from google.appengine.api import memcache
import logging

class Plot(db.Model):
    Tup = db.FloatProperty(required = True)
    Tleft = db.FloatProperty(required = True)
    Tright = db.FloatProperty(required = True)
    Tdown = db.FloatProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    image = db.TextProperty(required = True)
    user = db.UserProperty(required = True)
    

def recentPlots(update = False):
    key = 'recent'
    plots = memcache.get(key)
    if plots is None or update:
        logging.error("DB Query")
        plots = db.GqlQuery("SELECT * FROM Plot ORDER BY created DESC LIMIT 5")
        plots = list(plots)
        memcache.set(key, plots)
        logging.error("Added plot with key " + str(plots[0].key().id()))
    return plots
