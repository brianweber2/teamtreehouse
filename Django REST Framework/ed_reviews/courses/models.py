from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(Course, related_name='reviews')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['email', 'course']
    
    def __str__(self):
        return '{0.rating} by {0.email} for {0.course}'.format(self)