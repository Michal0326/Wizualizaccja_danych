import numpy

a = numpy.arange(2)
print(a)
print(type(a))

print(a.dtype)
a = numpy.array(['a', 'b', 'c', 1, 2, 3])
print(a)

a = numpy.arange(2, dtype='int32')
print(a.dtype)
b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)

m = numpy.array((numpy.arange(2), numpy.arange(2)))
print(m)
print(m.shape)

m0 = numpy.array([[2, 1, 3],
                  [5, 4, 8]], dtype='float')
print(m0)

zera = numpy.zeros((5, 5))
jedynki = numpy.ones((4, 4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = numpy.empty((2, 2))
print(pusta)
poz_1 = pusta[1, 1]
poz_2 = pusta[0, 1]
print(poz_1)
print(poz_2)

liczby = numpy.arange(1, 2, 0.1)
print(liczby)

liczby_lin = numpy.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)

z = numpy.indices((5, 3))
print(z)
print(z.shape)
print(z[0, 2, 1])

x, y = numpy.mgrid[0:5, 0:5]
print(x)
print(y)

mat_diag_k = numpy.diag([a for a in range(5)], -1)
print(mat_diag_k)

z = numpy.fromiter(range(5), dtype='int32')
print(z)

znaki = b'abcdef'
zn1 = numpy.frombuffer(znaki, dtype='S1')
print(zn1)
zn2 = numpy.frombuffer(znaki, dtype='S3')
print(zn2)

znaki0 = 'abcdef'
zn3 = numpy.array(list(znaki0))
zn4 = numpy.array(list(znaki0), dtype='S1')
zn5 = numpy.array(list(b'abcdef'))
zn6 = numpy.fromiter(znaki0, dtype='S1')
zn7 = numpy.fromiter(znaki0, dtype='U1')
print(zn3)
print(zn4)
print(zn5)
print(zn6)
print(zn7)

mat = numpy.ones((2, 2))
mat_1 = numpy.ones((2, 2))
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat * mat_1)
print(mat / mat_1)

a = numpy.dot(mat, mat_1)
print(a)
b = mat.dot(mat_1)
mat *= mat_1
print(mat)

a0 = numpy.arange(10)
print(a0)
s = slice(2, 7, 2)
print(a0[s])
s = range(2, 7, 2)
print(a0[s])
print(a0[2:7:2])
print(a0[1:])
print(a0[2:5])

mat_0 = numpy.arange(25)

mat_0 = mat_0.reshape((5, 5))

print(mat_0[1:])
print(mat_0[:, 1])
print(mat_0[:, -1])
print(mat_0[2:6, 1:3])
print(mat_0[:, range(2, 6, 2)])
print('')

x1 = numpy.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8],
                  [9, 10, 11]])
print(x1)

rows = numpy.array([[0, 0], [3, 3]])
cols = numpy.array([[0, 2], [0, 2]])
y = x1[rows, cols]
print(y)



