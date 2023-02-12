# http://www.zimmers.net/anonftp/pub/cbm/programming/cbm-basic-tokens.txt
from commodore import c4_0

keywords = c4_0.keywords + [
    ("COLOR", 0xDB),
    ("COLD", 0xDC),
    ("KEY", 0xDD),
    ("DVERIFY", 0xDE),
    ("DELETE", 0xDF),
    ("AUTO", 0xE0),
    ("MERGE", 0xE1),
    ("OLD", 0xE2),
    ("MONITOR", 0xE3)
]

