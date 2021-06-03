from django.shortcuts import render
from django.http import HttpResponse

participantes = [
    {
      'nombre':'Lizzie',
      'apellido':'Maradiaga',
      'correo':'lizzie@gmail.com',
      'twitter':'AmadeusLiz',
   },
   {
      'nombre':'Melva',
      'apellido':'Romero',
      'correo':'mr_romero@gmail.com',
      'twitter':'Melva.Romero',
   },
   {
      'nombre':'Abdiel',
      'apellido':'Banegas',
      'correo':'misael@gmail.com',
      'twitter':'Flaxtac',
   }
]

def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        participantes.append({
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'twitter': twitter
        })

        ctx = {
            'participantes': participantes
        }

        # return HttpResponse('El participante ha sido registrado')
        return render(request, 'registro/index.html', ctx)
    else:
        # contexto que va para la plantilla
        ctx = {
            'participantes': participantes
        }

        return render(request, 'registro/index.html', ctx)




