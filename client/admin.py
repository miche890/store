from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from django_tenants.utils import get_public_schema_name

from client.models import Client, Domain


class PublicTenantOnlyMixin():
    """Allow Access to Public Tenant Only"""

    def _only_public_tenant_access(self, request):
        return True if request.tenant.schema_name == get_public_schema_name() else False

    def has_view_permission(self, request, view=None):
        return self._only_public_tenant_access(request)

    def has_add_permission(self, request, view=None):
        return self._only_public_tenant_access(request)

    def has_change_permission(self, request, view=None):
        return self._only_public_tenant_access(request)

    def has_delete_permission(self, request, view=None):
        return self._only_public_tenant_access(request)

    def has_view_or_change_permission(self, request, view=None):
        return self._only_public_tenant_access(request)


# Register your models here.
class DomainInline(admin.TabularInline):
    model = Domain


@admin.register(Client)
class ClientAdmin(PublicTenantOnlyMixin, TenantAdminMixin, admin.ModelAdmin):
    inlines = [
        DomainInline
    ]
    list_display = ('schema_name', 'name')
