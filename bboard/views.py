from django.shortcuts import render, get_object_or_404
from .models import Bb, Rubric
from django.views.generic.edit import CreateView

# Главная страница: список объявлений
def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

# Объявления по рубрике
def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = get_object_or_404(Rubric, pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

# Детальная страница объявления
def detail(request, bb_id):
    bb = get_object_or_404(Bb, pk=bb_id)
    return render(request, 'bboard/detail.html', {'bb': bb})

from django.shortcuts import redirect
from django.urls import reverse

def go_home(request):
    url = reverse('index')
    return redirect(url)


from .forms import BbForm

class BbCreateView(CreateView):
    template_name = 'bboard/add.html'
    form_class = BbForm
    success_url = '/'  # redirect после сохранения
