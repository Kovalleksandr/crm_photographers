import threading

class TenantRouter:
    thread_local = threading.local()

    @staticmethod
    def get_database():
        return getattr(TenantRouter.thread_local, "db", "default")

    @staticmethod
    def set_database(db_name):
        TenantRouter.thread_local.db = db_name

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'crm':
            user = hints.get('user')
            if user and user.organization:
                return user.organization.db_name
        return self.get_database()

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'crm':
            user = hints.get('user')
            if user and user.organization:
                return user.organization.db_name
        return self.get_database()

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'crm':
            return db != 'default' and db == self.get_database()
        return db == self.get_database()