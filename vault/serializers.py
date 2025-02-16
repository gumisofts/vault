from rest_framework.serializers import ModelSerializer
from vault.models import SecretValue


class SecretValueSerializer(ModelSerializer):
    class Meta:
        exclude = []
        model = SecretValue
