from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('van', 'Van'),
        ('truck', 'Truck'),
    ]

    type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type.capitalize()} - {self.model} ({self.license_plate})"
