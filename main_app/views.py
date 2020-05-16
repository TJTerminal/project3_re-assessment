from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm

# Create your views here.
def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form})

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home')

# class WidgetCreate(CreateView):
#     model = Widget
#     fields = '__all__'
#     success_url = '/'

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'