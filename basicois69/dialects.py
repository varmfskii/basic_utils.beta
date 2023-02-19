from msbasic.dialect import Dialect

couleur_keywords = [
    ("'", 0x3A83),
    ("*", 0xAD),
    ("+", 0xAB),
    ("-", 0xAC),
    ("/", 0xAE),
    ("<", 0xB4),
    ("=", 0xB3),
    (">", 0xB2),
    ("ABS", 0xFF82),  # abs
    ("ALLER", 0x81),  # go
    ("ALORS", 0xA7),  # then
    ("ARRET", 0x91),  # stop
    ("ASC", 0xFF8A),  # asc
    ("AUDIO", 0xA1),  # audio
    ("CAPTE$", 0xFF92),  # inkey
    ("CAR$", 0xFF8B),  # chr$
    ("CCHARG", 0x97),  # cload
    ("CCHARGM", 0x974d),  # cloadm
    ("CCOPIE", 0x98),  # csave
    ("CCOPIEM", 0x984d),  # csavem
    ("CONTINUE", 0x93),  # cont
    ("DEFINIR", 0x9C),  # set
    ("DEMANDE", 0x89),  # input
    ("DIM", 0x8C),  # dim
    ("DROIT$", 0xFF8F),  # right$
    ("ECRIS", 0x87),  # print
    ("EFF", 0x9E),  # cls
    ("EMPLIS", 0x8D),  # read
    ("ENCORE", 0x8B),  # next
    ("ENT", 0xFF81),  # int
    ("EOF", 0xFF8C),  # eof
    ("ET", 0xB0),  # and
    ("EXE", 0x8E),  # run
    ("EXEC", 0xA2),  # exec
    ("FERME", 0x9A),  # close
    ("FIN", 0x8A),  # end
    ("GARNIS", 0x92),  # poke
    ("GAUCHE$", 0xFF8E),  # left$
    ("HSD", 0xFF84),  # rnd
    ("IMAGE", 0xFF86),  # peek
    ("INFOS", 0x86),  # data
    ("JUSQUE", 0xA5),  # to
    ("LISTAGE", 0x9B),  # llist
    ("LISTE", 0x94),  # list
    ("LONG", 0xFF87),  # len
    ("MANETTE", 0xFF8D),  # joystk
    ("MEM", 0xFF93),  # mem
    ("MOTOR", 0x9F),  # motor
    ("NBRE", 0xFF89),  # val
    ("NETTOIE", 0x96),  # new
    ("NON", 0xA8),  # not
    ("OFF", 0xAA),  # off *
    ("OU", 0xB1),  # or
    ("OUVRE", 0x99),  # open
    ("PAR", 0xA9),  # step
    ("PARTIE$", 0xFF90),  # mis$
    ("POINT", 0xFF91),  # point
    ("RAZ", 0x95),  # clear
    ("REINIT", 0x9D),  # reset
    ("REM", 0x82),  # rem
    ("REPETE", 0x80),  # for
    ("RESTAURE", 0x8F),  # restore
    ("REVIENS", 0x90),  # return
    ("SAUTERF", 0xA3),  # skipf
    ("SELON", 0x88),  # on
    ("SGN", 0xFF80),  # sgn
    ("SI", 0x85),  # if
    ("SIN", 0xFF85),  # sin
    ("SINON", 0x3A84),  # else
    ("SOUND", 0xA0),  # sound
    ("SOUS", 0xA6),  # sub
    ("TAB(", 0xA4),  # tab(
    ("TXT$", 0xFF88),  # str$
    ("USR", 0xFF83),  # usr
    ("VATEN", 0x81A5),  # goto
    ("VAVIENS", 0x81A6),  # gosub
    ("^", 0xAF),
]

ext_keywords = [
    ("ADRESSE", 0xFF9D),  # varptr
    ("ATN", 0xFF94),  # atn
    ("CERCLE", 0xC2),  # circle
    ("CHAINE$", 0xFFA1),  # string$
    ("COS", 0xFF95),  # cos
    ("COULEUR", 0xC1),  # color
    ("DCHARGE", 0xCA),  # dload
    ("DCHARGEM", 0xca4d),  # dloadm
    ("DEF", 0xB9),  # def
    ("DEL", 0xB5),  # del
    ("ECRAN", 0xBF),  # screen
    ("EXP", 0xFF97),  # exp
    ("FAIS", 0xBA),  # let
    ("FIX", 0xFF98),  # fix
    ("FN", 0xCC),  # fn
    ("HEX$", 0xFF9C),  # hex$
    ("INTXT", 0xFF9E),  # instr
    ("JOUER", 0xC9),  # play
    ("LIGNE", 0xBB),  # line
    ("LOG", 0xFF99),  # log
    ("MODIFIER", 0xB6),  # edit
    ("PCOPIE", 0xC7),  # pcopy
    ("PDEFINIR", 0xBD),  # pset
    ("PEFF", 0xBC),  # pcls
    ("PIENDRE", 0xC3),  # paint
    ("PMODE", 0xC8),  # pmode
    ("POS", 0xFF9A),  # pos
    ("PPOINT", 0xFFA0),  # ppoint
    ("PRAZ", 0xC0),  # pclear
    ("PREINIT", 0xBE),  # preset
    ("PRENDS", 0xC4),  # get
    ("RAC", 0xFF9B),  # sqr
    ("RANGE", 0xC5),  # put
    ("RENUM", 0xCB),  # renum
    ("SUIVANT", 0xCD),  # using
    ("TAN", 0xFF96),  # tan
    ("TE", 0xFF9F),  # timer
    ("TRACE", 0xC6),  # draw
    ("TROFF", 0xB8),  # troff
    ("TRON", 0xB7),  # tron
]

disque_keywords = [
    ("CHAMPS", 0xD0),  # field
    ("CHANGENOM", 0xD6),  # rename
    ("CHARGE", 0xD3),  # load
    ("CHARGEM", 0xd34d),  # loadm
    ("COPIE", 0xD8),  # save
    ("COPIEM", 0xd84d),  # savem
    ("COPIER", 0xDE),  # copy
    ("CVN", 0xFFA2),  # cvn
    ("DETRUIS", 0xD2),  # kill
    ("DOS", 0xE1),  # dos
    ("DSQI$", 0xDF),  # dski$
    ("DSQO$", 0xE0),  # dsko$
    ("DSQSTR", 0xDC),  # dskini
    ("ECRIT", 0xD9),  # write
    ("FERME", 0xDB),  # unload
    ("FORME", 0xFFA7),  # as
    ("FUSIONNE", 0xD5),  # merge
    ("JUSTD", 0xD7),  # rset
    ("JUSTG", 0xD4),  # lset
    ("LIBRE", 0xFFA3),  # free
    ("LOC", 0xFFA4),  # loc
    ("LOF", 0xFFA5),  # lof
    ("MKN$", 0xFFA6),  # mkn$
    ("REP", 0xCE),  # dir
    ("REPODUIT", 0xDD),  # backup
    ("TAMPONS", 0xD1),  # files
    ("UNITE", 0xCF),  # drive
    ("VERIFICATION", 0xDA),  # verify
]

super_keywords = [
    ("ATTR", 0xF8),  # attr
    ("BOUTON", 0xFFA9),  # button
    ("CASS", 0xF0),  # brk
    ("CMP", 0xF6),  # cmp
    ("ERR", 0xEF),  # err
    ("HCERCLE", 0xE9),  # hcircle
    ("HCOULEUR", 0xE7),  # hcolor
    ("HDEFINIR", 0xF3),  # hset
    ("HECRAN", 0xE4),  # hscreen
    ("HECRIS", 0xEE),  # hprint
    ("HEFF", 0xE6),  # hcls
    ("HLIGNE", 0xEA),  # hline
    ("HPIENDRE", 0xE8),  # hpaint
    ("HPOINT", 0xFFAA),  # hpoint
    ("HPREINIT", 0xF4),  # hreset
    ("HPRENDS", 0xEB),  # hget
    ("HRANGE", 0xEC),  # hput
    ("HSTAT", 0xF2),  # hstat
    ("HTAMP", 0xED),  # hbuff
    ("HTRACE", 0xF5),  # hdraw
    ("LARGEUR", 0xE2),  # width
    ("LGARNIS", 0xE5),  # lpoke
    ("LIMAGE", 0xFFA8),  # lpeek
    ("LINER", 0xFFAC),  # hlin
    ("LOCALISER", 0xF1),  # locate
    ("NUMER", 0xFFAB),  # erno
    ("PALETTE", 0xE3),  # palette
    ("RGB", 0xF7),  # rgb
]


class DialectFR(Dialect):
    specials = {
        'DATA': ['INFOS'],
        'ELSE': ['SINON'],
        'FOR': ['REPETE'],
        'GO': ['ALLER'],
        'GOSUB': ['VAVIENS'],
        'GOTO': ['VATEN'],
        'IF': ['SI'],
        'NEXT': ['ENCORE'],
        'REM': ['REM', "'"],
        'SUB': ['SOUS'],
        'THEN': ['ALORS'],
        'TO': ['JUSQUE']
    }


class BC(DialectFR):
    id = 'Basicois couleur'
    keywords = couleur_keywords
    dragon = False
    disk = False


class BCE(DialectFR):
    id = 'Basicois coluleur étendu'
    keywords = couleur_keywords + ext_keywords
    dragon = False
    disk = False


class DBCE(DialectFR):
    id = 'Disque Basicois couleur étendu'
    keywords = couleur_keywords + ext_keywords + disque_keywords
    dragon = False
    disk = True


class BCSE(DialectFR):
    id = 'Basicois coluleur étendu 2.x'
    keywords = couleur_keywords + ext_keywords + super_keywords
    dragon = False
    disk = False


class DBCSE(DialectFR):
    id = 'Disque Basicois couleur étendu 2.x'
    keywords = couleur_keywords + ext_keywords + super_keywords + disque_keywords
    dragon = False
    disk = True


DIALECTS = {'bc': BC, 'bce': BCE, 'dbce': DBCE, 'bcse': BCSE, 'dbcse': DBCSE}
