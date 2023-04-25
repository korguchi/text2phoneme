# text2phoneme
日本語文を音素列へ変換するスクリプト
形態素解析器を使って文節単位でスペースを空けて pyopenjtalk へ入力。
あらかじめ文節単位で分けておくことで形態素の推定誤りを低減する。

Requirements
- PyKNP
- GiNZA
- Juman++ V2
- pyopenjtalk (https://github.com/korguchi/pyopenjtalk)
