from django.db.models import Avg
from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'
        )
        model = models.Review
        
    def validate_rating(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError(
            'Rating must be an integer between 1 and 5')
        
        
class CourseSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, 
                                                  read_only=True
                                           )
    
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        fields = (
            'id',
            'title',
            'url',
            'reviews',
            'average_rating'
        )
        model = models.Course
        
    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
        
        if average is None:
            return 0
        return round(average*2) / 2