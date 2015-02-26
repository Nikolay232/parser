# -*- coding: utf-8 -*-
from django.db import models


class MediaFileSequence(models.Model):

    @classmethod
    def get_next(cls):
        seq_item = cls.objects.create()
        return u'%05i' % seq_item.id
