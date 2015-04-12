__author__ = 'tanuj'

import webapp2
import AppLogic
from spiders import *
import json

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write("Done")


class Transients(webapp2.RequestHandler):

    def get(self):
        satellite = self.request.get('satellite')
        if satellite.lower() == "swift":
            appLogicObject = AppLogic.AppLogic()
            json_obj = appLogicObject.buildjson("swift")
            self.response.write(json_obj)
        else:
            self.response.write("Satellite not available")


class GraphData(webapp2.RequestHandler):

    def get(self):
        url = "http://swift.gsfc.nasa.gov/results/transients/"
        sourcename = str(self.request.get('sourcename'))
        """
        if '*' in sourcename:
            newname = ""
            for c in sourcename:
                if c == '*':
                    newname += '+'
                else:
                    newname += c
            sourcename = newname
        """
        finurl = url+sourcename+".lc.txt"
        print "DEBUG", url, sourcename
        datSpider = SwiftDataSpider()
        try:
            data_set = datSpider.parse(finurl)
        except Exception as e:
            finurl = url+"/weak/"+sourcename+".lc.txt"
            data_set = datSpider.parse(finurl)
        full_json = []
        for data in data_set:
            json_data = {"day":data[0], "flux": data[1]}
            full_json.append(json_data)
        self.response.write(json.dumps({"source":full_json}))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/transients', Transients),
    ('/graphdata', GraphData),
], debug=True)