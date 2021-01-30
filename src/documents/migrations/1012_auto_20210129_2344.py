# Generated by Django 3.1.5 on 2021-01-29 22:44

from django.db import migrations, models


COLOR_ID_TO_CODE_MAP = {
    1: "#a6cee3",
    2: "#1f78b4",
    3: "#b2df8a",
    4: "#33a02c",
    5: "#fb9a99",
    6: "#e31a1c",
    7: "#fdbf6f",
    8: "#ff7f00",
    9: "#cab2d6",
    10: "#6a3d9a",
    11: "#b15928",
    12: "#000000",
    13: "#cccccc"
}


CODE_TO_COLOR_ID_MAP = {
    "#a6cee3": 1,
    "#1f78b4": 2,
    "#b2df8a": 3,
    "#33a02c": 4,
    "#fb9a99": 5,
    "#e31a1c": 6,
    "#fdbf6f": 7,
    "#ff7f00": 8,
    "#cab2d6": 9,
    "#6a3d9a": 10,
    "#b15928": 11,
    "#000000": 12,
    "#cccccc": 13
}


def colour_to_colour_code(apps, schema_editor):
    Tag = apps.get_model("documents", "Tag")
    for tag in Tag.objects.all():
        if tag.colour in COLOR_ID_TO_CODE_MAP:
            tag.colour_code = COLOR_ID_TO_CODE_MAP[tag.colour]


def colour_code_to_color(apps, schema_editor):
    Tag = apps.get_model("documents", "Tag")
    for tag in Tag.objects.all():
        if tag.colour_code.lower() in CODE_TO_COLOR_ID_MAP:
            tag.colour = CODE_TO_COLOR_ID_MAP[tag.colour_code.lower()]
        else:
            tag.colour = 1


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '1011_auto_20210101_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='colour_code',
            field=models.CharField(default='#a6cee3', max_length=9),
        ),
        migrations.RunPython(
            colour_to_colour_code, colour_code_to_color
        ),
        migrations.RemoveField(
            model_name='tag',
            name='colour',
        ),
    ]
