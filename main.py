import webapp2
from parameter import parameter
from conduct2d import conduct2d
from conduct2d import cacheFlush

app = webapp2.WSGIApplication([('/',parameter),
                               ('/result', conduct2d),
                               ('/flush', cacheFlush)],
                              debug = True)
