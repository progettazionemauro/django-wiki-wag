from wagtail import blocks

class PublicationBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    linked_page = blocks.PageChooserBlock(required=False, help_text='Select a linked page')

    class Meta:
        template = 'blog/publication_block.html'
