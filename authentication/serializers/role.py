from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from ..models import Role
from .permissions import PermissionsSerializer

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

    def validate_name(self, name):
        if Role.objects.filter(name=name):
            raise serializers.ValidationError(_("This role {name} already exists").format(name=name))

        return name

    def validate(self, attrs):
        user = self.context['request'].user
        if not user.is_superuser:
            raise serializers.ValidationError(_("You don't have permission to create role"))

        return attrs


class RoleReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    permissions = PermissionsSerializer()
    created_at = serializers.DateTimeField(read_only=True)