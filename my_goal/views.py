from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"


class ListView(generic.TemplateView):
    template_name = "goal_list.html"