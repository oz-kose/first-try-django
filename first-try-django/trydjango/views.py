"""
To render html web pages
"""
from django.http import HttpResponse

from articles.models import Article

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """


    #from database
    article_obj = Article.objects.get(id=4)

    H1_STRING = f"""
    <h1>{article_obj.title}</h1>
    """
    P1_STRING = f"""
    <h1>{article_obj.content}</h1>
    """
    P2_STRING = """
    <h1>rando stuff</h1>
    """

    HTML_STRING = H1_STRING + P1_STRING + P2_STRING

    return HttpResponse(HTML_STRING)
