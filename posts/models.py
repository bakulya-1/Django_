from django.db  import models

"""
все объекты таблицы -- Post.objects.all() --> select * from posts

один объект по условию -- Post.objects.get(id=1)

объекты по условию не уникальному(несколько) -- Post.objects.filter(title="title")

"""


class Post(models.Model):
    title = models.CharField(max_length=156)
    content = models.CharField(max_length=1056)
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.content}"



