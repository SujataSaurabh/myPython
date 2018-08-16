#	SuGo, 16 August 2018
#	Bitwise operators supported by Python language are
#	AND, OR, NOT, XOR, Binary left shift and Binary
#	right shift

# OPERATOR		DESCRIPTION
# Binary END (&)  -- 	operator copies a bit to teh result if it exists in both operands
# Binary OR (|)   --    operator copies a bit if it exists in either operand
# Binary XOR (^)  --	operator copies the bit if it is set in one operand but not both
# Binary Ones compliment (~) -- operator flips the bits. It is unary in nature.
# Binary left shift (<<)  --	left operands value is moved left by the number of bits specified by the right operand
# Binary right shift (>>) --	left operands value is moved right by the number of bits specified by the right operand

# Examples are explained below --

a = 60
b = 13

print("a -- ", a, "b -- ", b, "\n")
print("binary a = 0011 1100 and binary b = 0000 1101 \n")
print("AND (&) operator results ", (a & b), "\n binary 12 = 0000 1100 \n")

print("OR (|) operator results ", (a | b), "\n binary 61 = 0011 1101\n")

print("XOR (^) operator results ", (a ^ b), "\n binary 49 = 0011 0001\n")

print("Ones complimen (~) operator results on a ", ~a, "\n binary -61 = 1100 0011 \n")

print("Binary left shift (<<) operator on 'a' results  ", a<<2, "\n binary 240 = 1111 0000 \n")

print("Binary right shift (>>) operator on 'a' results ",a>>2, "\n binary 15 = 0000 1111 \n")


