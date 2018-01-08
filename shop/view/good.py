# -*- coding:utf-8 -*-
from shop.models import Goods
from django.views.generic import ListView

_author__ = 'ZHANGJUN'


class GoodListView(ListView):
	model = Goods
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(GoodListView, self).get_context_data(**kwargs)
		return context
