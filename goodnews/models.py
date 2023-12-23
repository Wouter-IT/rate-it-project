from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Pusblished"))

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_post")
    edited_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    reported = models.BooleanField(default=False)
    reports = models.ManyToManyField(Uer, related_name="post_report_count")
        
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)
    reported = models.BooleanField(default=False)
    reports = models.ManyToManyField(Uer, related_name="post_reports_count")

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"