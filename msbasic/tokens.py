from enum import Enum
from msbasic.options import Options


class Token(Enum):
    NONE = 256
    LABEL = 257
    TOKEN = 258
    ID = 259
    STR = 260
    ARR = 261
    STRARR = 262
    QUOTED = 263
    REM = 264
    DATA = 265
    NUM = 266
    HEX = 267
    FLOAT = 268
    WS = 269
    KW = 270

    def __repr__(self):
        return self.name


def tokenize(data: [[tuple[int, str] or tuple[int, str, int]]], opts: Options, be=True) -> [int]:
    # convert a parsed file into tokenized BASIC file
    address = opts.address
    tokenized = []
    for line in data:
        line_tokens = tokenize_line(line, be=be)
        address += 2 + len(line_tokens)
        if be:
            tokenized += [address // 0x0100, address & 0xff] + line_tokens
        else:
            tokenized += [address & 0xff, address // 0x0100] + line_tokens
    return tokenized


def tokenize_line(line: [tuple[int, str] or tuple[int, str, int]], be=True) -> [int]:
    # convert a parsed line into the tokenized format for a BASIC file
    val = int(line[0][1])
    if be:
        tokens = [val // 256, val & 0xff]
    else:
        tokens = [val & 0xff, val // 256]
    for token in line[1:]:
        if token[0] in [Token.QUOTED, Token.REM, Token.DATA]:
            # explicit text
            for char in token[1]:
                tokens.append(ord(char))
        elif token[0] != Token.KW:
            # code text, interpreter only recognizes uppercase
            for char in token[1]:
                tokens.append(ord(char))
        elif token[2] < 0x100:  # tokenized keyword
            tokens.append(token[2])
        elif token[2] < 0x10000:  # tokenized extended keyword
            tokens += [token[2] // 256, token[2] & 0xff]
        else:  # three byte keyword
            tokens += [token[2] // 0x10000, (token[2] // 0x100) & 0xff, token[2] & 0xff]
    tokens.append(0)
    return tokens


def detokenize_body(data, pp, be=True):
    listing = ""
    ix = 0

    while data[ix] != 0x00 or data[ix + 1] != 0x00:
        if be:
            line = f'{data[ix + 2] * 0x100 + data[ix + 3]} '
        else:
            line = f'{data[ix + 2] + data[ix + 3] * 0x100} '

        ix += 4
        lastid = False
        while data[ix] != 0x00:
            c1 = data[ix]
            ix = ix + 1
            c2 = data[ix]
            if c1 * 0x100 + c2 in pp.code2kw.keys():
                kw = pp.code2kw[c1 * 0x100 + c2]
                ix += 1
                iskw = True
            elif c1 in pp.code2kw.keys():
                kw = pp.code2kw[c1]
                iskw = True
            else:
                kw = chr(c1)
                iskw = False
                if kw.isalpha():
                    # A-Z
                    lastid = True
                elif not kw.isdigit():
                    # not 0-9
                    lastid = False
            if iskw:
                if lastid and kw[0].isalpha():
                    line += ' '
                lastid = False
            line += kw

        ix += 1
        pp.parse_txt(line)
        listing += line + '\n'

    return pp, listing


def no_ws(tokens: list[tuple]) -> list[tuple]:
    rv = []
    for token in tokens:
        if token[0] == Token.QUOTED:
            new_val = ''
            inquote = False
            for c in token[1]:
                if inquote or c != ' ':
                    new_val += c
                if c == '"':
                    inquote = not inquote
            token = (Token.QUOTED, new_val)
        if token[0] != Token.WS:
            rv.append(token)
    return rv


def matchkw(token, kw):
    return token[0] == Token.KW and token[1] in kw
