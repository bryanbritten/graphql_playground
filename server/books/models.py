from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author_name = models.ForeignKey(
        'authors.author',
        related_name='authors',
        verbose_name='author_name',
        db_column='author_name',
        default='Unknown',
        on_delete=models.SET_DEFAULT
    )
    year_published = models.CharField(max_length=10)
    review = models.FloatField()

    class Meta:
        db_table = "dim_all_books"
    
    def __str__(self):
        return self.title