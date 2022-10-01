""""

This file has functions to generate unique ids for the url given. 

Basically we want to generate a unique 64bit uuid and convert to hexa decimal 

"""

from textwrap import shorten
from uuid import uuid4
import string 
from src.yabitly.cache import cache

import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from src.yabitly.db import get_db

bp = Blueprint('genUrl',__name__, url_prefix='/generateUrl')

bit_size=64
BASE_LIST = string.ascii_letters + string.digits
# BASE_LIST = "0123456789ABCDEF"
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))
BASE_URL = 'http://yabitly.com/'


@bp.route('', methods = ['GET'])
def generateURL():
    url = request.args.get('url')
    if url is None or len(url.strip()) == 0:
        return  'Invalid Url : Please send proper URL', 400 
    
    key = generateUrl(url)
    cache.set(key, url)
    newUrl = BASE_URL + key    
    return newUrl
def init_app(app):
    pass


def insert_into_db( short_url, full_url):
    """
    saves the data into db for urls 
    """
    db = get_db()
    if db is None:
        raise Exception("Can't conenct to RDS!")        

    output = db.execute_async("insert into url_shorten(shorten_url, full_url) values('{}', '{}')".format(short_url, full_url))
    # print(output)
    


def base_encode(integer, base=BASE_LIST):
    if integer is None:
        return None

    if type(integer) == type(1.):
        raise ValueError("Cannot encode floating point number. Enter integer")

    if type(integer) == type('str'):
        try :
            integer = int(integer)
        except Exception as ex:
            raise  ValueError("Can't convert string input to integer.")

    if integer == 0:
        return base[0]

    length = len(base)
    ret = ''
    while integer != 0:
        # print(integer % length)
        ret = base[integer % length] + ret
        integer = integer // length

    return ret




def generateUrl(url):
    unique_id = uuid4().int >> bit_size    
    short_url = base_encode(unique_id)
    insert_into_db(short_url, url)
    return short_url
    
    


# if __name__ =="__main__":    

#     generateUrl('google.com')
