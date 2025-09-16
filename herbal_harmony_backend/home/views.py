from django.shortcuts import render, HttpResponse
import re
from django.utils.html import escape
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is the home page of Herbal Harmony Backend')

def about(request):
    return HttpResponse('This is the about page of Herbal Harmony Backend')

def yoga(request):
    query = request.GET.get('query', '').strip()

    content = """
    """

    highlighted_content = content  # Default to original content if no query
    if query:
        # Escape the query to prevent XSS attacks
        #escaped_query = escape(query)
        # Use regex to find whole word matches, case insensitive
        pattern = re.compile(r'\b' + re.escape(query) + r'\b', re.IGNORECASE)
        # Replace matches with highlighted version
        highlighted_content = pattern.sub(
            lambda m: f"<mark>{escape(m.group(0))}</mark>", content
            )
        highlighted_content = mark_safe(highlighted_content)

    return render(request, 'yoga.html', {
        'content': highlighted_content,
        'query': query
        })
