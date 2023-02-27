#!/usr/bin/env python3

import sys

from msbasic.options import Options
from msbasic.parser import Parser
from msbasic.labels import renumber
from msbasic.optimize import Optimizer, split_lines, OFlags
from msbasic.variables import reid
from msbasic.tokens import tokenize


def main():
    functions = {
        'd': detokenizefn, 'detokenize': detokenizefn,
        'f': fixfn, 'fix_data': fixfn,
        'h': helpfn, 'help': helpfn,
        'p': packfn, 'pack': packfn,
        'ri': reidfn, 'reid': reidfn,
        'rn': renumberfn, 'renum': renumberfn, 'renumber': renumberfn,
        't': tokenizefn, 'tokenize': tokenizefn,
        'u': unpackfn, 'unpack': unpackfn
    }
    if sys.argv[1] in functions.keys():
        functions[sys.argv[1]]()
    else:
        helpfn()


def detokenizefn():
    opts = Options(sys.argv[2:], ext='txt')

    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read(), onepass=True)
    open(opts.oname, 'w').write(pp.deparse())


def fixfn():
    opts = Options(sys.argv[2:], ext='txt')

    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read(), fix_data=True)
    open(opts.oname, 'w').write(pp.deparse())


def packfn():
    usage = [
        "\t-D\t--move-data\t\tmove DATA statements to end\n",
        "\t-P\t--point\t\t\tconvert 0 to .\n",
        "\t-X\t--hex\t\t\tconvert integers to &Hhex form\n",
        "\t-k\t--token-len\t\tline length is for tokenized form\n",
        "\t-m\t--maxline=<num>\t\tmaximum line length\n",
        "\t-t\t--text\t\t\toutput as text file\n",
        "\t-x\t--text-len\t\tline length is for untokenized form\n"
    ]
    lopts = ['move-data', 'token-len', 'maxline=', 'text', 'text-len', 'point', 'quotes', 'hex']
    astokens = True
    oflags = OFlags(0)
    opts = Options(sys.argv[2:], sopts='DPQXkm:tx', lopts=lopts, usage=usage, ext='pack')
    max_len = 0
    for o, a in opts.unused:
        if o in ['-D', '--fix-data']:
            oflags |= OFlags.MOVDAT
        elif o in ['-P', '--point']:
            oflags |= OFlags.Z2P
        elif o in ['-Q', '--quotes']:
            oflags |= OFlags.QUOTE
        elif o in ['-X', '--hex']:
            oflags |= OFlags.I2X
        elif o in ['-k', '--token-len']:
            oflags &= ~OFlags.TXTLEN
        elif o in ['-m', '--maxline']:
            max_len = int(a)
            if max_len < 0:
                sys.stderr.write(f'length must be non-negative\n')
                sys.exit(2)
        elif o in ['-t', '--text']:
            astokens = False
        elif o in ['-x', '--text-len']:
            oflags |= OFlags.TXTLEN
        else:
            assert False, f'unhandled option: [{o}]'
    pp = Parser(opts, open(opts.iname, 'rb').read(), fix_data=OFlags.MOVDAT in oflags)
    optimizer = Optimizer(pp)
    optimizer.opt(max_len=max_len, flags=oflags)
    if astokens:
        open(opts.oname, 'wb').write(tokenize(optimizer.data, opts))
    else:
        open(opts.oname, 'w').write(pp.deparse(optimizer.data))


def reidfn():
    astokens = True
    usage = ["\t-t\t--text\t\t\toutput as text file\n"]
    lopts = ["text"]
    opts = Options(sys.argv[2:], sopts='t', lopts=lopts, usage=usage, ext='reid')
    for o, a in opts.unused:
        if o in ['-t', '--text']:
            astokens = False
        else:
            assert False, f'unhandled option [{o}]'
    pp = Parser(opts, open(opts.iname, 'rb').read())
    data = reid(pp)
    if astokens:
        open(opts.oname, 'wb').write(tokenize(data, opts))
    else:
        open(opts.oname, 'w').write(pp.deparse(data))


def renumberfn():
    astokens = True
    usage = [
        '\t-s<n>\t--start=<num>\t\tstarting line number\n',
        '\t-t\t--text\t\t\toutput as text file\n',
        '\t-v<n>\t--interval=<num>\tinterval between line numbers\n'
    ]
    lopts = ["start=", "interval=", 'text']
    opts = Options(sys.argv[2:], sopts='s:tv:', lopts=lopts, usage=usage, ext='renum')
    start = 10
    interval = 10
    for o, a in opts.unused:
        if o in ["-s", "--start"]:
            start = int(a)
            if start < 0 or start > 32767:
                sys.stderr.write(f'Illegal starting line number: {start}\n')
                sys.exit(2)
        elif o in ['-t', '--text']:
            astokens = False
        elif o in ["-v", "--interval"]:
            interval = int(a)
            if interval < 1:
                sys.stderr.write(f'Illegal line number interval: {interval}\n')
                sys.exit(2)
        else:
            assert False, "unhandled option"
    pp = Parser(opts, open(opts.iname, 'rb').read())
    data = renumber(pp.full_parse, start=start, interval=interval)
    if astokens:
        open(opts.oname, 'wb').write(tokenize(data, opts))
    else:
        open(opts.oname, 'w').write(pp.deparse(data))


def tokenizefn():
    opts = Options(sys.argv[2:], ext='tok')
    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'
    pp = Parser(opts, open(opts.iname, 'rb').read(), onepass=True)
    open(opts.oname, 'wb').write(tokenize(pp.full_parse, opts))


def unpackfn():
    lo = ["no-whitespace"]
    us = ["\t-n\t--no-whitespace\t\tdo not add extra whitespace\n"]
    opts = Options(sys.argv[2], sopts='n', lopts=lo, usage=us, ext='txt')
    ws = True
    for o, a in opts.unused:
        if o in ['-n', '--no-whitespace']:
            ws = False
        else:
            assert False, f'unhandled option: [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read())
    data = split_lines(pp)
    open(opts.oname, 'w').write(pp.deparse(data, ws=ws))


def helpfn():
    if len(sys.argv) > 1 and sys.argv[1] in ['h', 'help']:
        fh = sys.stdout
    elif len(sys.argv) > 1:
        fh = sys.stderr
        fh.write(f'Error: Unknown function: {sys.argv[1]}\n')
    else:
        fh = sys.stderr
        fh.write(f'Error: No function specified\n')

    opts = Options(sys.argv[2:])
    usage = opts.usage
    usage.sort()
    fh.write(f'Usage: {sys.argv[0]} <function> <options> <infile> [<outfile>]\n')
    fh.write(
        "\nFunctions:\n"
        "\thelp\t\tprint this help message\n"
        "\tdetokenize\tconvert to a text file\n"
        "\tpack\t\tremove extraneous space, pack lines together, etc.\n"
        "\treid\t\tconvert long identifiers to no more than two characters.\n"
        "\trenumber\trenumber lines.\n"
        "\ttokenize\tconvert to tokenized form\n"
        "\tunpack\t\tsplit lines and insert whitespace\n"
        "\nCommon Options:\n"
    )
    for line in usage:
        fh.write(line)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        helpfn()
    else:
        main()
