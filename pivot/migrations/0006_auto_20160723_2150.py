# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 21:50
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pivot', '0005_auto_20160723_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pivotpage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField((('bottom_text_header', wagtail.wagtailcore.blocks.StructBlock((('header', wagtail.wagtailcore.blocks.CharBlock()), ('subheader', wagtail.wagtailcore.blocks.CharBlock()), ('background', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('centered_hero', wagtail.wagtailcore.blocks.StructBlock((('header', wagtail.wagtailcore.blocks.CharBlock()), ('subheader', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('background', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('centered_page_header', wagtail.wagtailcore.blocks.StructBlock((('header', wagtail.wagtailcore.blocks.CharBlock()), ('subheader', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('background', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('coming_soon_banner', wagtail.wagtailcore.blocks.StructBlock((('header', wagtail.wagtailcore.blocks.CharBlock()), ('note', wagtail.wagtailcore.blocks.CharBlock()), ('background', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('header_with_image', wagtail.wagtailcore.blocks.StructBlock((('header', wagtail.wagtailcore.blocks.CharBlock()), ('background', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('header_with_problems', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('problems', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('question', wagtail.wagtailcore.blocks.TextBlock()), ('answer', wagtail.wagtailcore.blocks.TextBlock())))))))), ('page_header', wagtail.wagtailcore.blocks.StructBlock((('header', wagtail.wagtailcore.blocks.CharBlock()), ('subheader', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('background', wagtail.wagtailimages.blocks.ImageChooserBlock()))))), blank=True, null=True),
        ),
    ]
