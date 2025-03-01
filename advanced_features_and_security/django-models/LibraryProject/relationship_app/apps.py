from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

class DjangoModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_models'

    def ready(self):
        import django_models.signals  # Ensures signals are registered
