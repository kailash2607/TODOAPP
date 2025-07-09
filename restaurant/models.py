from django.db import models

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    table_number = models.IntegerField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"Table {self.table_number} - {self.customer_name} on {self.date}"
