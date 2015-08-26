from django.core.management import BaseCommand
import os, signal

class Command(BaseCommand):
    def handle(self, *args, **options):
        for line in os.popen("ps ax | grep huey | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)