
import unittest


# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1


def check_name(dev_name):
    if dev_name:
        if dev_name.isupper():
            return True
        else:
            return False
    else:
        return False


def eualcheck(var1, var2):
    if var1 == var2:
        return True
    else:
        return False


# Here's our "unit tests".
class GeneralUnitTest(unittest.TestCase):

    def testone(self):
        self.failUnless(IsOdd(1))

    def testtwo(self):
        self.failIf(IsOdd(2))

    def test3(self):
        self.failIf(IsOdd(6))

    def test4(self):
        self.assertFalse(check_name("huseni"))

    def test5(self):
        self.assertFalse(check_name("14"))

    def test6(self):
        self.assertFalse(check_name("&^%#^"))

    def test7(self):
        self.assertFalse(check_name("Tasneem"))

    def test8(self):
        self.assertEqual(4, 4, "They are equal")

    def test9(self):
        self.assertNotEqual(4, 5, "They are not equal")

    def test10(self):
        #self.assertRaises(exception, func, para, meters, ...)
        pass

    def test_split_true(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_split_false(self):
        s = 'hello world'
        self.assertNotEqual(s.split(), ['hello', 'worl'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


def main():
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(GeneralUnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()