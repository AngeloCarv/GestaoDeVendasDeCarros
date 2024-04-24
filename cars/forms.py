from django import forms
from cars.models import BrandCars, Car

class carsForm(forms.Form):
    modelCar = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(queryset=BrandCars.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=7)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            modelCar=self.cleaned_data['modelCar'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            photo=self.cleaned_data['photo']
        )
        car.save()
        return car

class CarModelForms(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 5000:
            self.add_error('value', 'O valor mínimo do carro deve ser maior que R$ 5.000')
        return value
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível adicionar carros fabricados antes de 1975')
        return factory_year
