import unittest#导入unittest标准库

from Fibonacci import main,Fibonacci_#从Fibonacci文件中导入写好的函数main(),Fibonacci_()

class TestFibonacci(unittest.TestCase):#创建名为TestFibonacci的类，（unittest.TestCase）表示继承自unittest(标注库中的一个module)TestCase（子模块）——实现assert语句
    def test_n_23(self):#编写测试用例——检验23时是否返回28657
        self.assertEqual(Fibonacci_(23),28657)
    def test_negative_n(self):#检验负数时是否返回False
        self.assertFalse(Fibonacci_(-6))
    def test_invalid_input_type(self):#数据类型错误时（通过int('invalid')）捕捉ValueError
        with self.assertRaises(ValueError):
            int('invalid')
if __name__=='__main__':
    unittest.main()
