 # -*- coding: utf-8 -*
# 装饰器是一个以另一个函数为参数的函数
def my_shiny_new_decorator(a_function_to_decorate):

    # 在这里，装饰器定义一个函数： 包装器.
    # 这个函数将原始函数进行包装，以达到在原始函数之前、之后执行代码的目的
    def the_wrapper_around_the_original_function():

        # 将你要在原始函数之前执行的代码放到这里
        print "Before the function runs"

        # 调用原始函数(需要带括号)
        a_function_to_decorate()

        # 将你要在原始函数之后执行的代码放到这里
        print "After the function runs"

    # 代码到这里，函数‘a_function_to_decorate’还没有被执行
    # 我们将返回刚才创建的这个包装函数
    # 这个函数包含原始函数及要执行的附加代码，并且可以被使用
    return the_wrapper_around_the_original_function


def a_stand_alone_function():
    print "I am a stand alone function,don~t you dare modify me"

@my_shiny_new_decorator
def another_stand_alone_function():
    print "Leave me alone"

if"__name__ == main":
    a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)


    
    another_stand_alone_function()
