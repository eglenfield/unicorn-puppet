# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 12:47
from __future__ import unicode_literals

from django.db import migrations
from puppet_parser import initialize, package_parser, user_parser, volume_parser

import json
import os
import re


class Migration(migrations.Migration):

    def parser(apps, schema_editor):
        Packages = apps.get_model("analyser", "packages")
        Users = apps.get_model("analyser", "users")
        Volumes = apps.get_model("analyser", "volumes")

        package_parser(Packages)
        user_parser(Users)
        volume_parser(Volumes)

    dependencies = [
        ('analyser', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(parser),
    ]