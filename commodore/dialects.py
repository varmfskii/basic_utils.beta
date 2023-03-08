from msbasic.dialects import Dialect

SPECIALS1 = {
    'DATA': ['DATA'],
    'ELSE': ['ELSE'],
    'FOR': ['FOR'],
    'GO': [],
    'GOSUB': ['GOSUB'],
    'GOTO': ['GOTO'],
    'IF': ['IF'],
    'NEXT': ['NEXT'],
    'REM': ['REM', "'"],
    'SUB': [],
    'THEN': ['THEN'],
    'TO': []
}

SPECIALS2 = {
    'DATA': ['DATA'],
    'ELSE': ['ELSE'],
    'FOR': ['FOR'],
    'GO': ['GO'],
    'GOSUB': ['GOSUB'],
    'GOTO': ['GOTO'],
    'IF': ['IF'],
    'NEXT': ['NEXT'],
    'REM': ['REM', "'"],
    'SUB': [],
    'THEN': ['THEN'],
    'TO': ['TO']
}

# http://www.zimmers.net/anonftp/pub/cbm/programming/cbm-basic-tokens.txt
c1_0_keywords = [
    ("END", 0x80),
    ("FOR", 0x81),
    ("NEXT", 0x82),
    ("DATA", 0x83),
    ("INPUT#", 0x84),
    ("INPUT", 0x85),
    ("DIM", 0x86),
    ("READ", 0x87),
    ("LET", 0x88),
    ("GOTO", 0x89),
    ("RUN", 0x8A),
    ("IF", 0x8B),
    ("RESTORE", 0x8C),
    ("GOSUB", 0x8D),
    ("RETURN", 0x8E),
    ("REM", 0x8F),
    ("STOP", 0x90),
    ("ON", 0x91),
    ("WAIT", 0x92),
    ("LOAD", 0x93),
    ("SAVE", 0x94),
    ("VERIFY", 0x95),
    ("DEF", 0x96),
    ("POKE", 0x97),
    ("PRINT#", 0x98),
    ("PRINT", 0x99),
    ("CONT", 0x9A),
    ("LIST", 0x9B),
    ("CLR", 0x9C),
    ("CMD", 0x9D),
    ("SYS", 0x9E),
    ("OPEN", 0x9F),
    ("CLOSE", 0xA0),
    ("GET", 0xA1),
    ("NEW", 0xA2),
    ("TAB(", 0xA3),
    ("TO", 0xA4),
    ("FN", 0xA5),
    ("SPC(", 0xA6),
    ("THEN", 0xA7),
    ("NOT", 0xA8),
    ("STEP", 0xA9),
    ("+", 0xAA),
    ("-", 0xAB),
    ("*", 0xAC),
    ("/", 0xAD),
    ("^", 0xAE),
    ("AND", 0xAF),
    ("OR", 0xB0),
    (">", 0xB1),
    ("=", 0xB2),
    ("<", 0xB3),
    ("SGN", 0xB4),
    ("INT", 0xB5),
    ("ABS", 0xB6),
    ("USR", 0xB7),
    ("FRE", 0xB8),
    ("POS", 0xB9),
    ("SQR", 0xBA),
    ("RND", 0xBB),
    ("LOG", 0xBC),
    ("EXP", 0xBD),
    ("COS", 0xBE),
    ("SIN", 0xBF),
    ("TAN", 0xC0),
    ("ATN", 0xC1),
    ("PEEK", 0xC2),
    ("LEN", 0xC3),
    ("STR$", 0xC4),
    ("VAL", 0xC5),
    ("ASC", 0xC6),
    ("CHR$", 0xC7),
    ("LEFT$", 0xC8),
    ("RIGHT$", 0xC9),
    ("MID$", 0xCA)
]


class C1(Dialect):
    id = 'Commodore BASIC 1.0'
    keywords = c1_0_keywords
    specials = SPECIALS1


c2_0_keywords = [
    ("GO", 0xcb),
    ("PI", 0xff)
]


class C2(Dialect):
    id = 'Commodore BASIC 2.0'
    keywords = c1_0_keywords + c2_0_keywords
    specials = SPECIALS2


c3_5_keywords = [
    ("RGR", 0xCC),
    ("RCLR", 0xCD),
    ("RLUM", 0xCE),
    ("JOY", 0xCF),
    ("RDOT", 0xD0),
    ("DEC", 0xD1),
    ("HEX$", 0xD2),
    ("ERR$", 0xD3),
    ("INSTR", 0xD4),
    ("ELSE", 0xD5),
    ("RESUME", 0xD6),
    ("TRAP", 0xD7),
    ("TRON", 0xD8),
    ("TROFF", 0xD9),
    ("SOUND", 0xDA),
    ("VOL", 0xDB),
    ("AUTO", 0xDC),
    ("PUDEF", 0xDD),
    ("GRAPHIC", 0xDE),
    ("PAINT", 0xDF),
    ("CHAR", 0xE0),
    ("BOX", 0xE1),
    ("CIRCLE", 0xE2),
    ("GSHAPE", 0xE3),
    ("SSHAPE", 0xE4),
    ("DRAW", 0xE5),
    ("LOCATE", 0xE6),
    ("COLOR", 0xE7),
    ("SCNCLR", 0xE8),
    ("SCALE", 0xE9),
    ("HELP", 0xEA),
    ("DO", 0xEB),
    ("LOOP", 0xEC),
    ("EXIT", 0xED),
    ("DIRECTORY", 0xEE),
    ("DSAVE", 0xEF),
    ("DLOAD", 0xF0),
    ("HEADER", 0xF1),
    ("SCRATCH", 0xF2),
    ("COLLECT", 0xF3),
    ("COPY", 0xF4),
    ("RENAME", 0xF5),
    ("BACKUP", 0xF6),
    ("DELETE", 0xF7),
    ("RENUMBER", 0xF8),
    ("KEY", 0xF9),
    ("MONITOR", 0xFA),
    ("USING", 0xFB),
    ("UNTIL", 0xFC),
    ("WHILE", 0xFD),
]


class C35(Dialect):
    id = 'Commodore BASIC 3.5'
    keywords = c1_0_keywords + c2_0_keywords + c3_5_keywords
    specials = SPECIALS2


c4_0_keywords = [
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


class C4(Dialect):
    id = 'Commodore BASIC 4.0'
    keywords = c1_0_keywords + c2_0_keywords + c4_0_keywords
    specials = SPECIALS2


c4_0x_keywords = [
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


class C4X(Dialect):
    id = 'Commodore BASIC 4.0 extended'
    keywords = c1_0_keywords + c2_0_keywords + c4_0_keywords + c4_0x_keywords
    specials = SPECIALS2


c7_0_keywords = [
    ("RGR", 0xCC),
    ("RCLR", 0xCD),
    ("JOY", 0xCF),
    ("RDOT", 0xD0),
    ("DEC", 0xD1),
    ("HEX$", 0xD2),
    ("ERR$", 0xD3),
    ("INSTR", 0xD4),
    ("ELSE", 0xD5),
    ("RESUME", 0xD6),
    ("TRAP", 0xD7),
    ("TRON", 0xD8),
    ("TROFF", 0xD9),
    ("SOUND", 0xDA),
    ("VOL", 0xDB),
    ("AUTO", 0xDC),
    ("PUDEF", 0xDD),
    ("GRAPHIC", 0xDE),
    ("PAINT", 0xDF),
    ("CHAR", 0xE0),
    ("BOX", 0xE1),
    ("CIRCLE", 0xE2),
    ("GSHAPE", 0xE3),
    ("SSHAPE", 0xE4),
    ("DRAW", 0xE5),
    ("LOCATE", 0xE6),
    ("COLOR", 0xE7),
    ("SCNCLR", 0xE8),
    ("SCALE", 0xE9),
    ("HELP", 0xEA),
    ("DO", 0xEB),
    ("LOOP", 0xEC),
    ("EXIT", 0xED),
    ("DIRECTORY", 0xEE),
    ("DSAVE", 0xEF),
    ("DLOAD", 0xF0),
    ("HEADER", 0xF1),
    ("SCRATCH", 0xF2),
    ("COLLECT", 0xF3),
    ("COPY", 0xF4),
    ("RENAME", 0xF5),
    ("BACKUP", 0xF6),
    ("DELETE", 0xF7),
    ("RENUMBER", 0xF8),
    ("KEY", 0xF9),
    ("MONITOR", 0xFA),
    ("USING", 0xFB),
    ("UNTIL", 0xFC),
    ("WHILE", 0xFD),
    ("POT", 0xCE02),
    ("BUMP", 0xCE03),
    ("PEN", 0xCE04),
    ("RSPPOS", 0xCE05),
    ("RSPRITE", 0xCE06),
    ("RSPCOLOR", 0xCE07),
    ("XOR", 0xCE08),
    ("RWINDOW", 0xCE09),
    ("POINTER", 0xCE0A),
    ("BANK", 0xFE02),
    ("FILTER", 0xFE03),
    ("PLAY", 0xFE04),
    ("TEMPO", 0xFE05),
    ("MOVSPR", 0xFE06),
    ("SPRITE", 0xFE07),
    ("SPRCOLOR", 0xFE08),
    ("RREG", 0xFE09),
    ("ENVELOPE", 0xFE0A),
    ("SLEEP", 0xFE0B),
    ("CATALOG", 0xFE0C),
    ("DOPEN", 0xFE0D),
    ("APPEND", 0xFE0E),
    ("DCLOSE", 0xFE0F),
    ("BSAVE", 0xFE10),
    ("BLOAD", 0xFE11),
    ("RECORD", 0xFE12),
    ("CONCAT", 0xFE13),
    ("DVERIFY", 0xFE14),
    ("DCLEAR", 0xFE15),
    ("SPRSAV", 0xFE16),
    ("COLLISION", 0xFE17),
    ("BEGIN", 0xFE18),
    ("BEND", 0xFE19),
    ("WINDOW", 0xFE1A),
    ("BOOT", 0xFE1B),
    ("WIDTH ", 0xFE1C),
    ("SPRDEF", 0xFE1D),
    ("QUIT", 0xFE1E),
    ("OFF", 0xFE24),
    ("FAST", 0xFE25),
    ("SLOW", 0xFE26),
    ("STASH", 0xFE1F),
    ("FETCH", 0xFE21),
    ("SWAP", 0xFE23)
]


class C7(Dialect):
    id = 'Commodore BASIC 7.0'
    keywords = c1_0_keywords + c2_0_keywords + c7_0_keywords
    specials = SPECIALS2


c10_0_keywords = [
    ("RGR", 0xCC),
    ("RCLR", 0xCD),
    ("JOY", 0xCF),
    ("RDOT", 0xD0),
    ("DEC", 0xD1),
    ("HEX$", 0xD2),
    ("ERR$", 0xD3),
    ("INSTR", 0xD4),
    ("ELSE", 0xD5),
    ("RESUME", 0xD6),
    ("TRAP", 0xD7),
    ("TRON", 0xD8),
    ("TROFF", 0xD9),
    ("SOUND", 0xDA),
    ("VOL", 0xDB),
    ("AUTO", 0xDC),
    ("PUDEF", 0xDD),
    ("GRAPHIC", 0xDE),
    ("PAINT", 0xDF),
    ("CHAR", 0xE0),
    ("BOX", 0xE1),
    ("CIRCLE", 0xE2),
    ("PASTE", 0xE3),
    ("CUT", 0xE4),
    ("LINE", 0xE5),
    ("LOCATE", 0xE6),
    ("COLOR", 0xE7),
    ("SCNCLR", 0xE8),
    ("SCALE", 0xE9),
    ("HELP", 0xEA),
    ("DO", 0xEB),
    ("LOOP", 0xEC),
    ("EXIT", 0xED),
    ("DIR", 0xEE),
    ("DSAVE", 0xEF),
    ("DLOAD", 0xF0),
    ("HEADER", 0xF1),
    ("SCRATCH", 0xF2),
    ("COLLECT", 0xF3),
    ("COPY", 0xF4),
    ("RENAME", 0xF5),
    ("BACKUP", 0xF6),
    ("DELETE", 0xF7),
    ("RENUMBER", 0xF8),
    ("KEY", 0xF9),
    ("MONITOR", 0xFA),
    ("USING", 0xFB),
    ("UNTIL", 0xFC),
    ("WHILE", 0xFD),
    ("POT", 0xCE02),
    ("BUMP", 0xCE03),
    ("PEN", 0xCE04),
    ("RSPPOS", 0xCE05),
    ("RSPRITE", 0xCE06),
    ("RSPCOLOR", 0xCE07),
    ("XOR", 0xCE08),
    ("RWINDOW", 0xCE09),
    ("POINTER", 0xCE0A),
    ("BANK", 0xFE02),
    ("FILTER", 0xFE03),
    ("PLAY", 0xFE04),
    ("TEMPO", 0xFE05),
    ("MOVSPR", 0xFE06),
    ("SPRITE", 0xFE07),
    ("SPRCOLOR", 0xFE08),
    ("RREG", 0xFE09),
    ("ENVELOPE", 0xFE0A),
    ("SLEEP", 0xFE0B),
    ("CATALOG", 0xFE0C),
    ("DOPEN", 0xFE0D),
    ("APPEND", 0xFE0E),
    ("DCLOSE", 0xFE0F),
    ("BSAVE", 0xFE10),
    ("BLOAD", 0xFE11),
    ("RECORD", 0xFE12),
    ("CONCAT", 0xFE13),
    ("DVERIFY", 0xFE14),
    ("DCLEAR", 0xFE15),
    ("SPRSAV", 0xFE16),
    ("COLLISION", 0xFE17),
    ("BEGIN", 0xFE18),
    ("BEND", 0xFE19),
    ("WINDOW", 0xFE1A),
    ("BOOT", 0xFE1B),
    ("WIDTH", 0xFE1C),
    ("SPRDEF", 0xFE1D),
    ("QUIT", 0xFE1E),
    ("OFF", 0xFE24),
    ("FAST", 0xFE25),
    ("SLOW", 0xFE26),
    ("DMA", 0xFE1F),
    ("DMA", 0xFE21),
    ("DMA", 0xFE23),
    ("TYPE", 0xFE27),
    ("BVERIFY", 0xFE28),
    ("ECTORY", 0xFE29),
    ("ERASE", 0xFE2A),
    ("FIND", 0xFE2B),
    ("CHANGE", 0xFE2C),
    ("SET", 0xFE2D),
    ("SCREEN", 0xFE2E),
    ("POLYGON", 0xFE2F),
    ("ELLIPSE", 0xFE30),
    ("VIEWPORT", 0xFE31),
    ("GCOPY", 0xFE32),
    ("PEN", 0xFE33),
    ("PALETTE", 0xFE34),
    ("DMODE", 0xFE35),
    ("DPAT", 0xFE36),
    ("PIC", 0xFE37),
    ("GENLOCK", 0xFE38),
    ("FOREGROUND", 0xFE39),
    ("BACKGROUND", 0xFE3B),
    ("BORDER", 0xFE3C),
    ("HIGHLIGHT", 0xFE3D)
]


class C10(Dialect):
    id = 'Commodore BASIC 10.0'
    keywords = c1_0_keywords + c2_0_keywords + c10_0_keywords
    specials = SPECIALS2


atbasic_keywords = [
    ("TRACE", 0xCC),
    ("DELETE", 0xCD),
    ("AUTO", 0xCE),
    ("OLD", 0xCF),
    ("DUMP", 0xD0),
    ("FIND", 0xD1),
    ("RENUMBER", 0xD2),
    ("DLOAD", 0xD3),
    ("DSAVE", 0xD4),
    ("DVERIFY", 0xD5),
    ("DIRECTORY", 0xD6),
    ("CATALOG", 0xD7),
    ("SCRATCH", 0xD8),
    ("COLLECT", 0xD9),
    ("RENAME", 0xDA),
    ("COPY", 0xDB),
    ("BACKUP", 0xDC),
    ("DISK", 0xDD),
    ("HEADER", 0xDE),
    ("APPEND", 0xDF),
    ("MERGE", 0xE0),
    ("MLOAD", 0xE1),
    ("MVERIFY", 0xE2),
    ("MSAVE", 0xE3),
    ("KEY", 0xE4),
    ("BASIC", 0xE5),
    ("RESET", 0xE6),
    ("EXIT", 0xE7),
    ("ENTER", 0xE8),
    ("DOKE", 0xE9),
    ("SET", 0xEA),
    ("HELP", 0xEB),
    ("SCREEN", 0xEC),
    ("LOMEM", 0xED),
    ("HIMEM", 0xEE),
    ("COLOUR", 0xEF),
    ("TYPE", 0xF0),
    ("TIME", 0xF1),
    ("DEEK", 0xF2),
    ("HEX$", 0xF3),
    ("BIN$", 0xF4),
    ("OFF", 0xF5),
    ("ALARM", 0xF6)
]


class AtBASIC(Dialect):
    id = '@BASIC'
    keywords = c1_0_keywords + c2_0_keywords + atbasic_keywords
    specials = SPECIALS2


simons_keywords = [
    ("HIRES", 0x6401),
    ("PLOT", 0x6402),
    ("LINE", 0x6403),
    ("BLOCK", 0x6404),
    ("FCHR", 0x6405),
    ("FCOL", 0x6406),
    ("FILL", 0x6407),
    ("REC", 0x6408),
    ("ROT", 0x6409),
    ("DRAW", 0x640A),
    ("CHAR", 0x640B),
    ("HI COL", 0x640C),
    ("INV", 0x640D),
    ("FRAC", 0x640E),
    ("MOVE", 0x640F),
    ("PLACE", 0x6410),
    ("UPB", 0x6411),
    ("UPW", 0x6412),
    ("LEFTW", 0x6413),
    ("LEFTB", 0x6414),
    ("DOWNB", 0x6415),
    ("DOWNW", 0x6416),
    ("RIGHTB", 0x6417),
    ("RIGHTW", 0x6418),
    ("MULTI", 0x6419),
    ("COLOUR", 0x641A),
    ("MMOB", 0x641B),
    ("BFLASH", 0x641C),
    ("MOB SET", 0x641D),
    ("MUSIC", 0x641E),
    ("FLASH", 0x641F),
    ("REPEAT", 0x6420),
    ("PLAY", 0x6421),
    (">>", 0x6422),
    ("CENTRE", 0x6423),
    ("ENVELOPE", 0x6424),
    ("CGOTO", 0x6425),
    ("WAVE", 0x6426),
    ("FETCH", 0x6427),
    ("AT(", 0x6428),
    ("UNTIL", 0x6429),
    (">>", 0x642A),
    (">>", 0x642B),
    ("USE", 0x642C),
    (">>", 0x642D),
    ("GLOBAL", 0x642E),
    (">>", 0x642F),
    ("RESET", 0x6430),
    ("PROC", 0x6431),
    ("CALL", 0x6432),
    ("EXEC", 0x6433),
    ("END PROC", 0x6434),
    ("EXIT", 0x6435),
    ("END LOOP", 0x6436),
    ("ON KEY", 0x6437),
    ("DISABLE", 0x6438),
    ("RESUME", 0x6439),
    ("LOOP", 0x643A),
    ("DELAY", 0x643B),
    (">>", 0x643C),
    (">>", 0x643D),
    (">>", 0x643E),
    (">>", 0x643F),
    ("SECURE", 0x6440),
    ("DISAPA", 0x6441),
    ("CIRCLE", 0x6442),
    ("ON ERROR", 0x6443),
    ("NO ERROR", 0x6444),
    ("LOCAL", 0x6445),
    ("RCOMP", 0x6446),
    ("ELSE", 0x6447),
    ("RETRACE", 0x6448),
    ("TRACE", 0x6449),
    ("DIR", 0x644A),
    ("PAGE", 0x644B),
    ("DUMP", 0x644C),
    ("FIND", 0x644D),
    ("OPTION", 0x644E),
    ("AUTO", 0x644F),
    ("OLD", 0x6450),
    ("JOY", 0x6451),
    ("MOD", 0x6452),
    ("DIV", 0x6453),
    (">>", 0x6454),
    ("DUP", 0x6455),
    ("INKEY", 0x6456),
    ("INST", 0x6457),
    ("TEST", 0x6458),
    ("LIN", 0x6459),
    ("EXOR", 0x645A),
    ("INSERT", 0x645B),
    ("POT", 0x645C),
    ("PENX", 0x645D),
    (">>", 0x645E),
    ("PENY", 0x645F),
    ("SOUND", 0x6460),
    ("GRAPHICS", 0x6461),
    ("DESIGN", 0x6462),
    ("RLOCMOB", 0x6463),
    ("CMOB", 0x6464),
    ("BCKGNDS", 0x6465),
    ("PAUSE", 0x6466),
    ("NRM", 0x6467),
    ("MOB OFF", 0x6468),
    ("OFF", 0x6469),
    ("ANGL", 0x646A),
    ("ARC", 0x646B),
    ("COLD", 0x646C),
    ("SCRSV", 0x646D),
    ("SCRLD", 0x646E),
    ("TEXT", 0x646F),
    ("CSET", 0x6470),
    ("VOL", 0x6471),
    ("DISK", 0x6472),
    ("HRDCPY", 0x6473),
    ("KEY", 0x6474),
    ("PAINT", 0x6475),
    ("LOW COL", 0x6476),
    ("COPY", 0x6477),
    ("MERGE", 0x6478),
    ("RENUMBER", 0x6479),
    ("MEM", 0x647A),
    ("DETECT", 0x647B),
    ("CHECK", 0x647C),
    ("DISPLAY", 0x647D),
    ("ERR", 0x647E),
    ("OUT", 0x647F)
]


class Simons(Dialect):
    id = "Simon's BASIC"
    keywords = c1_0_keywords + c2_0_keywords + simons_keywords
    specials = SPECIALS2


speech_keywords = [
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


class Speech(Dialect):
    id = 'Speech BASIC'
    keywords = c1_0_keywords + c2_0_keywords + speech_keywords
    specials = SPECIALS2


sb_keywords = [
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


class SuperBASIC(Dialect):
    id = 'SuperBASIC'
    keywords = c1_0_keywords + c2_0_keywords + sb_keywords
    specials = SPECIALS2


turtle_keywords = [
    ("GRAPHIC", 0xCC),
    ("OLD", 0xCD),
    ("TURN", 0xCE),
    ("PEN", 0xCF),
    ("DRAW", 0xD0),
    ("MOVE", 0xD1),
    ("POINT", 0xD2),
    ("KILL", 0xD3),
    ("WRITE", 0xD4),
    ("REPEAT", 0xD5),
    ("SCREEN", 0xD6),
    ("DOKE", 0xD7),
    ("RELOC", 0xD8),
    ("FILL", 0xD9),
    ("RTIME", 0xDA),
    ("BASE", 0xDB),
    ("PAUSE", 0xDC),
    ("POP", 0xDD),
    ("COLOR", 0xDE),
    ("MERGE", 0xDF),
    ("CHAR", 0xE0),
    ("TAKE", 0xE1),
    ("SOUND", 0xE2),
    ("VOL", 0xE3),
    ("PUT", 0xE4),
    ("PLACE", 0xE5),
    ("CLS", 0xE6),
    ("ACCEPT", 0xE7),
    ("RESET", 0xE8),
    ("GRAB", 0xE9),
    ("RDOT", 0xEA),
    ("PLR$", 0xEB),
    ("DEEK", 0xEC),
    ("JOY", 0xED)
]


class Turtle(Dialect):
    id = 'Turtle BASIC'
    keywords = c1_0_keywords + c2_0_keywords + turtle_keywords
    specials = SPECIALS2


DIALECTS = {
    '1.0': (C1, 0x0401), '2.0': (C2, 0x0801), '3.5': (C35, 0x1001),
    '4.0': (C4, 0x0401), '4.0x': (C4X, 0x0801), '7.0': (C7, 0x1c01),
    '10.0': (C10, 0x0801), 'pet': (C2, 0x0401), 'pet1': (C1, 0x0401),
    'pet2': (C2, 0x0401), 'pet4': (C4, 0x0401), 'vic20': (C2, 0x1001),
    'turtle': (Turtle, 0x1001), 'c16': (C35, 0x1001), 'c64': (C2, 0x0801),
    'c64_4.0': (C4X, 0x0801), 'super': (SuperBASIC, 0x0801),
    'simons': (Simons, 0x0801), 'speech': (Speech, 0x0801),
    'atbasic': (AtBASIC, 0x0801), 'c128': (C7, 0x1c01),
}
