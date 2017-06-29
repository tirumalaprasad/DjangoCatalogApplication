from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.template import loader
from .models import Category, Subcategory, Product
from .forms import CategoryForm, SubcategoryForm, ProductForm

def index(request):
    try:
        product_list = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("No Products")
    template = loader.get_template('index.html')
    context = {
        'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))


def departments(request):
    try:
        department_list = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404("No Departments")
    template = loader.get_template('departments.html')
    context = {
        'department_list': department_list,
    }
    return HttpResponse(template.render(context, request))


def category(request,category_id):
    try:
        category_list = Subcategory.objects.filter(category=category_id)
    except Subcategory.DoesNotExist:
        raise Http404("No Categories")
    template = loader.get_template('category.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))


def subcategory(request,subcategory_id):
    print(subcategory_id)
    try:
        subcategory_list = Product.objects.filter(subcategory=subcategory_id)
    except Product.DoesNotExist:
        raise Http404("No Products")
    template = loader.get_template('subcategory.html')
    context = {
        'subcategory_list': subcategory_list,
    }
    return HttpResponse(template.render(context, request))


def product(request, product_id):
    try:
        product_details = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    template = loader.get_template('product.html')
    context = {
        'product_details': product_details,
    }
    return HttpResponse(template.render(context, request))


def add_category(request):
    form_class = CategoryForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            obj = Category()
            obj.title = form.cleaned_data['title']
            obj.description = form.cleaned_data['description']
            obj.save()
            return redirect('departments')
    return render(request, 'add_new.html', {'form_class': form_class})


def add_subcategory(request):
    form_class = SubcategoryForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            obj = Subcategory()
            obj.category = form.cleaned_data['category']
            obj.sub_title = form.cleaned_data['sub_title']
            obj.sub_description = form.cleaned_data['sub_description']
            obj.save()
            return redirect('index')
    return render(request, 'add_new.html', {'form_class': form_class})


def add_product(request):
    form_class = ProductForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            obj = Product()
            obj.subcategory = form.cleaned_data['subcategory']
            obj.name = form.cleaned_data['name']
            obj.info = form.cleaned_data['info']
            obj.price = form.cleaned_data['price']
            obj.save()
            return redirect('index')
    return render(request, 'add_new.html', {'form_class': form_class})