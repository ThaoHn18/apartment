
from django.db import models
from enum import Enum
from .Permissions import Permission


class RoleName(Enum):
    roler1 = 'Contractor management'
    roler2 = 'General contractor'
    roler3 = 'Group management'
    roler4 = 'Group in general'
    roler5 = 'User'


class Role(models.Model):

    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="role",
    )

    class Meta:
        db_table = "role"
        ordering = ["created_at"]

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def is_roler1(self):
        return self.name == RoleName.roler1.value

    @property
    def is_roler2(self):
        return self.name == RoleName.roler2.value

    @property
    def is_roler3(self):
        return self.name == RoleName.roler3.value

    @property
    def is_roler4(self):
        return self.name == RoleName.roler4.value

    @property
    def is_roler5(self):
        return self.name == RoleName.roler5.value