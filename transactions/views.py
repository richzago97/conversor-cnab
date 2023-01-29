from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from .forms import UploadCnbalForm
from .serializers import TransactionSerializer
import datetime
import ipdb

store_data = []
stores = {}


def transactions(request):
    store_data = [
        {"store_name": store, "store_total": total} for store, total in stores.items()
    ]
    context = {"store_data": store_data}
    return render(request, "transactions.html", context)


def upload_file(request):
    if request.method == "POST":
        form = UploadCnbalForm(request.POST, request.FILES)
        file = request.FILES["file"]
        if form.is_valid():
            handle_uploaded_file(file)
            return HttpResponseRedirect("transactions")
    else:
        form = UploadCnbalForm()
    return render(request, "upload.html", {"form": form})


def handle_uploaded_file(file):

    decoded_file = file.read().decode("utf-8")
    formated_file = decoded_file.replace("\r", "").replace("\n", "")
    start = 0
    end = 80
    while len(formated_file) > end:
        field = formated_file[start:end]
        dict_cnab = {
            "type": field[0:1],
            "date": datetime.date(
                int(field[1:5]),
                int(field[5:7]),
                int(field[7:9]),
            ),
            "value": (float(field[9:19]) / 100),
            "cpf": field[19:30],
            "card": field[30:42],
            "time": datetime.time(
                int(field[42:44]), int(field[44:46]), int(field[46:48])
            ),
            "owner_store": field[48:62],
            "name_store": field[62:81],
        }
        serializer = TransactionSerializer(data=dict_cnab)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        store_name = dict_cnab["name_store"]
        if store_name in stores:
            stores[store_name] += dict_cnab["value"]
        else:
            stores[store_name] = dict_cnab["value"]

        start += 80
        end += 80
