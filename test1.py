def main():
    """ メイン関数
    """

    # 変数宣言
    name: str = "katano"
    age: int = 34
    is_student: bool = True

    # データ表示
    print(conversionString(name, age, is_student))

def conversionString(name: str, age: int, is_student: bool) -> str:
    """ 文字列変換関数

    Args:
        name (str): 名前
        age (int): 年齢
        is_student (bool): 生徒フラグ

    Returns:
        str: 変換後文字列
    """

    # 型変換
    s_age = str(age)
    i_is_student = int(is_student)

    return f"name:{name} age:{s_age} is_student:{i_is_student}"

if __name__ == "__main__":
    main()
