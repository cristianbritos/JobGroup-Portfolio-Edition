from django.shortcuts import render
from django.views.generic import ListView


from django.http import JsonResponse
from django.contrib import messages
from apps.school.models import Curso
from apps.shop.models import Producto
from .models import Mensaje
from .forms import MensajeForm

class IndexView(ListView):
    model = Curso
    template_name = 'index.html'
    form_class = MensajeForm



    def get_queryset(self):
        return Curso.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cursos'
        context['action'] = 'List'
        context['entity'] = 'Curso'
        context['form'] = self.form_class()
        context['productos'] = Producto.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, "Tu mensaje ha sido enviado con éxito. Gracias por contactarnos. Te responderemos pronto.")
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': form.errors})

def success_view(request):
    return render(request, 'mensaje/success.html')