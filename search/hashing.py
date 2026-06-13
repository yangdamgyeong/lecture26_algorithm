#BOJ15829
#영문소문자를 입력받아서 
#자릿수마다 31의 거듭제곱을 곱해 더한 뒤
#1234567891로 나눈 나머지(해시값)를 출력하는 프로그램 작성
def hash_function(alpha):
    alphabet = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
        'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    r = 31
    M = 1234567891

    result = 0
    for i in range(len(alpha)):
        val = alphabet[alpha[i]]
        result += val * (r ** i)
    return result % M

alpha = input("문자열: ")
print(hash_function(alpha))
