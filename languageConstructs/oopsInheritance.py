#	SuGo, 16 August 2018
#	This program implements the concept of inheritance in python

# PART1 : Check if a class is a subclass of another

class Base(object):
	pass

#
class Derived(Base):
	pass
#

# 	** ** 
print("issubclass(Derived, Base) ", issubclass(Derived, Base))
print("issubclass(Base, Derived) ", issubclass(Base, Derived))

d = Derived()
b = Base()

print("Is b the instance od derived class ", isinstance(b, Derived))
print("Is d the instance od Derived class ", isinstance(d, Derived))
