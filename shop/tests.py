from django.test import TestCase

# Create your tests here.

def power(x,n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


print(power(5, 2))
print(power(4))
print(power(3))


