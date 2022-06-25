from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name = "Тег")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

class New(models.Model):
    title = models.CharField(max_length=150,verbose_name = "Заголовок")
    content = models.TextField(blank=True,verbose_name = "Контент")
    date_published = models.DateTimeField(auto_now_add=True,verbose_name = "Дата публикации")
    likes = models.IntegerField(verbose_name = "Понравилось",default = 0)
    is_published = models.BooleanField(default = True,verbose_name = "Статус публикации")
    tags = models.ForeignKey('Tags', on_delete = models.PROTECT, null = True,blank = True,verbose_name = "Теги")#
    keywords = models.CharField(max_length=150,verbose_name = "Ключевые слова",default = "")
    photo = models.ImageField(upload_to ='photos/%Y/%m/%d', verbose_name='Фото',blank = True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ['-date_published','title']
