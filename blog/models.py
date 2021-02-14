from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from taggit.managers import TaggableManager
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator

def blog_thumbnail_directory_path(instance, filename):
    return 'user_{0}/blog/{1}/thumbnail/{2}'.format(instance.author.id, instance.title, filename)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)

class Blog(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to=blog_thumbnail_directory_path, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = RichTextUploadingField()
    views= models.IntegerField(default=0)
    tags=TaggableManager(help_text="Tag your blog here")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title + '- by ' + self.author.username

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.thumbnail.url))
    admin_photo.short_description = "Blog Thumbnail"
    admin_photo.allow_tags = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args,**kwargs)

class BlogComment(models.Model):
    user=models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    comment=models.TextField()
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "---" + "by" + " " + self.user.username

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.post.thumbnail.url))
    admin_photo.short_description = "Blog Thumbnail"
    admin_photo.allow_tags = True
    
    

    
