from import_export import resources
from .models import Books

class BookResource(resources.ModelResource):
    class Meta:
        model = Books