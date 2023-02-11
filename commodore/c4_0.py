# http://www.zimmers.net/anonftp/pub/cbm/programming/cbm-basic-tokens.txt
from commodore import c2_0

keywords = c2_0.keywords + [
    ("concat", 0xcc),
    ("dopen", 0xcd),
    ("dclose", 0xce),
    ("record", 0xcf),
    ("header", 0xd0),
    ("collect", 0xd1),
    ("backup", 0xd2),
    ("copy", 0xd3),
    ("append", 0xd4),
    ("dsave", 0xd5),
    ("dload", 0xd6),
    ("catalog", 0xd7),
    ("rename", 0xd8),
    ("scratch", 0xd9),
    ("directory", 0xda)
]
