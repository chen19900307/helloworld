# -*- coding: utf-8 -*
# bold装饰器
def makebold(fn):
    def wrapper():
        # 在前后加入标签
        return "<b>" + fn() + "</b>"
    return wrapper

# italic装饰器
def makeitalic(fn):
    def wrapper():
        # 加入标签
        return "<i>" + fn() + "</i>"
    return wrapper

@makebold
@makeitalic
def say():
    return "hello"

print say()
#outputs: <b><i>hello</i></b>

# 等价的代码
def say():
    return "hello"
say = makebold(makeitalic(say))

print say()
#outputs: <b><i>hello</i></
