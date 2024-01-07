# in wagtail_rawhtml/utils.py
from bs4 import BeautifulSoup
from wagtail.rich_text import RichText


def convert_html_to_richtext(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Here you'll convert the soup object to a representation compatible with Wagtail's RichText
    # For simplicity, I am just getting the text from HTML, 
    # you should implement conversion according to your needs
    
    text_content = soup.get_text(separator='\n', strip=True)
    
    return RichText(text_content)
