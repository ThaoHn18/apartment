from django.db import models
from enum import Enum
# from company.models import Company

class PermissonName(Enum):
    List = 'List'
    Create = 'Create'
    Detail = 'Detail'
    Update = 'Update'
    Delete = 'Delete'


class Permission(models.Model):

    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=25)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='permission')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "permission"
        ordering = ["created_at"]

    def __str__(self):
        return '{}'.format(self.name)

    # @property
    # def is_List(self):
    #     return self.name == PermissonName.List.value
    #
    # @property
    # def is_Create(self):
    #     return self.name == PermissonName.Create.value
    #
    # @property
    # def is_Detail(self):
    #     return self.name == PermissonName.Delete.value
    #
    # @property
    # def is_Update(self):
    #     return self.name == PermissonName.Update.value
    #
    # @property
    # def is_Delete(self):
    #     return self.name == PermissonName.roler5.value