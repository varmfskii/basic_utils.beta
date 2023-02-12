# http://www.zimmers.net/anonftp/pub/cbm/programming/cbm-basic-tokens.txt
from commodore import c2_0

keywords = c2_0.keywords + [
    ("KEY", 0xCC),
    ("GRAPHIC", 0xCD),
    ("SCNCLR", 0xCE),
    ("CIRCLE", 0xCF),
    ("DRAW", 0xD0),
    ("REGION", 0xD1),
    ("COLOR", 0xD2),
    ("POINT", 0xD3),
    ("SOUND", 0xD4),
    ("CHAR", 0xD5),
    ("PAINT", 0xD6),
    ("RPOT", 0xD7),
    ("RPEN", 0xD8),
    ("RSND", 0xD9),
    ("RCOLR", 0xDA),
    ("RGR", 0xDB),
    ("RJOY", 0xDC),
    ("RDOT", 0xDD)
]
