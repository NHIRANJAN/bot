# chatbot_app/management/commands/delete_chatbot_data.py

from django.core.management.base import BaseCommand
from chatbot_app.models import ChatbotResponse

class Command(BaseCommand):
    help = 'Deletes all data from the ChatbotResponse table'

    def handle(self, *args, **kwargs):
        ChatbotResponse.objects.all().delete()
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Deletes data from the ChatbotResponse table'

    def handle(self, *args, **kwargs):
        confirmation = input('Are you sure you want to delete all data from ChatbotResponse table? (yes/no): ')

        if confirmation.lower() == 'yes':
            # Perform the data deletion here
            from chatbot_app.models import ChatbotResponse
            ChatbotResponse.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Data deleted successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Data deletion canceled.'))

