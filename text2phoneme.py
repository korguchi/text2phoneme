"""日本語文を音素列へ変換。
Ginza や JUMAN++ V2 で文節単位でスペースを空け、pyopenjtalk へ入力。
あらかじめ文節単位で分けておくことで形態素の推定誤りを低減する。

Requirements
-----
- PyKNP
- Ginza
- Juman++ V2
- pyopenjtalk (https://github.com/korguchi/pyopenjtalk)
"""


from pyknp import Juman
import spacy
import pyopenjtalk


def insert_spaces_ginza(text):
    nlp = spacy.load("ja_ginza_electra")
    doc = nlp(text)

    output = []
    prev_noun = False
    prev_chunk = ""
    punctuations = ["、", "。", "！", "？", "；", "：", "・"]

    for token in doc:
        morpheme = token.text
        pos = token.pos_

        if pos == "NOUN":
            if prev_noun and morpheme not in punctuations:
                output.append(" ")
            output.append(morpheme)
            prev_noun = True
        else:
            if prev_chunk != "" and morpheme not in punctuations:
                output.append(" ")
                prev_chunk = ""
            output.append(morpheme)
            prev_noun = False

        if pos == "ADP" or pos == "AUX":
            prev_chunk = morpheme

    return "".join(output)


def insert_spaces_juman(text):
    juman = Juman("jumanpp", multithreading=True)
    result = juman.analysis(text)
    
    output = []
    prev_noun = False
    prev_chunk = ""
    punctuations = ["、", "。", "！", "？", "；", "：", "・"]

    for mrph in result.mrph_list():
        morpheme = mrph.midasi
        pos = mrph.hinsi

        if pos == "名詞":
            if prev_noun and morpheme not in punctuations:
                output.append(" ")
            output.append(morpheme)
            prev_noun = True
        else:
            if prev_chunk != "" and morpheme not in punctuations:
                output.append(" ")
                prev_chunk = ""
            output.append(morpheme)
            prev_noun = False

        if pos == "助詞" or pos == "助動詞":
            prev_chunk = morpheme

    return "".join(output)


def insert_spaces(text, analyzer='ginza'):
    if analyzer == 'ginza':
        return insert_spaces_ginza(text)
    else:
        return insert_spaces_juman

def text2phoneme(text):
    divided_text = insert_spaces(text)
    phonemes = pyopenjtalk.g2p(divided_text)
    return phonemes

if __name__ == '__main__':
    text = "ゲグァンはこのところ他者を見下すし、ちょっと脅かすか？形態素解析"
    phonemes = text2phoneme(text)
    print('sil '+phonemes+' sil')
