from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from vault.serializers import SecretValueSerializer
from vault.models import SecretValue
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class SecretValueViewsets(ListModelMixin, GenericViewSet):
    serializer_class = SecretValueSerializer
    queryset = SecretValue.objects.all()
    permission_classes = []

    def get_queryset(self):
        queryset = self.queryset
        app_number = self.request.GET.get("app_number")

        if app_number:
            queryset = queryset.filter(vault__app_number=app_number)

        return queryset


@csrf_exempt
def get_environmental_variables(request, app_number, **kwargs):
    values = SecretValue.objects.filter(vault__app_number=app_number)
    file_content = ""
    for q in values:
        file_content += f"{q.field}={q.value}\n"

    response = HttpResponse(content=file_content, content_type="text/plain")
    response["Content-Disposition"] = 'attachment; filename=".env"'
    return response
