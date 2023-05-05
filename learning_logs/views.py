from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    """Домашняя страница прложения learning_log"""
    return render(request, 'learning_logs/index.html')

def topics(reqest):
    """Выводит список тем."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(reqest, 'learning_logs/topics.html', context)
