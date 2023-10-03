from celery import shared_task
from .utils.samples import (
    generate_category,
    create_sample_car,
    create_sample_delivery,
)

@shared_task
def generate_category_task():
    generate_category()

@shared_task
def create_sample_car_task():
    create_sample_car()

@shared_task
def create_sample_delivery_task():
    create_sample_delivery()
