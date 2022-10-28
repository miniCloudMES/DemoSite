# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   urls
  Description : MiniMES Company
  Author :    Karo Lin
  date：     2022/10/25
  Copyright follow MIT definitions.
-------------------------------------------------
  Change Activity:
          2022/10/25:
-------------------------------------------------
"""
__author__ = 'Karo Lin'

from django.urls import path

from upload_image import views

app_name = 'upload_image'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:image_id>/delete/', views.delete, name='delete'),
    path('<int:image_id>/update/', views.update, name='update'),
]
