__author__ = 'tanuj'


class SwiftItem(object):

    def __init__(self):

        self.sourcename = None
        self.RA	= None
        self.Dec = None
        self.alternatename = None
        self.sourcetype = None
        self.Today = None
        self.Yesterday = None
        self.Tenday = None
        self.Mean = None
        self.Peak = None
        self.Days = None
        self.Last_Day = None

        #introduced artificially:
        self.sourcetype_full = None
        self.user_interest= None

    def __str__(self):
        return str(self.sourcename) +" "+str(self.RA)+" "+ str(self.Dec)+" "+ str(self.alternatename)+" "+str(self.sourcetype)+" "+ str(self.Today)+" "+ str(self.Yesterday)+" "+ str(self.Tenday)+" "+ str(self.Mean)+" "+ str(self.Peak)+" "+ str(self.Days)+" "+ str(self.Last_Day)