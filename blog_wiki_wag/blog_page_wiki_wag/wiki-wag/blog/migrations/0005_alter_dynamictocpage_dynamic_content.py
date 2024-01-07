# Generated by Django 3.2.22 on 2023-11-18 11:34

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_dynamictocpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamictocpage',
            name='dynamic_content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock())], blank=True, null=True, use_json_field=True),
        ),
    ]