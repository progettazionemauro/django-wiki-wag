# in wagtail_rawhtml/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from myapp.models import MyPage  # Adjust the import with your actual Page model and app
from .utils import convert_html_to_richtext

def convert_blocks(request):
    if request.method == 'POST':
        page_id = request.POST.get('page_id')
        block_id = request.POST.get('block_id')
        
        page = get_object_or_404(MyPage, id=page_id)  
        
        # Assuming your raw HTML blocks are in a StreamField named 'body'
        # Locate the specific block, convert it, and save back to the page.
        stream_data = page.body.stream_data
        for i, block in enumerate(stream_data):
            if str(i) == block_id and block['type'] == 'raw_html':
                html = block['value']
                richtext = convert_html_to_richtext(html)
                block['value'] = str(richtext)  # Save the converted Richtext back to the block
                break
        
        page.body.stream_data = stream_data
        page.save()
        
        return JsonResponse({'status': 'success', 'message': 'Block converted successfully!'})

    return render(request, 'wagtail_rawhtml/convert_blocks.html')
