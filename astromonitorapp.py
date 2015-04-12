__author__ = 'tanuj'

import webapp2
import AppLogic


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
         satellite = self.request.get('satellite')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/transients', Transients),
], debug=True)