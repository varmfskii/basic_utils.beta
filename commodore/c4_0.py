# http://www.zimmers.net/anonftp/pub/cbm/programming/cbm-basic-tokens.txt
from commodore import c2_0

keywords = c2_0.keywords + [
    ("CONCAT", 0xCC),
    ("DOPEN", 0xCD),
    ("DCLOSE", 0xCE),
    ("RECORD", 0xCF),
    ("HEADER", 0xD0),
    ("COLLECT", 0xD1),
    ("BACKUP", 0xD2),
    ("COPY", 0xD3),
    ("APPEND", 0xD4),
    ("DSAVE", 0xD5),
    ("DLOAD", 0xD6),
    ("CATALOG", 0xD7),
    ("RENAME", 0xD8),
    ("SCRATCH", 0xD9),
    ("DIRECTORY", 0xDA)
]
