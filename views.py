from flask import request, redirect, jsonify
from flask_restful import Resource
from models.URL import URL
from models.URL_serializer import URLSerializer
import os
from server import limiter
from urllib.parse import urlparse


HOST = os.getenv('HOST')


class UrlShorter(Resource):
  """
  GET /?url=<url>
  """

  decorators = [limiter.limit('100 per day', methods=['GET'])]

  def get(self):
    url = request.args.get('url')

    if not url:
      return jsonify(error='Missing "url" parameter.')        
    
    parsed_url = urlparse(url)

    print(parsed_url)

    path = parsed_url.path if parsed_url.path else parsed_url.netloc

    # Anything different to www.domain.gh or domain.gh is invalid
    if len(parsed_url.path.split('.')) < 1 or len(parsed_url.path.split('.')) > 3:
      return jsonify(error=f'Invalid url value "{url}".')

    if not parsed_url.scheme:
      url = 'https://' + parsed_url.netloc + parsed_url.path + parsed_url.query
    else:
      url = parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path + '?'+ parsed_url.query

    exists = URL._exists(url)
    if exists:
      return jsonify(URLSerializer().dump(exists)) 

    new_url = URL(original_url=url)
    return jsonify(URLSerializer().dump(new_url))


class UrlRedirect(Resource):
  """
  GET /<identifier>
  """
  def get(self, identifier):
    exists = URL.query.filter_by(identifier=identifier).first()
    if exists:
      return redirect(exists.original_url, code=301)
    return jsonify(error='Invalid identifier.')