from django import template
import re

register = template.Library()

@register.simple_tag
def extract_headings(content):
    headings = re.findall(r'<h[1-6]>(.*?)</h[1-6]>', content)
    

    return headings
