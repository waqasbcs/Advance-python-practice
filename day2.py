from django.shortcuts import get_object_or_404
from myapp.models import MyModel

obj = get_object_or_404(MyModel, pk=1)
