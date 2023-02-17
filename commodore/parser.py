# parse Microsoft BASIC dialects, may be useful for some others
import sys

from msbasic.parser import Parser as MSParser
from .petscii import a2p, p2a


class Parser(MSParser):

    def parse(self, data: list[int], fix_data=False) -> list[list[tuple]]:
        if data[0] < 0x80 and data[1] < 0x80:
            if self.opts.petscii:
                data = a2p(data, mixed=self.opts.mixed)
            self.full_parse = self.parse_txt("".join(map(chr, data)), fix_data=fix_data)
        else:
            self.full_parse = self.parse_bin(data, fix_data=fix_data)
        return self.full_parse

    def deparse_line(self, line, ws=False):
        out = super().deparse_line(line, ws=ws)
        if self.opts.petscii:
            out = "".join(map(chr, p2a(list(map(ord, out)), self.opts.mixed)))
        return out


if __name__ == "__main__":
    sys.stderr.write("This is a library")
