from django.core.management.base import BaseCommand, CommandError
from aws.models import Matter
from django.core import serializers
import json
import pandas as pd


class Command(BaseCommand):

    def handle(self, *args, **options):
        Matter.objects.get_or_create(name="Anglais", description="Préparation au toeic", hours_number=15)
        Matter.objects.get_or_create(name="BI et Big Data", description="Informatique décisionelle et du Big Data",
                                     hours_number=15)
        Matter.objects.get_or_create(name="Cloud et Big Data", description="GCP, AWS, AZURE...", hours_number=15)
        Matter.objects.get_or_create(name="Communication professionnelle",
                                     description="Techniques de Communication Professionnelle", hours_number=30)
        Matter.objects.get_or_create(name="Deep Learning",
                                     description="Apprendre le deep learning et participer à des compétitions kaggle",
                                     hours_number=15)
        Matter.objects.get_or_create(name="AWS",
                                     description="Environnement de développement, de test et de production : amazon web service",
                                     hours_number=30)
        Matter.objects.get_or_create(name="Option", description="Tout depend le choix de l'étudiant", hours_number=15)
        Matter.objects.get_or_create(name="Management de projet", description="gestion de projet", hours_number=15)
        Matter.objects.get_or_create(name="Mathématiques", description=" Mathématique avec R", hours_number=15)
        Matter.objects.get_or_create(name="Programme Open",
                                     description="Tout depend le choix des associations de l'étudiant", hours_number=15)
        Matter.objects.get_or_create(name="Spark core", description="Spark avec scala", hours_number=15)

        print('Successfully ' + str(Matter.objects.all().count()) + ' matters created')

        data = Matter.objects.all()
        df = pd.DataFrame(data)
        df.to_json("matters.json")
