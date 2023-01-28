from django.urls import path
from .views import upload_file, transactions

urlpatterns = [
    path("cnab/transactions/", transactions),
    path("cnab/", upload_file),
]
