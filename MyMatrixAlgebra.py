class MyMatrixAlgebraElement(CombinatorialFreeModule.Element):
    def __init__(self, *args, **kwargs):
        CombinatorialFreeModule.Element.__init__(self, *args, **kwargs)

    def _listify(self):
        P = self.parent()
        n = P._n
        R = P._R
        my_list = [[R.zero()]*n for _ in range(n)]
        mcs = self.monomial_coefficients()
        for mc in mcs:
            i, j = mc[0], mc[1]
            my_list[i][j] = mcs[mc]
        return my_list

    def _repr_(self):
        my_list = self._listify()
        my_string = ''
        for row in my_list:
            my_string += str(row) + '\n'
        my_string = my_string[:-1]
        return my_string

    def _latex_(self):
        n = self.parent()._n
        my_list = self._listify()
        the_string = '\\left(\\begin{array}{%s}\n'%('r'*n)
        for row in my_list:
            for item in row:
                the_string += latex(item) + '&'
            the_string = the_string[:-1] + '\\\\\n'
        the_string = the_string[:-3]
        the_string += '\n\\end{array}\\right)'
        return the_string

class MyMatrixAlgebra(CombinatorialFreeModule):

    # Element = MyMatrixAlgebraElement

    def __init__(self, R, n, *args, **kwargs):
        self._n = n
        self._R = R
        indices = [(i, j) for i in range(n) for j in range(n)]

        # Comment one of the following two lines:
        # CombinatorialFreeModule.__init__(self, R, indices, category=AlgebrasWithBasis(R), *args, **kwargs)
        CombinatorialFreeModule.__init__(self, R, indices, *args, **kwargs)

    def _repr_(self):
        return "My %s by %s matrix algebra over %s"%(self._n, self._n, self._R)

    def product_on_basis(self, left, right):
        if left[1] != right[0]:
            return self.zero()
        else:
            return self.monomial((left[0], right[1]))

    def one(self):
        return self.sum([self.monomial((i, i)) for i in range(self._n)])

    def matrix(self, L):
        n = self._n
        errmsg = "input should be a length %s list of length %s lists"%(n, n)
        if len(L) != n:
            raise ValueError(errmsg)
        for item in L:
            if len(item) != n:
                raise ValueError(errmsg)
        sum = self.zero()
        for i in range(n):
            for j in range(n):
                sum += L[i][j]*self.monomial((i, j))
        return sum
