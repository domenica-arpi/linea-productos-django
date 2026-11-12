from django.http import HttpResponse


def list_notifications(request):
    avisos = [
        "Bienvenido al sistema",
        "Tiene 2 tareas pendientes",
        "Mantenimiento programado para el viernes",
    ]
    html = "<h1>Notificaciones</h1><ul>"
    for aviso in avisos:
        html += f"<li>{aviso}</li>"
    html += "</ul><p><a href='/'>Volver al inicio</a></p>"
    return HttpResponse(html)
