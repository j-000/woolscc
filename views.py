from flask import request, redirect, jsonify
from flask_restful import Resource
from models.URL import URL
from models.URL_serializer import URLSerializer
import os

HOST = os.getenv('HOST')


class UrlShorter(Resource):
  """
  GET /?url=<url>
  """
  def get(self):
    url = request.args.get('url')
    if not url:
      return jsonify(error='Missing "url" parameter.')      

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
    print(identifier)
    exists = URL.query.filter_by(identifier=identifier).first()
    if exists:
      return redirect(exists.original_url, code=301)
    return jsonify(error='Invalid identifier.')