""""

This file has functions to generate unique ids for the url given. 

Basically we want to generate a unique 64bit uuid and convert to hexa decimal 

"""

from uuid import uuid4
import string 

bit_size=64
# BASE_LIST = string.ascii_letters + string.digits
BASE_LIST = "0123456789ABCDEF"
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))


def init_app(app):
    # app.teardown_appcontext(close_db)
    # app.cli.add_command(init_db_command)
    pass 

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
    return base_encode(unique_id)
    # print(unique_id)
    # print(base_encode(unique_id))


if __name__ =="__main__":
    generateUrl('google.com')
