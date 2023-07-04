from rest_framework import serializers
from .models import PDIModel, CoilSchedule, CoilRejectModel


class PDIModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDIModel
        fields = "__all__"


class CoilScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoilSchedule
        fields = "__all__"

class RejectCoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoilRejectModel
        fields = "__all__"
