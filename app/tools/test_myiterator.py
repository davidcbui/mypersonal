import pytest

from .myiterator import yrange

# from passlib.context import CryptContext
from .mypasslib import Mypasslib


def test_iteraror():
    n_list = iter([1, 100])
    print("im testing")
    next(n_list)
    assert True


def test_yrange():
    yr = yrange(100)
    yr.next()
    print(yr.next())


def test_xrange():
    xr = yrange.xrange(10)
    print("test xrange")
    print(xr)


def test_gennum():
    gen_nums = yrange.gen_num(100)
    print("testing number generator")
    print(type(gen_nums))
    for num in gen_nums:
        print(num)
    print("or it can use next function")
    more_nums = yrange.gen_num(10)
    print(next(more_nums))
    print(next(more_nums))
    print(next(more_nums))

    assert True


def test_repeat():
    # unpacking argument
    args = [4, "john"]
    rp = yrange.repeat(*args)  # for list then using *args
    kargs = {"count": 4, "name": "john"}  # for dict then using **kargs
    rp2 = yrange.repeat(**kargs)


def test_encrypt_pass():
    print("test encrypt pass ")
    mypasslb = Mypasslib()
    passwrd = "tuimora"
    hashed_pass = mypasslb.encrypt_password(passwrd)

    print("encryped pass {}".format(hashed_pass))

    verifypass = mypasslb.check_encrypted_password(passwrd, hashed_pass)
    # print("now back to pass {}".format(verifypass))
    print(f"ok back to pass {verifypass}")
    assert True

