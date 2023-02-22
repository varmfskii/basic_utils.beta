class Dialect:
    keywords = []
    specials = {
        'DATA': ['DATA'],
        'ELSE': ['ELSE'],
        'FOR': ['FOR'],
        'GO': ['GO'],
        'GOSUB': ['GOSUB'],
        'GOTO': ['GOTO'],
        'IF': ['IF'],
        'LET': ['LET'],
        'NEXT': ['NEXT'],
        'REM': ['REM', "'"],
        'SUB': ['SUB'],
        'THEN': ['THEN'],
        'TO': ['TO']
    }
    kw2code = {}
    code2kw = {}
    kw_keys = []

    def __init__(self):
        for k, c in self.keywords:
            self.kw2code[k] = c
            self.code2kw[c] = k
            self.kw_keys.append(k)
        self.kw_keys.sort(key=(lambda x: -len(x)))
