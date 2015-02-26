# -*- coding: utf-8 -*-
from __future__ import with_statement

from django.conf import settings, UserSettingsHolder
from django.utils.functional import wraps


def diff_tuple(original_tuple, deleted_elements):
    original_list = list(original_tuple)

    result_list = [element for element in original_list if element not in deleted_elements]
    return tuple(result_list)


def sizeof_fmt(num):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')
