# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# A grid means that you could potentially break it into rows and columns, like here:

# 7	i	3
# T	s	i
# h	%	x
# i		#
# s	M	
# $	a	
# #	t	%
# ^	r	!

# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix.

a = ["7This$#^", "is% Matr", "3ix#  %!"]

def decrypt_msg(a):
    res = ""
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j].isalpha():
                res += a[i][j]
            else:
                res += " "
    return (" ".join(res.split()))

res = decrypt_msg(a)
print(res)

