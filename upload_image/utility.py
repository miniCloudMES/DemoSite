# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   utility
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

import os
import uuid


def image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join('images', filename)
