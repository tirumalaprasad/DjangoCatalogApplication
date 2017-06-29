from django.conf.urls import url
from . import views


urlpatterns = [
    # /catalog/
    url(r'^$', views.index, name='index',),

    # /catalog/departments/
    url(r'^departments/$',views.departments,name='departments'),

    # /catalog/2/category/
    url(r'^(?P<category_id>[0-9]+)/category/$',views.category,name='category'),

    # /catalog/2/subcategory/
    url(r'^(?P<subcategory_id>[0-9]+)/subcategory/',views.subcategory,name='subcategory'),

    # /catalog/3/product/
    url(r'^(?P<product_id>[0-9]+)/product/',views.product,name='product'),

    # /catalog/add-category/
    url(r'^add-category/$',views.add_category,name='add_category'),

    # /catalog/add-category/
    url(r'^add-subcategory/$',views.add_subcategory,name='add_subcategory'),

    # /catalog/add-product/
    url(r'^add-product/$',views.add_product,name='add_product'),
]
