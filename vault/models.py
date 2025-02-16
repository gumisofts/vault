from django.db import models


class Vault(models.Model):
    app_number = models.PositiveBigIntegerField(unique=True)
    title = models.CharField(max_length=255)
    dev_mode = models.CharField(
        choices=[("beta", "Beta"), ("dev", "Dev"), ("pro", "Pro")], max_length=255
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}:{self.dev_mode}({self.app_number})"

    class Meta:
        db_table = "Vaults"


class SecretValue(models.Model):
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    field = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Secrets"
