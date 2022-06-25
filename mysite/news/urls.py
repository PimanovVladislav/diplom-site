from django.urls import path
from news.views import *

urlpatterns = [

    path('',index),
    path('about_us',about_page),
    path('recomended',recommend_by_like), ##
    path('daterank',daterank),
    path('search',search),
    path(f'readmore/<int:news_id>', read_more),
    path(f'category/<int:category_id>',get_category),
    path(f'like/<int:news_id>',click_like)
]