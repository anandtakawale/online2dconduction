from mainHandler import *
from validTemp import validTemp
from solveConduct2d import solveConduct2d
from cStringIO import StringIO
import matplotlib.pyplot as plt
matplotlib.use('Agg')

class conduct2d(mainHandler):
    def post(self):
        Tup = self.request.get('Tup')
        Tleft = self.request.get('Tleft')
        Tdown = self.request.get('Tdown')
        Tright = self.request.get('Tright')
        Tuser = {'Tup':Tup, 'Tleft':Tleft, 'Tright':Tright, 'Tdown':Tdown}
        T = validTemp(**Tuser)
        if type(T) == list:
            for t in T:
                Tuser[t] = "Input invalid or beyond limits"
            self.renderPage("parameters.html", **Tuser)
        else:
            Tdist = solveConduct2d(**T)
            CS = plt.contour(T,np.linspace(min(inputs), max(inputs), 12), linewidths = 1.5)
            plt.clabel(CS, inline=1, fontsize=10)
            plt.title("Temperature distribution")
            plt.colorbar(CS, shrink = 0.8, extend = 'both')
            rv = StingIO()
            plt.savefig(rv, format = "png")
            plot = rv.getvalue().encode("base64").strip()
            plt.clf()
            rv.close()
            self.renderPage("result.html", plot = plot, **T)
