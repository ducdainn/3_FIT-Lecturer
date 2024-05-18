from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path

class Command(BaseCommand):
    help = "Insert data from SQL file"

    def handle(self, *args, **kwargs):
        sql_file = Path(__file__).resolve().parent / 'data_insertion.sql'
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql = f.read()
            with connection.cursor() as cursor:
                cursor.execute(sql)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
# run: py manage.py insert_data_from_sql
