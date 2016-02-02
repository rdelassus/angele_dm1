# coding=utf-8

import unittest
from unitTest import unitTests

from algo import (
    angele_algo,
    angele_algo2,
    angele_algo3
)
from algo import (
    convexe,
    intersection,
    paralleles,
    sur_segment
)
from algo import (
    RECTANGLE,
    CARRE,
    LOSANGE,
    PARALLELOGRAMME,
    QUELCONQUE,
    TRAPEZE
)


class algoTests(unitTests):

    def test_quelconque(self):
        """ test si un quadrilatere quelconque est reconnu
        en tant que tel
        """
        A = (1., 3.)
        B = (2., 4.)
        C = (5., 0.)
        D = (0., 1.)
        assert(angele_algo(A, B, C, D) == QUELCONQUE)
        assert(angele_algo2(A, B, C, D) == QUELCONQUE)
        assert(angele_algo3(A, B, C, D) == QUELCONQUE)

    def test_losange(self):
        """ test si un losagnge est reconnu
        en tant que tel
        """
        A = (3., 1.)
        B = (4., 3.)
        C = (6., 4.)
        D = (5., 2.)
        assert(angele_algo(A, B, C, D) == LOSANGE)
        assert(angele_algo2(A, B, C, D) == LOSANGE)
        assert(angele_algo3(A, B, C, D) == LOSANGE)

    def test_rectangle(self):
        """ test si un rectangle est reconnu
        en tant que tel
        """
        A = (0., 0.)
        B = (0., 3.)
        C = (1., 3.)
        D = (1., 0.)
        assert(angele_algo(A, B, C, D) == RECTANGLE)
        assert(angele_algo2(A, B, C, D) == RECTANGLE)
        assert(angele_algo3(A, B, C, D) == RECTANGLE)

    def test_carre(self):
        """ test si un carre est reconnu
        en tant que tel
        """
        A = (0., 0.)
        B = (0., 1.)
        C = (1., 1.)
        D = (1., 0.)
        assert(angele_algo(A, B, C, D) == CARRE)
        assert(angele_algo2(A, B, C, D) == CARRE)
        assert(angele_algo3(A, B, C, D) == CARRE)

    def test_para(self):
        """ test si un parallelogramme quelconque est reconnu
        en tant que tel
        """
        A = (0., 0.)
        B = (0., 3.)
        C = (1., 4.)
        D = (1., 1.)
        assert(angele_algo(A, B, C, D) == PARALLELOGRAMME)
        assert(angele_algo2(A, B, C, D) == PARALLELOGRAMME)
        assert(angele_algo3(A, B, C, D) == PARALLELOGRAMME)

    def test_trapeze(self):
        """ test si un trapeze est reconnu
        en tant que quelconque
        """
        A = (1., 0.)
        B = (3., 0.)
        C = (0., 3.)
        D = (0., 1.)
        assert(angele_algo(A, B, C, D) == QUELCONQUE)
        assert(angele_algo2(A, B, C, D) == QUELCONQUE)
        assert(angele_algo3(A, B, C, D) == TRAPEZE)

    def test_concave(self):
        """ test si un quadrilatere concave est reconnu
        """
        A = (0., 3.)
        B = (4., 3.)
        C = (2., 2.)
        D = (3., 0.)
        assert(not convexe(A, B, C, D))

    def test_convexe(self):
        """ test si un quadrilatere convexe est reconnu
        """
        A = (1., 3.)
        B = (2., 4.)
        C = (5., 0.)
        D = (0., 1.)
        diag1 = (A, C)
        diag2 = (B, D)
        K = intersection(diag1, diag2)
        assert(K is not None)
        assert(sur_segment(K, diag1))
        assert(sur_segment(K, diag2))
        assert(convexe(A, B, C, D))

    def test_parallele(self):
        """ckeck si deux droites sont paralleles"""
        A = (0., 0.)
        B = (1., 2.)
        C = (3., 0.)
        D = (4., 2.)
        assert(paralleles((A, B), (C, D)))

    def test_intersection1(self):
        """ckeck intersection d'un segment vertical et un segment horizontal"""
        A = (0., 0.)
        B = (0., 2.)
        C = (-1., 1.)
        D = (1., 1.)
        assert(intersection((A, B), (C, D)) == (0, 1))

    def test_intersection2(self):
        """ckeck intersection de deux segments quelconques sécants"""
        A = (0., 0.)
        B = (2., 2.)
        C = (0., 2.)
        D = (2., 0.)
        assert(intersection((A, B), (C, D)) == (1, 1))

    def test_non_intersection1(self):
        """ckeck intersection de deux segments parallèles"""
        A = (0., 0.)
        B = (1., 2.)
        C = (3., 0.)
        D = (4., 2.)
        assert(intersection((A, B), (C, D)) is None)

    def test_non_intersection2(self):
        """ckeck intersection de deux segments non sécants
        apprtenant à deux droites séquentes"""
        A = (0., 0.)
        B = (0., 1.)
        C = (-1., 2.)
        D = (1., 2.)
        K = intersection((A, B), (C, D))
        assert(K is not None)
        assert(not sur_segment(K, (A, B)) or not sur_segment(K, (C, D)))


if __name__ == '__main__':
    unittest.main()
