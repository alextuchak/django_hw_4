from django.core.management.base import BaseCommand
from articles.models import Tag
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open ('school.json') as f:
            file = json.load(f)
            for object in file:
                if object.get('model') == "school.student":
                    t = student_teacher()



        for tag in ['Культура', 'Город', 'Наука', 'Здоровье', 'Международные отношения', 'Космоc']:
            tag = Tag(name=tag)
            tag.save()
