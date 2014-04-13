from mainHandler import *
from plots import *

class parameter(mainHandler):
    def get(self, **kwargs):
        user = users.get_current_user()
        if user:
            username = user.nickname()
            loginLink = None
        else:
            username = None
            loginLink = users.create_login_url(self.request.uri)
        graphs = recentPlots()
        self.renderPage("parameters.html", username = username, loginLink = loginLink, plots = graphs)
