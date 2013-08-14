from django.views.generic import ListView, DetaitView
from django.views.generic.edit import CreateView
from .models import Message


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
