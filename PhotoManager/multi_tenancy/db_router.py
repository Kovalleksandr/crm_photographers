import threading

class TenantRouter:
    """
    Використовує різні бази даних для кожної команди (organization).
    """
    thread_local = threading.local()

    @staticmethod
    def get_database():
        return getattr(TenantRouter.thread_local, "db", "default")

    @staticmethod
    def set_database(db_name):
        TenantRouter.thread_local.db = db_name

    def db_for_read(self, model, **hints):
        return self.get_database()

    def db_for_write(self, model, **hints):
        return self.get_database()

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == self.get_database()
