# text2phoneme
日本語テキストを音素列へ変換するスクリプト

形態素解析器を使って文節単位でスペースを空けて pyopenjtalk へ入力。

あらかじめ文節単位で分けておくことで形態素の推定誤りを低減する。

## 必要パッケージ
- PyKNP
- GiNZA
- Juman++ V2
- pyopenjtalk (https://github.com/korguchi/pyopenjtalk)

## 環境構築
### pyopenjtalk のインストール
```
>>> git clone https://github.com/korguchi/pyopenjtalk
>>> cd pyopenjtalk
>>> pip install -e .
```

### GiNZA のインストール
```
>>> pip install -U ginza https://github.com/megagonlabs/ginza/releases/download/latest/ja_ginza_electra-latest-with-model.tar.gz
>>> pip install -U "spacy[cuda<version>]"
```

### JUMAN++ V2, PyKNP のインストール
```
>>> wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc3/jumanpp-2.0.0-rc3.tar.xz
>>> tar xvf jumanpp-2.0.0-rc3.tar.xz
>>> cd jumanpp-2.0.0-rc3 && mkdir bld
>>> cd jumanpp-2.0.0-rc3/bld && cmake ..  -DCMAKE_INSTALL_PREFIX=/usr/local
>>> cd jumanpp-2.0.0-rc3/bld && make install -j 4
>>> pip install pyknp
```
