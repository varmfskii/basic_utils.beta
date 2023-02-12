# http://www.zimmers.net/anonftp/pub/cbm/programming/cbm-basic-tokens.txt
from commodore import c2_0

keywords = c2_0.keywords + [
    ("RESET", 0xCC),
    ("BASIC", 0xCD),
    ("HELP", 0xCE),
    ("KEY", 0xCF),
    ("HIMEM", 0xD0),
    ("DISK", 0xD1),
    ("DIR", 0xD2),
    ("BLOAD", 0xD3),
    ("BSAVE", 0xD4),
    ("MAP", 0xD5),
    ("MEM", 0xD6),
    ("PAUSE", 0xD7),
    ("BLOCK", 0xD8),
    ("HEAR", 0xD9),
    ("RECORD", 0xDA),
    ("PLAY", 0xDB),
    ("VOLDEF", 0xDC),
    ("COLDEF", 0xDD),
    ("HEX", 0xDE),
    ("DEZ", 0xDF),
    ("SCREEN", 0xE0),
    ("EXEC", 0xE1),
    ("MON", 0xE2),
    ("<-", 0xE3),
    ("FROM", 0xE4),
    ("SPEED", 0xE5),
    ("OFF", 0xE6)
]
