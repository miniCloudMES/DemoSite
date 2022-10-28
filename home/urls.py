# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   urls
  Description : MiniMES Company
  Author :    Karo Lin
  date：     2022/10/26
  Copyright follow MIT definitions.
-------------------------------------------------
  Change Activity:
          2022/10/26:
-------------------------------------------------
"""
__author__ = 'Karo Lin'

from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index')
]
