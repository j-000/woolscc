from server import (
  app, 
  api
)
from views import (
  UrlShorter, 
  UrlRedirect
)


# NGINX will only route traffic to the backend 
# that starts with /B or has any ?query=value, 
# even though the route below catched anything after /.
api.add_resource(UrlShorter, '/') 

# This is the route that catched /B<anything>
api.add_resource(UrlRedirect, '/<identifier>')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
