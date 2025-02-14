from django.db  import models

"""
все объекты таблицы -- Post.objects.all() --> select * from posts

один объект по условию -- Post.objects.get(id=1)

объекты по условию не уникальному(несколько) -- Post.objects.filter(title="title")

создать объект - Post.objects.create(title="fghj", content="njkl")

"""

    # =======
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    #=====

class Post(models.Model):
    title = models.CharField(max_length=156)
    content = models.CharField(max_length=1056)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)# Связь с Category (один ко многим)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)# Связь с Tag (многие ко многим)


    def __str__(self):
        return f"{self.title} - {self.content}"





