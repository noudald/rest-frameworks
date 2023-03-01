import json
import numpy as np

from django.contrib.auth.models import User

from rest_framework import generics, permissions

from .models import IrisInput, IrisOutput
from .serializers import IrisInputSerializer, IrisOutputSerializer


class IrisInputList(generics.ListCreateAPIView):
    queryset = IrisInput.objects.all()
    serializer_class = IrisInputSerializer

    def perform_create(self, serializer):
        input_features = json.loads(self.request.POST.get('inputFeatures'))

        iris_input = serializer.save()

        IrisOutput(
            irisInput=iris_input,
            title=self.request.POST.get('title'),
            modelVersion='0.1',
            outputPredictions=[0.0]
        ).save()


class IrisInputDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IrisInput.objects.all()
    serializer_class = IrisInputSerializer


class IrisOutputList(generics.ListAPIView):
    queryset = IrisOutput.objects.all()
    serializer_class = IrisOutputSerializer


class IrisOutputDetail(generics.RetrieveAPIView):
    queryset = IrisOutput.objects.all()
    serializer_class = IrisOutputSerializer
