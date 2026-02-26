# calculator.py
def get_divisor():
    # 问题1：返回0，会导致下面的divide函数除零（跨函数依赖问题）
    return 0  

def divide(a, b=None):
    # 问题2：b为None时，调用get_divisor()获取值，但未做防护
    if b is None:
        b = get_divisor()
    return a / b

# 测试调用
result = divide(10)
print(result)
