import webapp2
from parameter import parameter
from conduct2d import conduct2d

app = webapp2.WSGIApplication([('/',parameter),
                               ('/result', conduct2d)],
                              debug = True)
