import common


class Map:
    pageTitle = "Map"

    # handle HTTP GET requests here.  Name gets value from routing rules above.
    def GET(self):
        return str(  common.render._head(self.pageTitle, stylesheets=['/static/css/map.css'], scripts=['/static/js/map.js'])) \
               + str(common.render._header(common.navbar, self.pageTitle)) \
               + str(common.render.map()) \
               + str(common.render._tail())