from spellchecker import SpellChecker


if __name__ == '__main__':
    spell = SpellChecker()
    samples = spell.unknown([
        'correct',
        'corect',
        'loooove',
        'foootballl',
        'circit',
        'translat',
        'guydance',
    ])

    for sample in samples:
        correct_form = spell.correction(sample)
        print(f"{sample} ------> {correct_form}")
