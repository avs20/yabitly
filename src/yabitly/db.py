import click
from flask import current_app, g
from cassandra.cluster import Cluster
from flask.cli import with_appcontext
import os
import socket 
from cassandra.auth import PlainTextAuthProvider

def isOpen(ip, port):
   test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      test.connect((ip, int(port)))
      test.shutdown(1)
      return True
   except:
      return False

def fakeLoadBalancer():
    # ips = []
    # port = 9042
    # for ip in os.environ.get('CASSANDRA_SEEDS').split(','):
    #     if isOpen(ip, port):
    #         ips.append(ip)
    ips = ["0.0.0.0"]
    return ips

def get_db():
    if 'db' not in g:
        cluster = Cluster(fakeLoadBalancer(), port=9042, auth_provider=PlainTextAuthProvider(username='cassandra', password='cassandra'))
        g.session = cluster.connect('urlshorten',wait_for_all_pools=False)

    return g.session


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.shutdown()

def init_app(app):
    app.teardown_appcontext(close_db)

# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo('Initialized the database.')

# def init_app(app):
    
#     app.cli.add_command(init_db_command)

