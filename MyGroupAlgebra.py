from sage.categories.tensor import tensor

class MyGroupAlgebra(CombinatorialFreeModule):
    def __init__(self, R, G, *args, **kwargs):
        '''
        Which instance variables are important? Which object should you use to
        index a basis for this algebra? Which category should you use?
        '''
        pass

    def __repr__(self):
        pass

    def product_on_basis(self, left, right):
        '''
        left and right are two elements of G. These two elements correspond
        to two elements of this group algebra. This function should return the
        product of those two elements.
        '''
        pass

    def one_basis(self):
        '''
        This function should return the element of G whose corresponding group
        algebra element is the identity of the algebra.
        '''
        pass


    # Implement the following if you know what a Hopf Algebra is.

    def coproduct_on_basis(self, g):
        '''
        g is an element of G. This function should return the co-multiplication
        of the corresponding group algebra element.
        '''
        pass

    def antipode_on_basis(self, g):
        '''
        g is an element of G. This function should return the antipode of the
        group algebra element corresponding to g.
        '''
        pass

    def counit_on_basis(self, g):
        '''
        g is an element of G. This function should return the field element
        which is the counit applied to the group algebra element corresponding
        to g.
        '''
        pass
