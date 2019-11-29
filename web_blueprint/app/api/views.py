from . import api


#
@api.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"