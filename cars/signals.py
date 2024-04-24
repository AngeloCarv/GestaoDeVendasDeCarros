from django.db.models.signals import pre_save, pre_delete , post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInvetory
from django.db.models import Sum
#from openai_api.client import get_car_ai_bio

def Car_Inventory_Update():
      cars_count = Car.objects.all().count()
      cars_value = Car.objects.aggregate(
        total_value= Sum('value')
    )['total_value']
      CarInvetory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save,sender=Car)
def car_pre_save(sender, instance, **kwargs):
     if not instance.bio:
          #ia_bio = get_car_ai_bio(
           #    instance.modelCar, instance.brand, instance.factory_year
          #)
          instance.bio = 'Bio gereda automaticamente'

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    Car_Inventory_Update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    Car_Inventory_Update()