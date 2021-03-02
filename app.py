from server import (app, api)
from views import (UrlShorter, UrlRedirect)


api.add_resource(UrlRedirect, '/<identifier>')
api.add_resource(UrlShorter, '/')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
