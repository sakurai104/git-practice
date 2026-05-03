# 圧力・応力 単位変換プログラム

# Pa（パスカル）を基準とした変換係数
UNITS = {
    "Pa":       1.0,
    "kPa":      1e3,
    "MPa":      1e6,
    "GPa":      1e9,
    "kgf/cm2":  98066.5,
    "N/mm2":    1e6,
    "atm":      101325.0,
    "psi":      6894.757,
}

def convert(value, from_unit, to_unit):
    """from_unit → Pa → to_unit に変換する"""
    value_in_pa = value * UNITS[from_unit]
    return value_in_pa / UNITS[to_unit]

def show_units():
    print("\n使用可能な単位：")
    for i, unit in enumerate(UNITS.keys(), 1):
        print(f"  {i}. {unit}")

def main():
    print("=== 圧力・応力 単位変換プログラム ===")
    while True:
        show_units()
        print("\n'q' を入力すると終了します")

        # 入力値
        value_str = input("\n変換したい数値を入力: ")
        if value_str.lower() == "q":
            print("終了します。")
            break

        try:
            value = float(value_str)
        except ValueError:
            print("数値を入力してください。")
            continue

        from_unit = input("変換元の単位を入力: ")
        if from_unit not in UNITS:
            print("対応していない単位です。")
            continue

        to_unit = input("変換先の単位を入力: ")
        if to_unit not in UNITS:
            print("対応していない単位です。")
            continue

        result = convert(value, from_unit, to_unit)
        print(f"\n結果: {value} {from_unit} = {result:.6g} {to_unit}")

if __name__ == "__main__":
    main()