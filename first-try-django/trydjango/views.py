"""
To render html web pages
"""
from django.http import HttpResponse

from articles import Article

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """


    #from database
    article_obj = Article.objects.get(id=3)

    H1_STRING = f"""
    <h1>{article_obj.title} ({article_obj.id})</h1>
    """
    P1_STRING = f"""
    <h1>{article_obj.content}</h1>
    """
    P2_STRING = """
    <h1>EB showed me how to do it</h1>
    """

    HTML_STRING = H1_STRING + P1_STRING + P2_STRING

    return HttpResponse(HTML_STRING)
