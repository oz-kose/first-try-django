"""
To render html web pages
"""
from django.http import HttpResponse

from articles.models import Article
from django.template.loader import render_to_string

#MVT MODEL VIEW TEMPLATE

def home_view(request, id=None, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """


    #from database
    article_obj = Article.objects.get(id=1)
    object_queryset = Article.objects.all()
    word_salad = ['yes', 'why', 'dumb', 'right', 'whatever']
    context = {
        "object_queryset": object_queryset,
        "word_salad": word_salad,
        # "title": article_obj.title,
        # "content": article_obj.title
    }

    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = 
    # """
    # <h1>{title}</h1>
    # <p>{content}</p>
    # <p>rando stuff</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING)
