import sys

from msbasic.options import Options as BaseOptions
from msbasic.dialect import Dialect

basica_keywords = [
    ("'", 0x3A8FD9), ("*", 0xEB), ("+", 0xE9), ("-", 0xEA), ("/", 0xEC),
    ("<", 0xE8), ("=", 0xE7), (">", 0xE6), ("ABS", 0xFF86), ("AND", 0xEE),
    ("ASC", 0xFF95), ("ATN", 0xFF8E), ("AUTO", 0xAA), ("BEEP", 0xC5),
    ("BLOAD", 0xC3), ("BSAVE", 0xC2), ("CALL", 0xB3), ("CALLS", 0xFEA1),
    ("CDBL", 0xFF9E), ("CHAIN", 0xFE8C), ("CHDIR", 0xFE97), ("CHR$", 0xFF96),
    ("CINT", 0xFF9C), ("CIRCLE", 0xFE91), ("CLEAR", 0x92), ("CLOSE", 0xBB),
    ("CLS", 0xC0), ("COLOR", 0xBF), ("COM", 0xFE90), ("COMMON", 0xFE8B),
    ("CONT", 0x99), ("COS", 0xFF8C), ("CSNG", 0xFF9D), ("CSRLIN", 0xDB),
    ("CVD", 0xFD83), ("CVI", 0xFD81), ("CVS", 0xFD82), ("DATA", 0x84),
    ("DATE$", 0xFE8D), ("DEF", 0x97), ("DEFDBL", 0xAF), ("DEFINT", 0xAD),
    ("DEFSNG", 0xAE), ("DEFSTR", 0xAC), ("DELETE", 0xA9), ("DIM", 0x86),
    ("DRAW", 0xFE92), ("EDIT", 0xA6), ("ELSE", 0x3AA1), ("END", 0x81),
    ("ENVIRON", 0xFE9B), ("EOF", 0xFFA3), ("EQV", 0xF1), ("ERASE", 0xA5),
    ("ERDEV", 0xFE95), ("ERL", 0xD4), ("ERR", 0xD5), ("ERROR", 0xA7),
    ("EXP", 0xFF8B), ("EXTERR", 0xFD8B), ("FIELD", 0xFE82), ("FILES", 0xFE81),
    ("FIX", 0xFF9F), ("FN", 0xD1), ("FOR", 0x82), ("FRE", 0xFF8F),
    ("GET", 0xFE89), ("GOSUB", 0x8D), ("GOTO", 0x89), ("HEX$", 0xFF9A),
    ("IF", 0x8B), ("IMP", 0xF2), ("INKEY$", 0xDE), ("INP", 0xFF90),
    ("INPUT", 0x85), ("INSTR", 0xD8), ("INT", 0xFF85), ("IOCTL", 0xFE96),
    ("KEY", 0xC9), ("KILL", 0xFE87), ("LCOPY", 0xFEA0), ("LEFT$", 0xFF81),
    ("LEN", 0xFF92), ("LET", 0x88), ("LINE", 0xB0), ("LIST", 0x93),
    ("LLIST", 0x9E), ("LOAD", 0xBC), ("LOC", 0xFFA4), ("LOCATE", 0xCA),
    ("LOCK", 0xFEA7), ("LOF", 0xFFA5), ("LOG", 0xFF8A), ("LPOS", 0xFF9B),
    ("LPRINT", 0x9D), ("LSET", 0xFE85), ("MERGE", 0xBD), ("MID$", 0xFF83),
    ("MKD$", 0xFD86), ("MKDIR", 0xFE98), ("MKI$", 0xFD84), ("MKS$", 0xFD85),
    ("MOD", 0xF3), ("MOTOR", 0xC1), ("NAME", 0xFE84), ("NEW", 0x94),
    ("NEXT", 0x83), ("NOT", 0xD3), ("OCT$", 0xFF99), ("OFF", 0xDD),
    ("ON", 0x95), ("OPEN", 0xBA), ("OPTION", 0xB8), ("OR", 0xEF), ("OUT", 0x9C),
    ("PAINT", 0xFE8F), ("PALETTE", 0xFE9F), ("PEEK", 0xFF97), ("PEN", 0xFFA0),
    ("PLAY", 0xFE93), ("PMAP", 0xFE9E), ("POINT", 0xDC), ("POKE", 0x98),
    ("POS", 0xFF91), ("PRESET", 0xC7), ("PRINT", 0x91), ("PSET", 0xC6),
    ("PUT", 0xFE88), ("RANDOMIZE", 0xB9), ("READ", 0x87), ("REM", 0x8F),
    ("RENUM", 0xAB), ("RESET", 0xFE8A), ("RESTORE", 0x8C), ("RESUME", 0xA8),
    ("RETURN", 0x8E), ("RIGHT$", 0xFF82), ("RMDIR", 0xFE99), ("RND", 0xFF88),
    ("RSET", 0xFE86), ("RUN", 0x8A), ("SAVE", 0xBE), ("SCREEM", 0xC8),
    ("SGN", 0xFF84), ("SHELL", 0xFE9A), ("SIN", 0xFF89), ("SOUND", 0xC4),
    ("SPACE$", 0xFF98), ("SPC(", 0xD2), ("SQR", 0xFF87), ("STEP", 0xCF),
    ("STICK", 0xFFA1), ("STOP", 0x90), ("STR$", 0xFF93), ("STRIG", 0xFFA2),
    ("STRING$", 0xD6), ("SWAP", 0xA4), ("SYSTEM", 0xFE83), ("TAB(", 0xCE),
    ("TAN", 0xFF8D), ("THEN", 0xCD), ("TIME$", 0xFE8E), ("TIMER", 0xFE94),
    ("TO", 0xCC), ("TROFF", 0xA3), ("TRON", 0xA2), ("UNLOCK", 0xFEA8),
    ("USING", 0xD7), ("USR", 0xD0), ("VAL", 0xFF94), ("VARPTR", 0xDA),
    ("VIEW", 0xFE9C), ("WAIT", 0x96), ("WEND", 0xB2), ("WHILE", 0xB1E9),
    ("WIDTH", 0xA0), ("WINDOW", 0xFE9D), ("WRITE", 0xB7), ("XOR", 0xE0),
    ("\\", 0xF4), ("^", 0xED)
]


class BASICA(Dialect):
    id = 'BASICA'
    ketwords = basica_keywords


class EGA(Dialect):
    id = 'EGA BASIC'
    keywords = basica_keywords + [("PCOPY", 0xFEA5)]


class PCJr(Dialect):
    id = 'PC Jr. BASIC'
    keywords = basica_keywords + [
        ("NOISE", 0xFEA4), ("PCOPY", 0xFEA5), ("TERM", 0xFEA6)
    ]


class Sperry(Dialect):
    id = 'Sperry BASIC'
    keywords = basica_keywords + [("DEBUG", 0xFEA4)]


DIALECTS = {'basica': BASICA, 'ega': EGA, 'pcjr': PCJr, 'sperry': Sperry}


class Options(BaseOptions):
    dialects = DIALECTS


if __name__ == "__main__":
    sys.stderr.write("This is a library")
