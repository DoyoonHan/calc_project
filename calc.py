#더하기 함수 주석 추가
def sum(a, b):
    return a + b

# 빼기 함수 주석 추가
def sub(a, b):
    return a - b

# 곱하기 함수 주석 추가
def mul(a, b):
    return a * b

def div(a, b):
    if b == 0: #added this
        return 0
    else:
        return a / b

def mod(a, b):
    return a % b