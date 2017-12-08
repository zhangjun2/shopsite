# -*- coding:utf-8 -*-
_author__ = 'ZHANGJUN'


# test01 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

def test01():
	L = []
	for x in range(1, 5):
		for y in range(1, 5):
			for i in range(1, 5):
				if x != y or y != i or x != i:
					L.append(x, y, i)
				# print(x,y,i)
	print('总共有', len(L), '个', L)

test01()
