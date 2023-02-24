#!/usr/bin/env python3
import re

from msbasic.tokens import Token, matchkw


class Parser:
    full_parse = None

    def __init__(self, opts, data=None, be=True, fix_data=False, onepass=False):
        self.be = be
        self.code2kw = opts.dialect.code2kw
        self.kw2code = opts.dialect.kw2code
        self.kw_keys = opts.dialect.kw_keys
        self.specials = opts.dialect.specials
        self.then_kw = self.specials['THEN'] + self.specials['ELSE']
        self.branch_kw = self.specials['GO'] + self.specials['GOTO'] + self.specials['GOSUB']
        self.ign_kw = self.specials['TO'] + self.specials['SUB']
        if data:
            self.parse(data, fix_data=fix_data, onepass=onepass)

    def parse(self, data: [int], fix_data=False, onepass=False) -> [[tuple[int, str] or tuple[int, str, int]]]:
        binary = False
        for d in data:
            if d == 0:
                binary = True
                break
        if binary:
            self.full_parse = self.kws_bin(data)
        else:
            self.full_parse = self.kws_txt(data)
        if onepass:
            return self.full_parse
        return self.get_tokens(fix_data=fix_data)

    def get_tokens(self, data=None, fix_data=False) -> [[tuple[int, str] or tuple[int, str, int]]]:
        if not data:
            data = self.full_parse
        parsed = []
        data_data = ''
        for line in data:
            new_line = []
            for token in line:
                if token[0] == Token.NONE:
                    new_line += self.parse_none(token[1])
                elif token[0] == Token.DATA:
                    new_data = ''
                    inquote = False
                    for c in token[1]:
                        if inquote or c != ' ':
                            new_data += c
                        if c == '"':
                            inquote = not inquote
                    if fix_data:
                        if data_data:
                            data_data += ',' + new_data
                        else:
                            data_data = new_data
                        if len(new_line) >= 2 and new_line[-2][0] == ord(':'):
                            new_line = new_line[:-2]
                        else:
                            new_line = new_line[:-1]
                    else:
                        new_line.append((Token.DATA, new_data))
                else:
                    new_line.append(token)
            if new_line:
                label = 0
                for ix, token in enumerate(new_line):
                    # adjust to labels where applicable
                    if (label and token[0] == Token.NUM) or (label == 2 and token[0] == Token.ID):
                        new_line[ix] = (Token.LABEL, token[1])
                    # setup for label detection
                    if token[0] == Token.KW and token[1] in self.then_kw:
                        label = 1
                    elif token[0] == Token.KW and token[1] in self.branch_kw:
                        label = 2
                    elif label == 1 or (label == 2 and token[0] not in [Token.ID, Token.NUM, ord(',')]
                                        and not (token[0] == Token.KW and token[1] in self.ign_kw)):
                        label = 0
                    else:
                        pass
                parsed.append(new_line)
        if data_data:
            parsed += [(Token.KW, 'DATA', self.kw2code['DATA']), (Token.DATA, data_data)]
        self.full_parse = parsed
        return self.full_parse

    @staticmethod
    def parse_none(data: str) -> [tuple[int, str]]:
        data = re.sub(' ', '', data).upper()
        tokens = []
        while data != '':
            match = re.match(r'[A-Z][0-9A-Z]*\$\(', data)
            if match:
                tokens += [(Token.STRARR, match.group(0)[:-2]), (ord('$'), '$'), (ord('('), '(')]
                data = data[match.end():]
                continue
            match = re.match(r'[A-Z][0-9A-Z]*\$\(', data)
            if match:
                tokens += [(Token.STRARR, match.group(0)[:-1]), (ord('$'), '$')]
                data = data[match.end():]
                continue
            match = re.match(r'[A-Z][0-9A-Z]*\$', data)
            if match:
                tokens += [(Token.STRARR, match.group(0)[:-1]), (ord('('), '(')]
                data = data[match.end():]
                continue
            match = re.match(r'[A-Z][0-9A-Z]*', data)
            if match:
                tokens.append((Token.ID, match.group(0)))
                data = data[match.end():]
                continue
            match = re.match(r'&H[0-9A-F]*', data)
            if match:
                tokens.append((Token.HEX, match.group(0)))
                data = data[match.end():]
                continue
            match = re.match(r'[0-9]*\.[0-9]*(E[+-]?[0-9]*)', data)
            if match:
                tokens.append((Token.FLOAT, match.group(0)))
                data = data[match.end():]
                continue
            match = re.match(r'[0-9]+', data)
            if match:
                tokens.append((Token.NUM, match.group(0)))
                data = data[match.end():]
                continue
            tokens.append((ord(data[0]), data[0]))
            data = data[1:]
        return [(Token.NONE, data)]

    def kws_txt(self, data_i: [int]) -> [[tuple[int, str] or tuple[int, str, int]]]:
        parsed = []
        data = cont_line("".join(map(chr, data_i)))
        for linein in re.split('[\n\r]+', data):
            if linein == "":
                continue
            match1 = re.match(' *([0-9]+) *', linein)
            match2 = re.match(' *([A-Za-z][0-9A-Za-z]*): *', linein)
            if match1:
                line = [(Token.LABEL, match1.group(1))]
                linein = linein[match1.end():]
            elif match2:
                line = [(Token.LABEL, match2.group(1))]
                linein = linein[match2.end():]
            else:
                line = []
                match = re.match(' *', linein)
                linein = linein[match.end():]
            while linein != '':
                if len(line) and matchkw(line[-1], self.specials['REM']):
                    line.append((Token.REM, linein))
                    linein = ''
                    continue
                if len(line) and matchkw(line[-1], self.specials['DATA']):
                    match = re.match('[^:]+', linein)
                    if match:
                        line.append((Token.DATA, match.group(0)))
                        linein = linein[match.end():]
                    continue

                kw = self.match_kw(linein)
                if kw:
                    linein = linein[len(kw[1]):]
                    line.append(kw)
                    continue

                match = re.match('"[^"]*"?', linein)
                if match:
                    ml = match.end()
                    quoted = linein[:ml]
                    if quoted[-1] != '"':
                        quoted += '"'
                    line.append((Token.QUOTED, quoted))
                    linein = linein[ml:]
                    continue

                match = re.match('.|([A-Za-z][0-9A-Za-z]*)', linein)
                if len(line) and line[-1][0] == Token.NONE:
                    line[-1] = (Token.NONE, line[-1][1] + match.group(0))
                else:
                    line.append((Token.NONE, match.group(0)))
                linein = linein[match.end():]
            parsed.append(line)
        return parsed

    def kws_bin(self, data: [int]) -> [[tuple[int, str] or tuple[int, str, int]]]:
        parsed = []
        while len(data) >= 2 and data[0] or data[1]:
            if self.be:
                tokens = [(Token.LABEL, data[2] * 0x0100 + data[3])]
            else:
                tokens = [(Token.LABEL, data[2] + data[3] * 0x0100)]
            data = data[4:]
            while data[0]:
                if len(tokens) and matchkw(tokens[-1], self.specials['REM']):
                    remark = ''
                    while data[0]:
                        remark += chr(data[0])
                        data = data[1:]
                    tokens.append((Token.REM, remark))
                    continue
                if len(tokens) and matchkw(tokens[-1], self.specials['DATA']):
                    data_data = ''
                    while data[0] and data[0] != ord(':'):
                        data_data += chr(data[0])
                        data = data[1:]
                    if data_data:
                        tokens.append((Token.DATA, data_data))
                    continue
                c1 = data[0]
                if len(data) > 1:
                    c2 = c1 * 0x100 + data[1]
                else:
                    c2 = c1 * 0x100
                if len(data) > 2:
                    c3 = c2 * 0x100 + data[2]
                else:
                    c3 = c2 * 0x100
                if c3 in self.code2kw.keys():
                    # 3-byte token
                    data = data[3:]
                    tokens.append((Token.KW, self.code2kw[c3], c3))
                    continue
                if c2 in self.code2kw.keys():
                    # 2-byte token
                    data = data[2:]
                    tokens.append((Token.KW, self.code2kw[c2], c2))
                    continue
                if c1 in self.code2kw.keys():
                    # 1-byte token
                    data = data[1:]
                    tokens.append((Token.KW, self.code2kw[c1], c1))
                    continue
                next_chr = chr(data[0])
                if 'A' <= next_chr <= 'Z' or 'a' <= next_chr <= 'z':
                    datum = ''
                    while ('0' <= next_chr <= '9' or
                           'A' <= next_chr <= 'Z' or
                           'a' <= next_chr <= 'z'):
                        datum += next_chr
                        data = data[1:]
                        next_chr = chr(data[0])
                    if len(tokens) and tokens[-1][0] == Token.NONE:
                        tokens[-1] = (Token.NONE, tokens[-1][1] + datum)
                    else:
                        tokens.append((Token.NONE, datum))
                    continue
                if len(tokens) and tokens[-1][0] == Token.NONE:
                    tokens[-1] = (Token.NONE, tokens[-1][1] + chr(data[0]))
                else:
                    tokens.append((Token.NONE, chr(data[0])))
                data = data[1:]
            if tokens:
                parsed.append(tokens)
        return parsed

    @staticmethod
    def split_none(s: str) -> [tuple[int, str]]:
        tokens = []
        while s != '':
            match = re.match('[0-9]*\\.[0-9]*', s)
            if match and match.end() > 0:
                ml = match.end()
                tokens.append((Token.FLOAT, s[:ml]))
                s = s[ml:]
                continue
            match = re.match('[0-9]*(\\.[0-9]*)?[+-]?[Ee][0-9]*', s)
            if match and match.end() > 0:
                ml = match.end()
                tokens.append((Token.FLOAT, s[:ml]))
                s = s[ml:]
                continue
            match = re.match('[0-9]*', s)
            if match and match.end() > 0:
                ml = match.end()
                tokens.append((Token.NUM, s[:ml]))
                s = s[ml:]
                continue
            match = re.match('&H[0-9A-Fa-f]*', s)
            if match and match.end() > 0:
                ml = match.end()
                tokens.append((Token.HEX, s[:ml]))
                s = s[ml:]
                continue
            match = re.match(' *', s)
            if match and match.end() > 0:
                ml = match.end()
                tokens.append((Token.WS, s[:ml]))
                s = s[ml:]
                continue
            tokens.append((ord(s[0]), s[0]))
            s = s[1:]
        return tokens

    def match_kw(self, line) -> tuple or None:
        ll = len(line)
        for kw in self.kw_keys:
            kl = len(kw)
            if ll >= kl and kw == line[:kl].upper():
                return Token.KW, kw, self.kw2code[kw]
        return None

    def deparse(self, data=None, ws=False) -> str:
        out = ''
        if not data:
            data = self.full_parse
        for line in data:
            out += self.deparse_line(line, ws)
        return out

    def deparse_line(self, line, ws=False):
        if line[0][0] == Token.LABEL:
            out = line[0][1] + ' '
            line = line[1:]
        else:
            out = ' '
        for ix, token in enumerate(line):
            if (token[0] == Token.KW and token[1][0].isalpha() and ix > 0
                    and line[ix - 1][0] in [Token.ID, Token.STR, Token.ARR, Token.STRARR]):
                out += ' '
            if ws and out[-1].isalnum() and token[1][0].isalnum():
                out += ' '
            if token[0] in [Token.QUOTED, Token.DATA, Token.REM]:
                out += token[1]
            else:
                out += token[1].upper()
        out += '\n'
        return out


def cont_line(data: str) -> str:
    data = data.split('\\')
    s = data[0]
    for p in data[1:]:
        m = re.match('\r?\n?', p)
        if m.end() == 0:
            s += '\\' + p
        else:
            s += p[m.end():]
    return s
