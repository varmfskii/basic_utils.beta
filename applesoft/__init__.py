from msbasic.dialect import Dialect


class Applesoft(Dialect):
    keywords = [
        ("&", 0xAF), ("*", 0xCA), ("+", 0xC8), ("-", 0xC9), ("/", 0xCB),
        (";", 0xCC), ("<", 0xD1), ("=", 0xD0), (">", 0xCF), ("ABS", 0xD4),
        ("AND", 0xCD), ("ASC", 0xE6), ("AT", 0xC5), ("ATN", 0xE1),
        ("CALL", 0x8C), ("CHR$", 0xE7), ("CLEAR", 0xBD), ("COLOR=", 0xA0),
        ("CONT", 0xBB), ("COS", 0xDE), ("DATA", 0x83), ("DEF FN", 0xB8),
        ("DEL", 0x85), ("DIM", 0x86), ("DRAW", 0x94), ("END", 0x80),
        ("EXP", 0xDD), ("FLASH", 0x9F), ("FN", 0xC2), ("FOR", 0x81),
        ("FRE", 0xD6), ("GET", 0xBE), ("GOSUB", 0xB0), ("GOTO", 0xAB),
        ("GR", 0x88), ("HCOLOR=", 0x92), ("HGR", 0x91), ("HGR2", 0x90),
        ("HIMEM:", 0xA3), ("HLIN", 0x8E), ("HOME", 0x97), ("HPLOT", 0x93),
        ("HTAB", 0x96), ("IF", 0xAD), ("IN #", 0x8B), ("INPUT", 0x84),
        ("INT", 0xD3), ("INVERSE", 0x9E), ("LEFT$", 0xE8), ("LEN", 0xE3),
        ("LET", 0xAA), ("LIST", 0xBC), ("LOAD", 0xB6), ("LOG", 0xDC),
        ("LOMEM:", 0xA4), ("MID$", 0xEA), ("NEW", 0xBF), ("NEXT", 0x82),
        ("NORMAL", 0x9D), ("NOT", 0xC6), ("NOTRACE", 0x9C), ("ON", 0xB4),
        ("ONERR", 0xA5), ("OR", 0xCE), ("PDL", 0xD8), ("PEEK", 0xE2),
        ("PLOT", 0x8D), ("POKE", 0xB9), ("POP", 0xA1), ("POS", 0xD9),
        ("PR #", 0x8A), ("PRINT", 0xBA), ("READ", 0x87), ("RECALL", 0xA7),
        ("REM", 0xB2), ("RESTORE", 0xAE), ("RESUME", 0xA6), ("RETURN", 0xB1),
        ("RIGHT$", 0xE9), ("RND", 0xDB), ("ROT=", 0x98), ("RUN", 0xAC),
        ("SAVE", 0xB7), ("SCALE=", 0x99), ("SCRN (", 0xD7), ("SGN", 0xD2),
        ("SHLOAD", 0x9A), ("SIN", 0xDF), ("SPC(", 0xC3), ("SPEED=", 0xA9),
        ("SQR", 0xDA), ("STEP", 0xC7), ("STOP", 0xB3), ("STORE", 0xA8),
        ("STR$", 0xE4), ("TAB", 0xC0), ("TAN", 0xE0), ("TEXT", 0x89),
        ("THEN", 0xC4), ("TO", 0xC1), ("TRACE", 0x9B), ("USR", 0xD5),
        ("VAL", 0xE5), ("VLIN", 0x8F), ("VTAB", 0xA2), ("WAIT", 0xB5),
        ("XDRAW", 0x95)
    ]
    specials = {
        'DATA': ['DATA'], 'ELSE': [], 'FOR': ['FOR'], 'GO': [],
        'GOSUB': ['GOSUB'], 'GOTO': ['GOTO'], 'IF': ['IF'], 'NEXT': ['NEXT'],
        'REM': ['REM'], 'SUB': [], 'THEN': ['THEN'], 'TO': []
    }
    address = 0x0801


if __name__ == "__main__":
    import sys

    sys.stderr.write("This is a library")
