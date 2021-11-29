def test_pythagore(a,b,c):
    if a*a + b*b == c*c or a*a + c*c == b*b or b**2 + c**2 == a**2:
        return True
    return False


print(test_pythagore(3, 4, 5))
print(test_pythagore(7, 2, 12))
print(test_pythagore(3, 5, 4))
print(test_pythagore(5, 4, 3))