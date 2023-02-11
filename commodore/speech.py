# http://www.zimmers.net/anonftp/pub/cbm/programming/cbm-basic-tokens.txt
from commodore import c2_0

keywords = c2_0.keywords + [
    ("reset", 0xcc),
    ("basic", 0xcd),
    ("help", 0xce),
    ("key", 0xcf),
    ("himem", 0xd0),
    ("disk", 0xd1),
    ("dir", 0xd2),
    ("bload", 0xd3),
    ("bsave", 0xd4),
    ("map", 0xd5),
    ("mem", 0xd6),
    ("pause", 0xd7),
    ("block", 0xd8),
    ("hear", 0xd9),
    ("record", 0xda),
    ("play", 0xdb),
    ("voldef", 0xdc),
    ("coldef", 0xdd),
    ("hex", 0xde),
    ("dez", 0xdf),
    ("screen", 0xe0),
    ("exec", 0xe1),
    ("mon", 0xe2),
    ("<-", 0xe3),
    ("from", 0xe4),
    ("speed", 0xe5),
    ("off", 0xe6)
]
