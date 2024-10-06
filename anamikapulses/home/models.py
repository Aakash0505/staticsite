from django.db import models
from filer.fields.image import FilerImageField,FilerFileField
from treebeard.mp_tree import MP_Node
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from meta.models import ModelMeta
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator

alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z\s\.]*$', 'Please enter only alphanumeric characters.')
alpha = RegexValidator(
    r'^[a-zA-Z\s]*$', 'Please enter only letters.')
numeric = RegexValidator(
    r'^[0-9]*$', 'Please enter only numbers.')

class Homestatic(models.Model):
    page_title = models.CharField(('Title'), max_length=1000, null=True, blank=True,)
    section_one = RichTextField(blank=True)
    section_two = RichTextField(blank=True)
    section_three = RichTextField(blank=True)
    section_four = RichTextField(blank=True)
    section_five = RichTextField(blank=True)
    section_contact = RichTextField(blank=True)
    location_map = RichTextField(blank=True)
    location_address = RichTextField(blank=True)
    header = RichTextField(blank=True)
    footer = RichTextField(blank=True)
    

    # #  basic log
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False)

    # meta tag fields / SEO friendly
    meta_title = models.CharField(
        max_length=200, null=True, blank=True, default='Anamika Pulses')
    meta_description = models.TextField(max_length=500, null=True, blank=True)
    meta_keywords = models.CharField(max_length=500, null=True, blank=True)
    other_meta_tags = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.page_title)
    

# Area Of Interest
class AreaOfInterest(MP_Node):
    title = models.CharField(('Title'), max_length=1000, null=True, blank=True)

        # #  basic log
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Area Of Interest'
        verbose_name_plural = 'Area Of Interest'   

    
# Team
class Team(MP_Node):
    name = models.CharField(('Title'), max_length=1000, null=True, blank=True)
    designation = models.CharField(('Designation'), max_length=1000, null=True, blank=True)
    image  = FilerFileField(related_name='profile_image',
                                            null=True,
                                            blank=True,
                                            on_delete=models.SET_NULL
                                            )

        # #  basic log
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'   


# Product Category
class Category(MP_Node):
    name = models.CharField(('Title'), max_length=1000, null=True, blank=True)

        # #  basic log
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'



# Product
class Product(MP_Node):
    category = models.ForeignKey(Category, null=True,on_delete=models.CASCADE, related_name="product_category" )
    name = models.CharField(('Name'), max_length=1000, null=True, blank=True)
    description = models.CharField(('Description'), max_length=1000, null=True, blank=True)
    image  = FilerFileField(related_name='product_image',
                                            null=True,
                                            blank=True,
                                            on_delete=models.SET_NULL
                                            )

        # #  basic log
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'   
    




class Contact(models.Model):
    name = models.CharField(max_length=50, validators=[alpha])
    email_id = models.EmailField(max_length=100)
    contact_no = models.CharField(max_length=13, null=True, blank=True, validators=[numeric])
    area_of_interest = models.CharField(max_length=80)
    message = models.TextField(max_length=250, validators=[
                             alphanumeric], null=True, blank=True)
    document = models.FileField(
        null=True, blank=True, upload_to='uploads/Careers/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])])
# basic log
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'