import urllib2
from xml.dom import minidom
from google.appengine.ext import db

IP_URL="http://api.hostip.info/?ip="
def get_coords(ip):
#    ip="4.2.2.2"
#    ip="23.24.209.141"
    url=IP_URL+ip
    content = None
    try:
        content=urllib2.urlopen(url).read()
    except URLError:
        return
    if content:
        d=minidom.parseString(content)
        coords= d.getElementsByTagName("gml:coordinates")
        if coords and coords[0].childNodes[0].nodeValue:
            lon,lat= coords[0].childNodes[0].nodeValue.split(',')
            return db.GeoPt(lat,lon)

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"

def gmaps_img(points):
    markers= '&'.join('markers=%s,%s'%(p.lat,p.lon) for p in points)
    return GMAPS_URL +markers
