from mainHandler import *
from plots import *
from geolocation import gmaps_img

class parameter(mainHandler):
    def get(self, **kwargs):
        user = users.get_current_user()
        if user:
            username = user.nickname()
            loginLink = users.create_login_url(self.request.uri)
            logoutLink = users.create_logout_url(self.request.uri)
        else:
            username = None
            loginLink = users.create_login_url(self.request.uri)
            logoutLink = "/"
        graphs = recentPlots()
        points=filter(None,(graph.geoPt for graph in graphs))
        geolocationUrl=None
        if points:
            geolocationUrl=gmaps_img(points)
        self.renderPage("parameters.html", username = username, loginLink = loginLink, logoutLink = logoutLink, plots = graphs, geolocationUrl = geolocationUrl)
