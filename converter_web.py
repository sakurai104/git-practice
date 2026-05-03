import streamlit as st

# Pa（パスカル）を基準とした変換係数
UNITS = {
    "Pa":      1.0,
    "kPa":     1e3,
    "MPa":     1e6,
    "GPa":     1e9,
    "kgf/cm2": 98066.5,
    "N/mm2":   1e6,
    "atm":     101325.0,
    "psi":     6894.757,
}

st.title("圧力・応力 単位変換ツール")

value = st.number_input("変換したい数値を入力", value=1.0)
from_unit = st.selectbox("変換元の単位", list(UNITS.keys()))
to_unit = st.selectbox("変換先の単位", list(UNITS.keys()))

result = value * UNITS[from_unit] / UNITS[to_unit]

st.success(f"{value} {from_unit} = {result:.6g} {to_unit}")

# 全単位への一覧表示
st.subheader("全単位への変換一覧")
for unit, factor in UNITS.items():
    converted = value * UNITS[from_unit] / factor
    st.write(f"{unit}：{converted:.6g}")