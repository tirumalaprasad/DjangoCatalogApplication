from .models import Category, Subcategory, Product
from django.forms import ModelForm, inlineformset_factory


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class SubcategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        exclude = ()

SubcategoryFormSet = inlineformset_factory(Category,Subcategory,form=SubcategoryForm,extra=1)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ()
ProductFormSet = inlineformset_factory(Subcategory,Product,form=ProductForm,extra=1)


class UploadProductImage(ModelForm):
    class Meta:
        model = Product
        exclude = ()
