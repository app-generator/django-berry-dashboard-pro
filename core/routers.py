from django.db import connections
from django.db.utils import OperationalError


conn = connections['postgres_default']

try:
    c = conn.cursor()
    reachable = True
except OperationalError:
    reachable = False

class FallbackRouter(object):
    def db_for_read(self, model, **hints):
       if reachable :
           return 'postgres_default'
       else:
           return 'fallback_db'

    def db_for_write(self, model, **hints):
       if reachable :
           return 'postgres_default'
       else:
           return 'fallback_db'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
       if reachable :
           return db == 'postgres_default'
       else:
           return db == 'fallback_db'