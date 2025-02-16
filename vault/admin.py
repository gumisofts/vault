from django.contrib import admin
from vault.models import SecretValue, Vault


class SecretValueAdmin(admin.ModelAdmin):
    list_display = ["field", "value", "created_at", "updated_at"]

    list_filter = ["vault__title", "created_at", "updated_at"]


class VaultAdmin(admin.ModelAdmin):
    list_display = ["title", "app_number", "dev_mode", "created_at", "updated_at"]
    list_filter = ["dev_mode", "created_at", "updated_at"]


admin.site.register(SecretValue, SecretValueAdmin)
admin.site.register(Vault, VaultAdmin)
