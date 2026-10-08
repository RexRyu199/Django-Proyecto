import django.db.backends.mysql.base as mysql_base

def dummy_check(self):
    pass

mysql_base.DatabaseWrapper.check_database_version_supported = dummy_check