def main():
    """ メイン関数
    """

    # ユーザ入力受付
    value1: int = get_value(1)
    value2: int = get_value(2)

    # 計算結果表示
    calculation(value1, value2)

    # 文字列操作デモンストレーション
    first_name: str = "Yuri"
    last_name: str = "Katano"
    demonstrateStringManipulation(first_name, last_name)

def get_value(num: int) -> int:
    """ ユーザ入力受付

    Args:
        num (int): 何番目の入力か

    Returns:
        int: 入力された値(整数)
    """

    value: int = 0

    while True:
        user_input = input(f"{num}番目の値(整数)を入力してください: ")

        try:
            value = int(user_input)
            break
        except:
            print(f"無効な入力です。整数を入力してください。")
  
    return value

def calculation(value1: int, value2: int):
    """ 計算結果表示

    Args:
        value1 (int): 1番目の値
        value2 (int): 2番目の値
    """
    print(f"-----計算結果表示-----")
    # 足し算
    addition: int = int(value1) + int(value2)
    print(f"Addition:{addition}")

    # 引き算
    subtraction: int = int(value1) - int(value2)
    print(f"Subtraction:{subtraction}")

    # 掛け算
    multiplication: int = int(value1) * int(value2)
    print(f"Multiplication:{multiplication}")

    # 割り算
    integerDivision: int = int(value1) / int(value2)
    print(f"Integer Division:{int(integerDivision)}")

    # 浮動⼩数点除算
    floatDivision: int = int(value1) / int(value2)
    print(f"Float Division:{floatDivision}")

    # 余り
    modulo: int = int(value1) % int(value2)
    print(f"Modulo:{modulo}")
    print(f"----------------------")

def demonstrateStringManipulation(first_name: str, last_name: str):
    """ 文字列操作デモンストレーション

    Args:
        first_name (str): 名
        last_name (str): 姓
    """
    print(f"-----文字列操作結果表示-----")
    full_name: str = first_name + last_name
    print("Full name:" f"{full_name}")
    print("Full name length:" f"{len(full_name)}")
    print("Full name upper:" f"{full_name.upper()}")
    print("Full name lower:" f"{full_name.lower()}")
    print(f"----------------------------")

if __name__ == "__main__":
    main()
