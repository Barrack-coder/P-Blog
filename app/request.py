# import app.request as rq
import urllib.request,json
from .models import Quotes

# Getting api key
secret_key = None
# Getting the news base url
quote_api = None

# Getting the new_quote_url base url
# new_quote_url = None

def configure_request(app):
    global  secret_key, quote_api
    secret_key = app.config["SECRET_KEY"]
    quote_api = app.config["QUOTES_API"]



base_url = quote_api
def get_quotes():
   print(base_url)
   with urllib.request.urlopen(quote_api) as url:
      quotes_api_data = url.read()
      quotes_api_response = json.loads(quotes_api_data)
      quote_object = None
      if quotes_api_response:
        author = quotes_api_response['author']
        quote = quotes_api_response['quote']
        quote_object = Quotes(author=author , quote=quote)
   return quote_object


