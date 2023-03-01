from django.db import models


class IrisInput(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    inputFeatures = models.JSONField()


class IrisOutput(models.Model):
    irisInput = models.ForeignKey(IrisInput, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    modelVersion = models.CharField(max_length=20, default='')
    outputPredictions = models.JSONField()
