from django import forms

# tenemos que crear una clase de ese formulario (de contacto)
# por crear esta clase 
#  con python manage.py shell
# podemos ingresar al shell
# from gestionPedidos.forms import Formulario_contacto
# podemos crear objetos (variables de las clases)
# MiFormulario = Formulario_contacto({'asunto': 'algo', 'email': 'maail@gmail.com', 'mensaje': 'este es mensaje de prueba'})
# colocamos MiFormulario.cleaned_data y se muestra en pantalla los datos
class Formulario_contacto(forms.Form):
    nombre = forms.CharField(label='nombre', required=True)
    asunto = forms.CharField(label='asunto', required=True)
    email = forms.EmailField(label='email', required=True)
    # con widget le damos la forma que queramos que tenga
    mensaje = forms.CharField(widget=forms.Textarea)

