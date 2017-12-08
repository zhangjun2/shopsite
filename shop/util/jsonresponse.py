# -*- coding:utf-8 -*-
_author__ = 'ZHANGJUN'


class JsonResponse(object):

	STATUS_SUCCESS = 'SUCCESS'
	STATUS_ERROR = 'ERROR'

	def __init__(self, status=None, successMsg=None, errorMsg=None, data=None):
		self.status = status
		self.successMsg = successMsg
		self.errorMsg = errorMsg
		self.data = data

