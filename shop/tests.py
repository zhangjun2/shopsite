import os
import random
import string

import re
from collections import Counter

import math
from django.test import TestCase


# Create your tests here.

def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


# print(power(5, 2))
# print(power(4))
# print(power(3))

# ---------------------0001开始------------------------
# --生成200个激活码，20位
def generate(count, length, isgroup, indent=4):
	forselect = string.ascii_letters + "0123456789"
	l = []
	print(string.ascii_letters)
	for x in range(count):
		re = ""
		for y in range(length):
			if not isgroup:
				re += random.choice(forselect)
			else:
				if y % indent == 0 and y != 0:  # 需要分组，按每组的字母个数，中间加上'-'横杠分隔
					re += ("-" + random.choice(forselect))
				else:
					re += random.choice(forselect)
		l.append(re)
	return l


# print(generate(10, 20, True, indent=5))
# ---------------------0001结束------------------------------


# ------------------------0004开始-------------------------
# 统计一个文件中的英文单词，每个英文单词的个数
def word_count(txt):
	pattern = r'[a-zA-Z]+'
	words = re.findall(pattern, txt)
	# Counter(words).items()返回一个列表中各个元素出现次数的列表，列表的每个元素为一个tuple，tuple的第一个值为元素的值，第二个为元素出现的次数
	return Counter(words).items()


# 统计出现次数最多的元素
def word_most_count(txt):
	pattern = r'[a-zA-Z]+'
	words = re.findall(pattern, txt)
	# ****return Counter(words).most_common(1)返回要统计的列表中出现次数最多的元素 most_common的参数为次数最多的元素的个数。如数量最多的前三个元素，参数则为3
	return Counter(words).most_common(1)


# 打开文件的路径斜杠要转义，用双斜杠标示
# if __name__ == '__main__':
# 	txt = open('D:\\Users\\zhangjun693\Desktop\\test-0004.txt', 'r').read()
# 	print(word_count(txt))
# 	for x in word_count(txt):
# 		print(x)
# 		if x[0] == 'i':
# 			print(x)

# ------------------------0004结束-------------------------



# ------------------------0006开始-------------------------

# 利用0004中统计文字中单词出现的次数函数word_count()

# dir = 'D:\\Users\\zhangjun693\Desktop\\test\\'
# file_list = os.listdir(dir)
# for filename in file_list:
# 	with open(dir + filename, 'r') as f:
# 		print(filename, word_most_count(f.read()))

# ------------------------0006结束-------------------------


# d = {'2': 3, '3': 2, '17': 2, '2':4}
# d ='aaaffbbbd'
# d['2'] = 4
# <editor-fold desc="Description">
# print(Counter(d).update('a123'))
# print(Counter(d))
#
# class Animal(object):
# 	def run(self):
# 		print('animal is running')
#
# class Dog(Animal):
# 	def run(self):
# 		print('dog is running')
#
# class Sf(object):
# 	def run(self):
# 		print('gffffffffffff')
#
# def runtwice(animal):
# 	if isinstance(animal,Animal):
# 		animal.run()
#
# runtwice(Dog())
# runtwice(Sf())
# print(dir(Dog()))
# </editor-fold>


# test01 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
def test01():
	L = []
	for x in range(1, 5):
		for y in range(1, 5):
			for i in range(1, 5):
				if x != y and y != i and x != i:
					L.append(str(x) + str(y) + str(i))
				# print(x,y,i)
	print('总共有', len(L), '个', L)


# test01()

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def test02():
	for i in range(1, 10000):
		x = int(math.sqrt(i + 100))  # 转换成整数，如果平方根为整数，则转换为整数后该数的平方等于开平方根的数
		y = int(math.sqrt(i + 268))
		if x * x == (i + 100) and y * y == (i + 268):
			print(i, "  ", x, "      ", y)


# test02()

def test03():
	L = []
	for x in range(3):
		k = int(input("请输入："))
		L.append(k)
	L.sort()
	print(L)


# test03()

# <editor-fold desc="迭代测试">
# for x in [(1, 1), (2, 4), (3, 9)]:
# 	print(x)
#
# for i, value in enumerate([(1, 1), (2, 4), (3, 9)]):
# 	print(i, " ",  value)
# </editor-fold>


def test04():
	for i in range(1, 10):  # 行
		for j in range(1, i + 1):
			if j != i:
				print(j, '*', i, '=', i * j, '   ', end='')
			else:
				print(j, '*', i, '=', i * j, '   ')


# test04()


# 打印杨辉三角
def test05(leng):
	l = []
	a, b, n = 1, 0, 1
	while n < leng:
		if n == 1 or n == 2:
			l.append(1)
		yield l
		for i, x in enumerate(l):
			if i < len(l) - 1:
				l.append(l[i] + l[i + 1])
		n = n + 1
	return 'done'

# g = test05(10)
# for x in g:
# 	print(x)
# print(type(g))


def test06():
	lst = [1, 3, 5, 8, 10, 13, 18, 36, 78]
	new_list = list(x for x in lst[::2] if x%2==0)
	return new_list

# print(test06())
