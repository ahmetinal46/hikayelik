from django.views.generic import TemplateView,ListView
from articles.models import Article

class HomeListView(ListView):
    queryset = Article.objects.filter(published=True).order_by('created_date').reverse()[:3]
    context_object_name = 'articles'
    template_name = 'index.html'
    




class AboutPageView(TemplateView):
    template_name = 'index.html'

