import pymorphy2


# Check of pretext, conjunction, particle
def pretext_check(word):
    morph = pymorphy2.MorphAnalyzer()
    parsed = morph.parse(word)
    if len(parsed) == 0:
        return False
    if parsed[0].tag.POS in ['PREP', 'CONJ', 'PRCL']:
        return True
    return False
