from mainHandler import *
from validTemp import validTemp
from solveConduct2d import *
import cStringIO
from plots import recentPlots, Plot
from geolocation import get_coords
import matplotlib.pyplot as plt
from time import sleep
from geolocation import gmaps_img
from google.appengine.api import memcache

def plotcontour(T, plotType):
    Tdist = solveConduct2d(**T)
    if plotType == "filled":
        CS = plt.contourf(Tdist, 15)
    else:
        CS = plt.contour(Tdist, 15)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.title("Temperature distribution")
    plt.colorbar(CS, shrink = 0.8)
    rv = cStringIO.StringIO()
    plt.savefig(rv, format = "png")
    plot = "data:image/png;base64," + rv.getvalue().encode("base64").strip()
    plt.clf()
    rv.close()
    return plot
    
class conduct2d(mainHandler):
    def post(self):
        Tup = self.request.get('Tup')
        Tleft = self.request.get('Tleft')
        Tdown = self.request.get('Tdown')
        Tright = self.request.get('Tright')
        plotType = self.request.get('plotType')
        Tuser = {'Tup':Tup, 'Tleft':Tleft, 'Tright':Tright, 'Tdown':Tdown}
        T = validTemp(**Tuser)
        #To avoid zero array passed to contourplot
        if type(T) == dict:
            flag = 0
            for value in T.values():
                if value != 0:
                    flag = 1
                    break
                if flag == 0:
                    T = ["error" + key for key in Tuser.keys()]
        if type(T) == list:
            for t in T:
                Tuser[t] = "Input invalid or beyond limits"
            plots = recentPlots()
            points=filter(None,(plot.geoPt for plot in plots))
            geolocationUrl=None
            if points:
                geolocationUrl=gmaps_img(points)
            self.renderPage("parameters.html", plots = plots,geolocationUrl = geolocationUrl, **Tuser)
        else:
            plot = plotcontour(T, plotType)
            user = users.get_current_user()
            if user:
                p = Plot(user = user, image = plot, **T)
                coords=get_coords(self.request.remote_addr)
                if coords:
                    p.geoPt = coords
                p.put()
                sleep(0.1)
                recentPlots(True)
            self.renderPage("result.html", plot = plot, **T)


class cacheFlush(mainHandler):
    def get(self):
        memcache.flush_all()
        self.redirect("/")
        
