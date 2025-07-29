from django.db import models

class FarmOperation(models.Model):
    OPERATION_TYPES = [
        ('FERT', 'Fertilisation'),
        ('IRR', 'Irrigation'),
        ('PLANT', 'Planting'),
        ('HARV', 'Harvesting'),
        ('PEST', 'PesticideApplication'),
    ]
    operation_type = models.CharField(max_length=5, choices=OPERATION_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    farm = models.ForeignKey('farms.Farm', related_name='farm', on_delete=models.CASCADE)
    block_number = models.ForeignKey('farms.Block', related_name='block', on_delete=models.CASCADE)
    crop = models.CharField(max_length=100)
    operator_name = models.CharField(max_length=100)

    # class Meta:
    #     abstract = True  # Makes this a base class

class Fertilisation(FarmOperation):
    fertilizer_type = models.CharField(max_length=100)
    npk_ratio = models.CharField(max_length=10)  # e.g., "10-20-10"
    application_method = models.CharField(max_length=50)  # e.g., "Broadcast", "Banding", "Foliar-spray"
    application_rate = models.FloatField()  # kg/ha

    def __str__(self):
        return self.title
    
class Irrigation(FarmOperation):
    irrigation_method = models.CharField(max_length=50)  # e.g., "Drip", "Sprinkler", "Surface"
    water_volume = models.FloatField()  # m³/ha
    duration = models.DurationField()  # Duration of irrigation
    soil_moisture_pre = models.CharField(max_length=10)  # Soil moisture before irrigation

    def __str__(self):
        return self.title
    
class Planting(FarmOperation):
    seed_variety = models.CharField(max_length=100)
    seed_source = models.CharField(max_length=100)  
    planting_method = models.CharField(max_length=50)  # e.g., "Direct-seeding", "Transplanting"
    planting_density = models.FloatField()  # plants/ha
    row_spacing = models.FloatField()  # cm

    def __str__(self):
        return self.title
    
class Harvesting(FarmOperation):
    harvest_method = models.CharField(max_length=50)  # e.g., "Manual", "Mechanical"
    yield_quantity = models.FloatField()  # kg/ha
    yield_quality = models.CharField(max_length=20)
    harvest_notes = models.TextField(blank=True, null=True)  # Additional notes about the harvest

    def __str__(self):
        return self.title
    
class PesticideApplication(FarmOperation):
    pesticide_name = models.CharField(max_length=100)
    pesticide_type = models.CharField(max_length=100)
    target_pest = models.CharField(max_length=50)  # e.g., "Spray", "Granular"
    application_rate = models.FloatField()  # L/ha or kg/ha
    withholding_period = models.FloatField()  # Days before harvest

    def __str__(self):
        return self.title