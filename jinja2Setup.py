import os
import jinja2

#setting /templates as the html files repository
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#setting up jinja2 environment, autoescaping is enabled
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)
