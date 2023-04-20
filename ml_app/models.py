from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.ensemble import RandomForestClassifier
import joblib

# Create your models here.

RE = (
    (1, 'Has concept note'),
    (0, 'Has no concept note'),
)
class Data(models.Model):
    NAME = models.CharField(max_length=100, null=True)
    UGPA = models.FloatField(validators = [MaxValueValidator(5),MinValueValidator(0)], null=True)
    RCN = models.PositiveIntegerField(choices=RE, null=True)
    TOEFL = models.FloatField(validators = [MaxValueValidator(120),MinValueValidator(0)],null=True)
    LOR = models.PositiveIntegerField(validators = [MaxValueValidator(5),MinValueValidator(0)],null=True)
    SOP = models.FloatField(validators = [MaxValueValidator(5),MinValueValidator(0)],null=True)
    PROBABILITY = models.FloatField(validators = [MaxValueValidator(1),MinValueValidator(0)],null=True)
    STATUS = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/masters_intern.joblib')
        self.STATUS = ml_model.predict([[self.UGPA, self.RCN, self.TOEFL, self.LOR, self.SOP, self.PROBABILITY]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.NAME
