from django.urls import path
from wagtail import hooks
from .views import convert_blocks  # adjust the import to your view correctly

@hooks.register('register_admin_urls')
def register_admin_url():
    return [
        path('convert_blocks/', convert_blocks, name='convert_blocks'),
    ]

from wagtail.admin.menu import MenuItem
from django.urls import reverse

@hooks.register('register_admin_menu_item')
def register_converter_menu_item():
    return MenuItem('Convert Blocks', reverse('convert_blocks'), icon_name='code')
