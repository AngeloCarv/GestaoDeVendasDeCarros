from django.db import models

class BrandCars(models.Model):
    id = models.AutoField(primary_key=True)#ID da marca 
    name = models.CharField(max_length=200)#nome da marca

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)#ID do carro
    modelCar = models.CharField(max_length=200)#modelo do carro
    brand = models.ForeignKey(BrandCars, on_delete=models.PROTECT, related_name='car_brands')#marca do carro
    factory_year = models.IntegerField(blank=True, null=True)#ano de fabricação do carro
    model_year = models.IntegerField(blank=True, null=True)#ano do modelo do carro
    plate = models.CharField(max_length=7, blank=True, null=True)#placa do carro
    value = models.FloatField(blank=True, null=True)#valor do carro
    photo = models.ImageField(upload_to='cars/',blank=True, null=True)#images dos carros 
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.modelCar
    
class CarInvetory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'