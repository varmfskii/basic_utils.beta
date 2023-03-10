# parse Microsoft BASIC dialects, may be useful for some others
import sys

from msbasic.parser import Parser as MSParser
from msbasic.tokens import Token


class Parser(MSParser):
    def parse(self, data: [int], fix_data=False, onepass=False) -> [[Token]]:
        if data[0] == 0xff:  # decb
            self.full_parse = self.kws_bin(data[3:])
        else:
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
        return self.get_tokens(move_data=fix_data)


if __name__ == "__main__":
    sys.stderr.write("This is a library")
