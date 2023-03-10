from rest_framework import serializers

from .models import IrisInput, IrisOutput


class IrisInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrisInput
        ordering = ['created']
        read_only_fields = [
            'id',
            'created'
        ]
        fields = [
            'id',
            'title',
            'created',
            'inputFeatures',
        ]


class IrisOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrisOutput
        ordering = ['created']
        read_only_fields = [
            'id',
            'created',
            'irisInput',
        ]
        fields = [
            'id',
            'title',
            'irisInput',
            'created',
            'modelVersion',
            'outputPredictions'
        ]
