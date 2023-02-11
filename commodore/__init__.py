import sys

from commodore import atbasic, c1_0, c2_0, c2_0super, c4_0, c4_0x, c7_0, c10_0
from commodore import simons, superbasic, turtle 

from msbasic.options import Options as BaseOptions


class Options(BaseOptions):
    sopts = 'b:' + BaseOptions.sopts
    lopts = ['basic='] + BaseOptions.lopts
    usage = ['\t-b<d>\t--basic=<dialect>\tbasic dialect\n'] + BaseOptions.usage
    keywords = c2_0.keywords
    remarks = c1_0.remarks
    dialects = {
        "1.0": (c1_0.keywords, c1_0.remarks),
        "2.0": (c2_0.keywords, c1_0.remarks),
        "3.5": (c3_5.keywords, c1_0.remarks),
        "4.0": (c4_0.keywords, c1_0.remarks),
        "7.0": (c7_0.keywords, c1_0.remarks),
        "10.0": (c10_0.keywords, c1_0.remarks),
        "pet": (c2_0.keywords, c1_0.remarks),
        "pet1": (c1_0.keywords, c1_0.remarks),
        "pet2": (c2_0.keywords, c1_0.remarks),
        "pet4": (c4_0.keywords, c1_0.remarks),
        "vic20": (c2_0.keywords, c1_0.remarks),
        "c16": (c3_5.keywords, c1_0.remarks),
        "c64": (c2_0.keywords, c1_0.remarks),
        "c128": (c7_0.keywords, c1_0.remarks),
        "c64_4.0": (c4_0x.keywords, c1_0.remarks),
        "super": (superbasic.keywords, c1_0.remarks),
        "simons": (simons.keywords, c1_0.remarks),
        "speech": (speech.keywords, c1_0.remarks),
        "atbasic": (atbasic.keywords, c1_0.remarks),
        "turtle": (turtle.keywords, c1_0.remarks),
    }

    def subopts(self, other):
        o, a = other
        if o in ["-b", "--basic"]:
            if a in self.dialects.keys():
                self.keywords, self.remarks = dialects[a]
            elif a == "help":
                print("Supported dialects:")
                for key in self.dialects.keys():
                    print(f'\t{key}')
                sys.exit(0)
            else:
                sys.stderr.write(f'Unsupported dialect: {a}\n')
                sys.stderr.write("--basic=help to list available dialects")
                sys.exit(2)
        else:
            self.unused.append((o, a))


if __name__ == "__main__":
    sys.stderr.write("This is a library")
