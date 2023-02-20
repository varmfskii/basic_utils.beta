import sys

from msbasic.options import Options as BaseOptions
from msbasic.tokens import tokenize_line
from .dialects import DIALECTS, DBCSE
from .parser import Parser


class Options(BaseOptions):
    disk = None
    sopts = "b:cd" + BaseOptions.sopts
    lopts = ["basic=", "cassette", "disk"] + BaseOptions.lopts
    usage = BaseOptions.usage + [
        '\t-b\t--basic=<dialect>\tbasic dialect\n',
        '\t-c\t--cassette\t\ttokenized cassette file\n',
        '\t-d\t--disk\t\t\ttokenized disk file (default)\n'
    ]

    dialect = None

    def subopts(self, other):
        (o, a) = other
        if o in ["-b", "--basic"]:
            if a in DIALECTS.keys():
                self.dialect = DIALECTS[a]()
            elif a == "help":
                print("Supported dialects:")
                for key in DIALECTS.keys():
                    print(f'\t{key}:\t{DIALECTS[key].id}')
                sys.exit(0)
            else:
                sys.stderr.write(f'Unsupported dialect: {a}\n')
                sys.stderr.write("--basic=help to list available dialects")
                sys.exit(2)
        elif o in ["-c", "--cassette"]:
            self.disk = False
        elif o in ["-d", "--disk"]:
            self.disk = True
        else:
            self.unused.append(other)

    def post(self):
        if self.dialect is None:
            self.dialect = DBCSE()
        if self.disk is None:
            self.disk = self.dialect.disk
        if self.address == 0x0000:
            if self.disk or (self.disk is None and self.dialect.disk):
                self.address = 0x2601
            else:
                self.address = 0x25fe


def tokenize(data, opts):
    # convert a parsed file into tokenized BASIC file
    tokenized = []
    address = opts.address
    for line in data:
        line_tokens = tokenize_line(line)
        address += 2 + len(line_tokens)
        tokenized += [address // 0x100, address & 0xff] + line_tokens
    tokenized += [0, 0]
    if opts.disk and opts.isdragon:
        val = len(tokenized)
        tokenized = [0x55, 0x01, 0x24, 0x01, val // 256, val & 0xff, 0x8b, 0x8d, 0xaa] + tokenized
    elif opts.disk:
        val = len(tokenized)
        tokenized = [0xff, val // 0x100, val & 0xff] + tokenized
    return bytearray(tokenized)


if __name__ == "__main__":
    sys.stderr.write("This is a library")
