from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from django.db import models
from wagtail.models import Page


from wagtail.admin.panels import FieldPanel, StreamF

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

class BlogPage(Page):
    author = models.CharField(max_length=255, default='Default Author')
    date = models.DateField("Post date")
    
    # New field for content choice
    content_choice = models.CharField(
        max_length=20,
        choices=[
            ('choice_one', 'Choice One'),
            ('choice_two', 'Choice Two'),
        ],
        default='choice_one',  # Set a default choice
        help_text="Select the content to be displayed on the page."
    )
    
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('code', CodeBlock()),
        ('raw_html', RawHTMLBlock()),
        ('publication', PublicationBlock()), # rif 1 - Adding in rendering get_absolute_url
        ('table', TypedTableBlock([
            ('text', blocks.CharBlock()),
            ('numeric', blocks.FloatBlock()),
            ('rich_text', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('country', blocks.ChoiceBlock(choices=[
                ('be', 'Belgium'),
                ('fr', 'France'),
                ('de', 'Germany'),
                ('nl', 'Netherlands'),
                ('pl', 'Poland'),
                ('uk', 'United Kingdom'),
            ])),
        ])),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('content_choice'),
        FieldPanel('body'),
    ]


class DynamicTOCPage(Page):
    dynamic_content = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        # ... other block types ...
    ], use_json_field=True)

