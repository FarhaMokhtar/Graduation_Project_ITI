from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from st_notifications.models import Note

class Command(BaseCommand):
    help = "Delete notes older than a certain period"

    def handle(self, *args, **kwargs):
        days_to_keep = 0   
        threshold_date = now() - timedelta(days=days_to_keep)

        expired_notes = Note.objects.filter(created_at__lte=threshold_date)
        count = expired_notes.count()
        expired_notes.delete()

        self.stdout.write(self.style.SUCCESS(f"Deleted {count} expired notes."))
