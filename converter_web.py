import streamlit as st

# Pa（パスカル）を基準とした変換係数
UNITS = {
    "MPa":      1e6,
    "tonf/m2":  9806.65,
    "kgf/cm2":  98066.5,
    "N/mm2":    1e6,
    "kN/cm2":   1e7,
    "kN/m2":    1e3,
    "m(水頭)":  9806.65,
    "Pa":       1.0,
    "kPa":      1e3,
    "GPa":      1e9,
    "atm":      101325.0,
    "psi":      6894.757,
}

# 番号付きリストを作成
UNIT_LIST = list(UNITS.keys())
UNIT_OPTIONS = [f"{i+1}. {unit}" for i, unit in enumerate(UNIT_LIST)]

st.title("圧力・応力 単位変換ツール")
st.caption("ダム・土木分野対応版")

# 単位一覧を表示
st.subheader("単位一覧")
for i, unit in enumerate(UNIT_LIST):
    st.write(f"{i+1}. {unit}")

st.divider()

# 数値入力
value = st.number_input("変換したい数値を入力", value=1.0)

# 変換元の単位選択
from_num = st.number_input(
    "変換元の単位番号を入力",
    min_value=1,
    max_value=len(UNIT_LIST),
    value=1,
    step=1
)
from_unit = UNIT_LIST[from_num - 1]
st.info(f"変換元：{from_num}. {from_unit}")

# 変換先の単位選択
to_num = st.number_input(
    "変換先の単位番号を入力",
    min_value=1,
    max_value=len(UNIT_LIST),
    value=2,
    step=1
)
to_unit = UNIT_LIST[to_num - 1]
st.info(f"変換先：{to_num}. {to_unit}")

st.divider()

# 変換結果
result = value * UNITS[from_unit] / UNITS[to_unit]
st.success(f"**結果：{value} {from_unit} = {result:.6g} {to_unit}**")

# 全単位への変換一覧
st.subheader("全単位への変換一覧")
for i, (unit, factor) in enumerate(UNITS.items()):
    converted = value * UNITS[from_unit] / factor
    st.write(f"{i+1}. {unit}：{converted:.6g}")