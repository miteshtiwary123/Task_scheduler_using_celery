"""Model for celery app"""
from django.db import models

class SoftwareDetails(models.Model):
    """All the field"""
    descriptions = models.CharField(max_length=255)
    yearly_cost = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    support_end = models.DateField()
    renewal_date = models.DateField()
    remark = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.EmailField()
    vendor_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descriptions
