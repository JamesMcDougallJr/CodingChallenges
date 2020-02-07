# Implement your function below.
def is_one_away(s1, s2):
    return num_sub(s1, s2) < 2 

def num_sub(s1, s2):
    if len(s1) < 1 and len(s2) < 1:
        return 0
    elif len(s1) < 1:
        return len(s2)
    elif len(s2) < 1:
        return len(s1)

    # if the first chars equal, slice them out
    if s1[0] == s2[0]:
        return num_sub(s1[1:], s2[1:])
    elif len(s1) == len(s2):
        return 1 + num_sub(s1[1:], s2[1:])
    elif len(s1) < len(s2):
        return 1 + num_sub(s1, s2[1:])
    else:
        return 1 + num_sub(s1[1:], s2)

if __name__ == '__main__':
    assert True == is_one_away("abcde", "abcd")  # should return True
    assert True == is_one_away("abde", "abcde")  # should return True
    assert True == is_one_away("a", "a")  # should return True
    assert True == is_one_away("abcdef", "abqdef")  # should return True
    assert True == is_one_away("abcdef", "abccef")  # should return True
    assert True == is_one_away("abcdef", "abcde")  # should return True
    assert False == is_one_away("aaa", "abc")  # should return False
    assert False == is_one_away("abcde", "abc")  # should return False
    assert False == is_one_away("abc", "abcde")  # should return False
    assert False == is_one_away("abc", "bcc")  # should return False

