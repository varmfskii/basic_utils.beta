# http://www.zimmers.net/anonftp/pub/cbm/programming/cbm-basic-tokens.txt
from commodore import c4_0

keywords = c4_0.keywords + [
    ("color", 0xdb),
    ("cold", 0xdc),
    ("key", 0xdd),
    ("dverify", 0xde),
    ("delete", 0xdf),
    ("auto", 0xe0),
    ("merge", 0xe1),
    ("old", 0xe2),
    ("monitor", 0xe3)
]

