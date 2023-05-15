from django.db import models
from django.urls import reverse


class Position(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug_for_position = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Опис')
    photo = models.ImageField(upload_to="photos/%Y/%m/", verbose_name='Фото')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Ціна')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата останніх змін')
    published = models.BooleanField(default=True, verbose_name='Опубліковано')
    in_box = models.BooleanField(default=False, verbose_name='В корзині')
    categories = models.ForeignKey('Categories',
                                   on_delete=models.PROTECT,
                                   verbose_name='Категорія в позиціях')

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # return absolute url address of the model
        return reverse('show_position',
                       kwargs={'name_of_categories': Categories.objects.get(id=self.categories_id).slug_for_categories,
                               'position_slug': self.slug_for_position,
                               })  # reverse is return as url

    class Meta:
        '''вкладений клас який використовується адмінкою для налаштування класу Position '''
        verbose_name = 'Товарна одиниця'
        verbose_name_plural = 'Товарні одиниці'
        ordering = ['-time_update', 'title']


class Categories(models.Model):
    categories_name = models.CharField(max_length=100, db_index=True, verbose_name='Назва категорії')
    slug_for_categories = models.SlugField(max_length=255, unique=True, verbose_name='Слаг для категорії')

    def __str__(self):
        return self.categories_name

    def get_absolute_url(self):
        return reverse('show_positions', kwargs={'name_of_categories': self.slug_for_categories})

    class Meta:
        '''вкладений клас який використовується адмінкою для налаштування класу Categories '''
        verbose_name = 'Категорія товару'
        verbose_name_plural = 'Категорії товарів'
        ordering = ['categories_name']
