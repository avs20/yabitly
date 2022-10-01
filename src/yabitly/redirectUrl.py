""""

This file has functions to redirect to urls which are already stored in the app. 

"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from src.yabitly.cache import cache
from src.yabitly.db import get_db

bp = Blueprint('redirectUrl',__name__, url_prefix='/redirect')

@bp.route('', methods = ['GET'])
def fetchUrl():
    url = request.args.get('key')
    if url is None or len(url.strip()) == 0:
        # TODO redirect here to 404
        return  'Invalid Url : Please send proper URL', 400 
    
    cache_val = cache.get(url)
    redirectTo = getMappedUrl(url) if cache_val is None else cache_val
    if redirectTo :
        # TODO redirect to 404 page on website.
        return redirectTo, 200
        #return redirect(redirectTo, code=302)
    else:
        return 'Page not found', 404

def init_app(app):
    pass


def get_from_db( key ):
    """
    saves the data into db for urls 
    """
    db = get_db()
    if db is None:
        raise Exception("Can't conenct to RDS!")        
    output = db.execute(" select full_url from url_shorten where shorten_url = '{}'".format(key) )
    if len(output.current_rows) == 0:
        return None
    else:
        return output[0].full_url


def getMappedUrl(url):
    # use cache here, see if cache is present. 
    fullUrl = get_from_db(url)
    cache.set(url, fullUrl)
    return fullUrl
