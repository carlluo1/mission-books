from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=255, help_text='e.x fakeemail@gmail.com',
            null=True)
    GENRE_TYPE = (
        ('d', 'N/A'),
        ('a', 'ACT Test Prep'),
        ('b', 'Study Guide'),
        ('c', 'AP Test Prep'),
        ('e', 'SAT Test Prep'),
        ('f', 'SAT Subject Test Prep'),
        ('g', 'Textbook'),
        ('h', 'Workbook'),
    )
    genre = models.CharField(max_length=1, choices=GENRE_TYPE, blank=True,
        default='d', help_text='Select a Genre, do not leave blank')
    academic_subject = models.CharField(max_length=255,
        help_text='e.x Physics, Biology')
    year = models.CharField(max_length=255, help_text='e.x 1999', null=True)
    price = models.CharField(max_length=255,
        help_text='e.x 3.00, leave out the dollar sign', null=True)
    phone_number = models.CharField(max_length=255,
        help_text='e.x 111-111-1111', null=True)
    additional_comments = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    class Meta:
        ordering = ["title", "published_date"]
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)
