__author__ = 'tanuj'

from google.appengine.ext import ndb

class SwiftModel(ndb.Model):

    sourcename = ndb.StringProperty()
    RA = ndb.FloatProperty()
    Dec = ndb.FloatProperty()
    alternatename = ndb.StringProperty()
    sourcetype = ndb.StringProperty()
    Today = ndb.FloatProperty()
    Yesterday = ndb.FloatProperty()
    Tenday = ndb.FloatProperty()
    Mean = ndb.FloatProperty()
    Peak = ndb.FloatProperty()
    Days = ndb.IntegerProperty()
    Last_Day = ndb.IntegerProperty()
    user_interest = ndb.FloatProperty()
    sourcetype_full = ndb.StringProperty()