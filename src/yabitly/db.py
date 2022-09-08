import click
from flask import current_app, g
from cassandra.cluster import Cluster
from flask.cli import with_appcontext


# class DataBase:
#     def __init__(self):
#         self.db = None 
#         self.cluster = None
        
#     def get_db(self):
#         return self.connect()
        
#     def connect(self):
#         if self.db is None:
#             self.cluster = Cluster(['0.0.0.0'],port=9042)
#             self.session = self.cluster.connect('urlshorten',wait_for_all_pools=True)

#         return self.db
    
#     def close(self):
#         if self.cluster is not None:
#             self.cluster.shutdown()
        


def get_db():
    if 'db' not in g:
        g.db = Cluster(['0.0.0.0'],port=9042)
        g.db.session = g.db.connect('urlshorten',wait_for_all_pools=True)

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.shutdown()

def init_app(app):
    app.teardown_appcontext(close_db)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    
    app.cli.add_command(init_db_command)

