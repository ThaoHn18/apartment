
from django.contrib import admin

# Register your models here.
from authentication.models.users import User
from authentication.models.Role import Role
from authentication.models.Permissions import Permission

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)