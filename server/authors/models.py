from django.db import models

class Author(models.Model):
    author_name = models.CharField(
        max_length=100, 
        primary_key=True, 
        db_column='author_name',
        default='Unknown'
    )
    year_born = models.CharField(max_length=10)
    year_died = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=60)
    books_written = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'dim_all_authors'
    
    def __str__(self):
        return self.name