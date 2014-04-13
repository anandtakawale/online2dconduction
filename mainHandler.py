import webapp2
from jinja2Setup import *

from google.appengine.api import users

#Defining a super class to make rendering jinja2 templates easy for other. All other Handlers inherit from this.
class mainHandler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)
    def renderStr(self, template, **kwargs):
        t = jinja_env.get_template(template)
        return t.render(kwargs)
    def renderPage(self, template, **kwargs):
        self.write(self.renderStr(template, **kwargs))
