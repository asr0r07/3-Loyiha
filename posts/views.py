from django.shortcuts import HttpResponse

def home_page(request):
    html_response="""
        <h1>Blog site</h1>
    """
    return HttpResponse(html_response)