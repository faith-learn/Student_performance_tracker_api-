from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Unit, Assessment, Reminder
from .utils import calculate_performance_status


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"

    def validate_marks(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Marks must be between 0 and 100.")
        return value

    def create(self, validated_data):
        marks = validated_data.get("marks")
        validated_data["status"] = calculate_performance_status(marks)
        return super().create(validated_data)


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = "__all__"
