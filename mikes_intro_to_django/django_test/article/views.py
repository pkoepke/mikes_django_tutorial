from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from article.models import Article

# Create your views here.

def hello(request):
    name = "Mike"
    html = "<html><body>Hi %s, this example WITHOUT a template seems to have worked!</body></html>" % name
    return HttpResponse(html)

def hello_template(request): # example to teach us about Context objects
    name = "Mike"
    t = get_template('hello.html')
    html = t.render( Context( {'name': name} ) )
    return HttpResponse(html)

def hello_template_simple(request): # uses render_to_response() helper function to simplify and automatically handle context
    name = "Mike"
    return render_to_response('hello.html', {'name': name} )

class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Mike'
        return context

def homepage(request):
    html = 'This is the home page for Mike\'s Django Tutorial.<br /><a href="/hello/">/hello/</a><br /><a href="/hello_template/">/hello_template/</a><br /><a href="/hello_template_simple/">/hello_template_simple/</a><br /><a href="/hello_class_view/">/hello_class_view/</a><br /><a href="/articles/all/">/articles/all/</a><br /><a href="/articles/get/1/">/articles/get/1/</a><br /><a href="/admin/">/admin/</a><br />'
    return HttpResponse(html)

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all() } )

def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id) } )

