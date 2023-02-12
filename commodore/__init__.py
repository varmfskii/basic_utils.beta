import sys

from commodore import c1_0, c2_0, c3_5, c4_0, c4_0x, c7_0, c10_0
from commodore import atbasic, simons, speech, superbasic, turtle
from msbasic.options import Options as BaseOptions
from msbasic.tokens import tokenize_line
from .parser import Parser


class Options(BaseOptions):
    DIALECTS = {
        '1.0': (c1_0.keywords, c1_0.remarks, 0x0401),
        '2.0': (c2_0.keywords, c1_0.remarks, 0x0801),
        '3.5': (c3_5.keywords, c1_0.remarks, 0x1001),
        '4.0': (c4_0.keywords, c1_0.remarks, 0x0401),
        '7.0': (c7_0.keywords, c1_0.remarks, 0x1c01),
        '10.0': (c10_0.keywords, c1_0.remarks, 0x0801),
        'pet': (c2_0.keywords, c1_0.remarks, 0x0401),
        'pet1': (c1_0.keywords, c1_0.remarks, 0x0401),
        'pet2': (c2_0.keywords, c1_0.remarks, 0x0401),
        'pet4': (c4_0.keywords, c1_0.remarks, 0x0401),
        'vic20': (c2_0.keywords, c1_0.remarks, 0x1001),
        'c16': (c3_5.keywords, c1_0.remarks, 0x1001),
        'c64': (c2_0.keywords, c1_0.remarks, 0x0801),
        'c128': (c7_0.keywords, c1_0.remarks, 0x1c01),
        'c64_4.0': (c4_0x.keywords, c1_0.remarks, 0x0801),
        'super': (superbasic.keywords, c1_0.remarks, 0x0801),
        'simons': (simons.keywords, c1_0.remarks, 0x0801),
        'speech': (speech.keywords, c1_0.remarks, 0x0801),
        'atbasic': (atbasic.keywords, c1_0.remarks, 0x0801),
        'turtle': (turtle.keywords, c1_0.remarks, 0x1001),
    }
    sopts = 'b:pm' + BaseOptions.sopts
    lopts = ['basic=', 'petscii', 'mixed-case'] + BaseOptions.lopts
    usage = BaseOptions.usage + [
        '\t-b\t--basic=<dialect>\tbasic dialect\n',
        '\t-p\t--petscii\tuse petscii\n',
        '\t-m\t--mixed-case\tpetscii is mixed case\n'
    ]
    keywords = c2_0.keywords
    remarks = c1_0.remarks
    petscii = False
    mixed = False
    
    def subopts(self, other):
        (o, a) = other
        if o in ['-b', '--basic']:
            if a in self.DIALECTS.keys():
                self.keywords, self.remarks, address = self.DIALECTS[a]
                if self.address == 0:
                    self.address = address
            elif a == 'help':
                print('Supported dialects:')
                for key in self.DIALECTS.keys():
                    print(f'\t{key}')
                sys.exit(0)
            else:
                sys.stderr.write(f'Unsupported dialect: {a}\n')
                sys.stderr.write("--basic=help to list available dialects\n")
                sys.exit(2)
        elif o in ['-p', '--petscii']:
            petscii = True
        elif o in ['-m', '--mixed-case']:
            mixed = True
        else:
            self.unused.append(other)

    def post(self):
        if self.address == 0x0000:
            self.address = 0x0801


def tokenize(data, opts):
    # convert a parsed file into tokenized BASIC file
    address = opts.address
    tokenized = [address & 0xff, address // 0x100]
    for line in data:
        line_tokens = tokenize_line(line, be=False)
        address += 2 + len(line_tokens)
        tokenized += [address & 0xff, address // 0x0100] + line_tokens
    return bytearray(tokenized)


if __name__ == '__main__':
    sys.stderr.write("This is a library\n")
