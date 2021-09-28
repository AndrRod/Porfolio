from django.shortcuts import redirect, render, HttpResponse


# def home(request):
#     return render(request, 'home.html')



from .settings import EMAIL_HOST_USER
from .forms import Formulario_contacto
from django.contrib import messages

from django.shortcuts import redirect, render, HttpResponse

from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def home(request):

    if request.method=='POST':
        miFormulario = Formulario_contacto(request.POST)

        if miFormulario.is_valid():
            

            destinatario = request.POST['email']

            nombre = request.POST['nombre']
            mensaje = request.POST['mensaje']
            asunto = request.POST['asunto']
            

            contexto = {'nombre': nombre, 'mensaje': mensaje}

            template = render_to_string('mensaje.html', contexto)
            
            email = EmailMultiAlternatives(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [destinatario]
                
                )
            
            email.attach_alternative(template, 'text/html')
            email.send()

            messages.success(request, f'{nombre} has enviado un correo exitosamente!!!')
            return redirect('home')
        # return render(request, 'home.html', {'mensaje': mensaje})
        else:

            messages.warning(request, 'Hubo un error su mensaje no pudo ser enviado')
            return redirect('home')
        
    else:   
        miFormulario=Formulario_contacto()
        # obtiene un formulario vacio
        # seguidamente estmos pidiendo que debe renderizar a un html con el diccionario que encapsula la variable miFormulario
    
    return render(request, "home.html", {"form": miFormulario})