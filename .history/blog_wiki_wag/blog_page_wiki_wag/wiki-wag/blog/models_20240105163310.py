
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.models import Page
from wagtail import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from django.db import models
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField





from .blocks import PublicationBlock # rif 1 - Adding in rendering get_absolute_url
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock






from wagtail.images.blocks import ImageChooserBlock

class RawHTMLBlock(blocks.RawHTMLBlock):
    class Meta:
        icon = "code"  # Set a suitable icon from available Wagtail icons
        template = 'blog/raw_html_block.html'

class CodeBlock(blocks.StructBlock):
    code = blocks.TextBlock()
    class Meta:
        template = 'blog/code_block.html'

class FixedTableBlock(blocks.StructBlock):
    nation = blocks.CharBlock(required=True, help_text='Enter nation')
    capital = blocks.CharBlock(required=True, help_text='Enter capital')

    class Meta:
        icon = 'table'  # Set an icon for the block
        template = 'blog/fixed_table_block.html'  # Create this template for rendering the block




class DynamicTOCPage(Page):
    dynamic_content = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        # ... other block types ...
    ], use_json_field=True)

