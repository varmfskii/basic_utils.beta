import sys

from msbasic.options import Options as BaseOptions
from msbasic.tokens import tokenize_line as mstokenize
from .dialects import DIALECTS, C2
from .parser import Parser


class Options(BaseOptions):
    sopts = 'b:pm' + BaseOptions.sopts
    lopts = ['basic=', 'petscii', 'mixed-case'] + BaseOptions.lopts
    usage = BaseOptions.usage + [
        '\t-b\t--basic=<dialect>\tbasic dialect\n',
        '\t-n\t--not-petscii\tdon\'t use petscii\n',
        '\t-m\t--mixed-case\tpetscii is mixed case\n'
    ]
    dialect = None
    petscii = False
    mixed = False

    def subopts(self, other: tuple[str, str]):
        (o, a) = other
        if o in ['-b', '--basic']:
            if a in DIALECTS.keys():
                self.dialect, address = DIALECTS[a]()
                if self.address == 0:
                    self.address = address
            elif a == 'help':
                print('Supported dialects:')
                for key in DIALECTS.keys():
                    print(f'\t{key}')
                sys.exit(0)
            else:
                sys.stderr.write(f'Unsupported dialect: {a}\n')
                sys.stderr.write("--basic=help to list available dialects\n")
                sys.exit(2)
        elif o in ['-n', '--not-petscii']:
            self.petscii = True
        elif o in ['-m', '--mixed-case']:
            self.mixed = True
        else:
            self.unused.append(other)

    def post(self):
        if self.address == 0x0000:
            self.address = 0x0801
        if not self.dialect:
            self.dialect = C2()


def tokenize(data: [int], opts: Options) -> bytearray:
    # convert a parsed file into tokenized BASIC file
    address = opts.address
    tokenized = [address & 0xff, address // 0x100]
    tokenized += mstokenize(data, opts)
    return bytearray(tokenized)


if __name__ == '__main__':
    sys.stderr.write("This is a library\n")
