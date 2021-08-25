import app.request as rq
import urllib.request,json


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




base_url=quote_api
def get_quotes():

   with rq.get(base_url) as data:
       quotes = data.json()

   return quotes

