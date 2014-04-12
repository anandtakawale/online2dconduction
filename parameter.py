from mainHandler import *

class parameter(mainHandler):
    def get(self, **kwargs):
        self.renderPage("parameters.html")
