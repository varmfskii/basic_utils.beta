# parse Microsoft BASIC dialects, may be useful for some others
import sys

from msbasic.parser import Parser as MSParser
from .petscii import a2p, p2a

class Parser(MSParser):

    def parse(self, data: list[int]) -> list[list[tuple]]:
        if data[0] < 0x80 and data[1] < 0x80:
            if self.opts.petscii:
                data = p2a(data, mixed=self.opts.mixed)
            self.full_parse = self.parse_txt("".join(map(chr, data)))
        else:
            self.full_parse = self.parse_bin(data)
        return self.full_parse

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
        if self.opts.petscii:
            out = "".join(map(chr, a2p(list(map(ord, out)), self.opts.mixed)))
        return out


if __name__ == "__main__":
    sys.stderr.write("This is a library")
