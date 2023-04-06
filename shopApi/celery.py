from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTING_MODULE', 'shopApi.settings')

app = Celery('shopApi')
app.config_from_object('djnago.config:settings', namespace='CELERY')
