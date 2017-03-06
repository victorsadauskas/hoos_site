from django.views import generic
from django.views.generic.edit import CreateView
from .models import Mate, Nickname


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'home/index.html'

    context_object_name = 'all_mates'

    def get_queryset(self):
        return Mate.objects.all()


class DetailView(generic.DetailView):
    model = Mate
    template_name= 'home/detail.html'
