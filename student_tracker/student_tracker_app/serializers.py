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
        read_only_fields = ('student',)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['student'] = request.user
        return super().create(validated_data)

# --- ADD THESE NEW CLASSES BELOW ---

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
        read_only_fields = ('student',) # Ensures users can't "assign" reminders to others

    def create(self, validated_data):
        # Automatically sets the student to the logged-in user
        request = self.context.get('request')
        validated_data['student'] = request.user
        return super().create(validated_data)

class PerformanceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceStatus
        fields = '__all__'