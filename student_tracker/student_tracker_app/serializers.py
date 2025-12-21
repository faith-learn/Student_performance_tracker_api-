from rest_framework import serializers
from .models import Unit, Assessment, PerformanceStatus, Reminder

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'
        read_only_fields = ('student',)  # we'll set student from request

    def create(self, validated_data):
        # ensure the student is the request user
        request = self.context.get('request')
        validated_data['student'] = request.user
        return super().create(validated_data)
