# chatbot_app/management/commands/load_data.py
from chatbot_app.models import ChatbotResponse
import openpyxl
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load data from an XLSX file into the database'

    def add_arguments(self, parser):
        parser.add_argument('xlsx_file', type=str, help='Path to the XLSX file')

    def handle(self, *args, **options):
        xlsx_file = options['xlsx_file']

        try:
            workbook = openpyxl.load_workbook(xlsx_file)
            sheet = workbook.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                input_text, response_text = row[0], row[1]
                ChatbotResponse.objects.create(
                    input_text=input_text,
                    response_text=response_text,
                )

            self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error loading data: {e}'))
