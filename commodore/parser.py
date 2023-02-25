# parse Microsoft BASIC dialects, may be useful for some others
import sys

from msbasic.parser import Parser as MSParser
from .petscii import a2p, p2a


class Parser(MSParser):
    def __init__(self, opts, data=None, fix_data=False):
        super().__init__(opts, data=data, be=False, fix_data=fix_data)
        self.petscii = opts.petscii
        self.mixed = opts.mixed

    def parse(self, data: [int], fix_data=False, onepass=False) -> [[tuple[int, str, any]]]:
        binary = False
        for d in data:
            if d == 0:
                binary = True
                break
        if binary:
            self.full_parse = self.kws_bin(data)
        else:
            if self.petscii:
                data = a2p(data, mixed=self.mixed)
            self.full_parse = self.kws_txt(data)
        if onepass:
            return self.full_parse
        return self.get_tokens(fix_data=fix_data)

    def deparse_line(self, line, ws=False):
        out = super().deparse_line(line, ws=ws)
        if self.petscii:
            out = "".join(map(chr, p2a(list(map(ord, out)), self.mixed)))
        return out


if __name__ == "__main__":
    sys.stderr.write("This is a library")
