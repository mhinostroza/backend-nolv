from django.db import models
from tinymce.models import HTMLField
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField, ProcessedImageField
from autoslug import AutoSlugField
from imagekit.processors import ResizeToFill


VOTED_CHOICES = (
    (0, "A Favor"),
    (1, "Abstención"),
)


class GroupPerson(models.Model):
    name = models.CharField(max_length=255)

    image = ProcessedImageField(
        upload_to='images/',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 100}
    )
    active = models.BooleanField(default=False)

    class Meta:
        db_table = 'group_person'

    def __str__(self):
        return self.name


class Person(models.Model):

    full_name = models.CharField(max_length=255)
    group_person = models.ForeignKey(
        GroupPerson,
        related_name='group_person',
        default=None,
        on_delete=models.CASCADE,
    )

    slug = AutoSlugField(
        populate_from='full_name',
        unique_with=['full_name'],
        always_update=True
    )

    education = HTMLField()
    projects = HTMLField()

    complaints = models.PositiveIntegerField(default=0, blank=False, null=False)
    sentences = models.PositiveIntegerField(default=0, blank=False, null=False)

    voted = models.IntegerField(
        choices=VOTED_CHOICES,
        default=0
    )

    photo = ProcessedImageField(
        upload_to='images/',
        processors=[ResizeToFill(390, 230)],
        format='JPEG',
        options={'quality': 100}
    )

    linkedin = models.URLField()
    informed_vote = models.URLField()

    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'person'

    def __str__(self):
        return self.full_name


