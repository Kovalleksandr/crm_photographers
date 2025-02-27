from django.utils.deprecation import MiddlewareMixin
from .db_router import TenantRouter
from .models import Organization

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                org = Organization.objects.get(owner=request.user)
                TenantRouter.set_database(f"tenant_{org.id}")  # Змінили "org_" на "tenant_" для відповідності db_name
            except Organization.DoesNotExist:
                TenantRouter.set_database('default')  # Завершили логіку