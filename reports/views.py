import csv
from django.http import HttpResponse


def export_report(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="reporte.csv"'
    writer = csv.writer(response)
    writer.writerow(["ID", "Nombre", "Estado"])
    writer.writerow([1, "Ejemplo uno", "Activo"])
    writer.writerow([2, "Ejemplo dos", "Inactivo"])
    return response