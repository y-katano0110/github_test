import pytest
import test1
import test2

def test_conversionString():
    """ conversionString()のテスト
    """

    str = test1.conversionString("test", 99, True)
    assert str == "name:test age:99 is_student:1"

def test_calculation(capfd):
    """ calculation()のテスト

    Args:
        capfd (_type_): capfd
    """

    test2.calculation(4, 2)

    out, err = capfd.readouterr()
    assert out == "-----計算結果表示-----\n" \
        + "Addition:6\n" \
        + "Subtraction:2\n" \
        + "Multiplication:8\n" \
        + "Integer Division:2\n" \
        + "Float Division:2.0\n" \
        + "Modulo:0\n" \
        + "----------------------\n"
    assert err is ''

def test_demonstrateStringManipulation(capfd):
    """ demonstrateStringManipulation()のテスト

    Args:
        capfd (_type_): capfd
    """

    test2.demonstrateStringManipulation("Test", "Taro")

    out, err = capfd.readouterr()
    assert out == "-----文字列操作結果表示-----\n" \
        + "Full name:TestTaro\n" \
        + "Full name length:8\n" \
        + "Full name upper:TESTTARO\n" \
        + "Full name lower:testtaro\n" \
        + "----------------------------\n"
    assert err is ''
