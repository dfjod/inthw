from django.contrib import admin
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class ClientAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.exclude(is_staff=True, is_superuser=True)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "id", "label", "client", "created_at"
    ]


class ProjectObjectAdmin(admin.ModelAdmin):
    list_display = [
        "id", "label", "project", "created_at"
    ]


class ProjectObjectDataPointAdmin(admin.ModelAdmin):
    list_display = [
        "id", "project_object", "data_point", "value", "created_at"
    ]


class CustomUserAdmin(UserAdmin):
    list_display = ["username", "id"]
    readonly_fields = ["id"]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.DataPoint)
admin.site.register(models.Person)
admin.site.register(models.ProjectObject, ProjectObjectAdmin)
admin.site.register(models.ProjectObjectDataPoint, ProjectObjectDataPointAdmin)