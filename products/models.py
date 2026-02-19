from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_(
        'parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    descrption = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_("image"), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_("is enable"), default=True)
    create_time = models.DateTimeField(_('time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.CharField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='product/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField(
        'Category', verbose_name=_('categories'), blank=True)
    create_time = models.DateTimeField(_('time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_(
        'product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='files/%y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    create_time = models.DateTimeField(_('time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update'), auto_now=True)

    class Meta:
        db_table = 'file'
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self):
        return self.title
