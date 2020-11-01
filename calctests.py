import unittest
from calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 3), 6)
 
    def test_sub2(self):
        c = Calculator()
        self.assertEqual(c.sub(6, 3), 3)

    def test_sub3(self):
        c = Calculator()
        self.assertEqual(c.sub(4, 3), 1)

    def test_mul(self):
        c = Calculator()
        self.assertEqual(c.mul(5, 4), 20)

    def test_mul2(self):
        c = Calculator()
        self.assertEqual(c.mul(4, 4), 16)

    def test_mul3(self):
        c = Calculator()
        self.assertEqual(c.mul(5, 6.5), 32.5)

    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div(4, 2), 2)

    def test_div2(self):
        c = Calculator()
        self.assertEqual(c.div(4, 2.0), 2.0)

    def test_div3(self):
        c = Calculator()
        self.assertEqual(c.div(6, 6), 1)

    def test_sqr(self):
        c = Calculator()
        self.assertEqual(c.sqr(4), 16)

    def test_sqr2(self):
        c = Calculator()
        self.assertEqual(c.sqr(2.0), 4.0)

    def test_sqr3(self):
        c = Calculator()
        self.assertEqual(c.sqr(8), 64)

    def test_sqroot(self):
        c = Calculator()
        self.assertEqual(c.sqroot(2), 1.4142)

    def test_sqroot2(self):
        c = Calculator()
        self.assertEqual(c.sqroot(5), 2.2361)

    def test_sqroot3(self):
        c = Calculator()
        self.assertEqual(c.sqroot(4), 2.0)

    def test_log(self):
        c = Calculator()
        self.assertEqual(c.log(2), 0.301)

    def test_log2(self):
        c = Calculator()
        self.assertEqual(c.log(6), 0.7782)

    def test_log3(self):
        c = Calculator()
        self.assertEqual(c.log(9.0), 0.9542)

    def test_ilog(self):
        c = Calculator()
        self.assertEqual(c.ilog(2), 100.0)

    def test_ilog2(self):
        c = Calculator()
        self.assertEqual(c.ilog(6.0), 1000000.0)

    def test_ilog3(self):
        c = Calculator()
        self.assertEqual(c.ilog(3), 1000.0)

    def test_nlog(self):
        c = Calculator()
        self.assertEqual(c.nlog(4), 1.3863)

    def test_nlog2(self):
        c = Calculator()
        self.assertEqual(c.nlog(3), 1.0986)

    def test_nlog3(self):
        c = Calculator()
        self.assertEqual(c.nlog(8), 2.0794)

    def test_inlog(self):
        c = Calculator()
        self.assertEqual(c.inlog(5), 148.4132)

    def test_inlog2(self):
        c = Calculator()
        self.assertEqual(c.inlog(2), 7.3891)

    def test_inlog3(self):
        c = Calculator()
        self.assertEqual(c.inlog(5), 148.4132)

    def test_floor(self):
        c = Calculator()
        self.assertEqual(c.floor(3.9), 3)

    def test_floor2(self):
        c = Calculator()
        self.assertEqual(c.floor(5.1), 5)

    def test_floor3(self):
        c = Calculator()
        self.assertEqual(c.floor(0.9), 0)

    def test_ceil(self):
        c = Calculator()
        self.assertEqual(c.ceil(3.1), 4)

    def test_ceil2(self):
        c = Calculator()
        self.assertEqual(c.ceil(5.9), 6)

    def test_ceil3(self):
        c = Calculator()
        self.assertEqual(c.ceil(10.9), 11)

<<<<<<< HEAD
    def test_exponentiation1(self):
        c = Calculator()
        self.assertEqual(c.exponentiation(2, 3), 8)

    def test_exponentiation2(self):
        c = Calculator()
        self.assertEqual(c.exponentiation(5, 4), 625)

    def test_exponentiation3(self):
        c = Calculator()
        self.assertEqual(c.exponentiation(-6, 3), -216)

    def test_inverse1(self):
        c = Calculator()
        self.assertEqual(c.inverse(4), 0.2500)

    def test_inverse2(self):
        c = Calculator()
        self.assertEqual(c.inverse(25), 0.0400)

    def test_inverse3(self):
        c = Calculator()
        self.assertEqual(c.inverse(-0.5), -2.0000)

    def test_invert_sign1(self):
        c = Calculator()
        self.assertEqual(c.invert_sign(5), -5)

    def test_invert_sign2(self):
        c = Calculator()
        self.assertEqual(c.invert_sign(-40), 40)

    def test_invert_sign3(self):
        c = Calculator()
        self.assertEqual(c.invert_sign(1500), -1500)

    def test_display_error(self):
        c = Calculator()
        self.assertEqual(c.display_error(), 'Error!')

    def test_sine_radian1(self):
        c = Calculator()
        self.assertEqual(c.sine(90), 0.8940)

    def test_sine_radian2(self):
        c = Calculator()
        self.assertEqual(c.sine(180), -0.8012)

    def test_sine_radian3(self):
        c = Calculator()
        self.assertEqual(c.sine(360), 0.9589)

    def test_sine_degrees1(self):
        c = Calculator()
        self.assertEqual(c.sine(90), 1)

    def test_sine_degrees2(self):
        c = Calculator()
        self.assertEqual(c.sine(180), 0)

    def test_sine_degrees3(self):
        c = Calculator()
        self.assertEqual(c.sine(360), 0)

    def test_cosine_radians1(self):
        c = Calculator()
        self.assertEqual(c.cosine(90), -0.4481)

    def test_cosine_radians2(self):
        c = Calculator()
        self.assertEqual(c.cosine(180), -0.5985)

    def test_cosine_radians3(self):
        c = Calculator()
        self.assertEqual(c.cosine(360), -0.2837)

    def test_cosine_degrees1(self):
        c = Calculator()
        self.assertEqual(c.cosine(90), 0)

    def test_cosine_degrees2(self):
        c = Calculator()
        self.assertEqual(c.cosine(180), -1)

    def test_cosine_degrees3(self):
        c = Calculator()
        self.assertEqual(c.cosine(360), 1)

    def test_tangent_radians1(self):
        c = Calculator()
        self.assertEqual(c.tangent(90), -1.9952)

    def test_tangent_radians2(self):
        c = Calculator()
        self.assertEqual(c.tangent(180), 1.3387)

    def test_tangent_radians3(self):
        c = Calculator()
        self.assertEqual(c.tangent(360), -3.3801)

    def test_tangent_degrees1(self):
        c = Calculator()
        self.assertEqual(c.tangent(90), 'Error')

    def test_tangent_degrees2(self):
        c = Calculator()
        self.assertEqual(c.tangent(180), 0)

    def test_tangent_degrees3(self):
        c = Calculator()
        self.assertEqual(c.tangent(360), 0)

    def test_inverse_sine(self):
        pass


    # print("test")
    # print("2")



if __name__ == '__main__':
    unittest.main()
