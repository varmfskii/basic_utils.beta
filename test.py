#!/usr/bin/env python3

import sys

from basic69 import Options, Parser
from msbasic.optimize import Optimizer
from msbasic.tokens import no_ws


def main(program, args):
    functions = {
        'g': gotofn, 'goto': gotofn,
        'i': i2xfn, 'i2x': i2xfn,
        'l': labsfn, 'labels': labsfn,
        'r': remfn, 'rems': remfn,
        'w': nowsfn, 'nows': nowsfn,
        'z': z2pfn, 'z2p': z2pfn,
        'h': helpfn, 'help': helpfn,
    }
    if program in functions.keys():
        functions[program](args)
    else:
        helpfn(program)


def z2pfn(args):
    opts = Options(args, ext='z2p')

    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read())
    optimizer = Optimizer(pp)
    optimizer.z2p()
    open(opts.oname, 'w').write(pp.deparse())


def labsfn(args):
    opts = Options(args, ext='lab')

    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read())
    optimizer = Optimizer(pp)
    optimizer.clean_labs()
    open(opts.oname, 'w').write(pp.deparse())


def gotofn(args):
    opts = Options(args, ext='goto')

    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read())
    optimizer = Optimizer(pp)
    optimizer.data = no_ws(optimizer.data)
    optimizer.clean_goto()
    open(opts.oname, 'w').write(pp.deparse(optimizer.data, ws=True))


def i2xfn(args):
    opts = Options(args, ext='i2x')

    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read())
    optimizer = Optimizer(pp)
    optimizer.i2x()
    open(opts.oname, 'w').write(pp.deparse())


def remfn(args):
    opts = Options(args, ext='rem')

    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read())
    optimizer = Optimizer(pp)
    optimizer.no_remarks()
    open(opts.oname, 'w').write(pp.deparse(optimizer.data))


def nowsfn(args):
    opts = Options(args, ext='ws')

    for o, a in opts.unused:
        assert False, f'unhandled option [{o}]'

    pp = Parser(opts, open(opts.iname, 'rb').read())
    pp.full_parse = no_ws(pp.full_parse)
    open(opts.oname, 'w').write(pp.deparse())


def helpfn(program):
    if program:
        fh = sys.stderr
        fh.write(f'Error: Unknown function: {program}\n')
    elif program in ['h', 'help']:
        fh = sys.stdout
    else:
        fh = sys.stderr
        fh.write(f'Error: No function specified\n')
    fh.write(
        "Usage: {sys.argv[0]} <function> <options> <infile> [<outfile>]\n"
        "\nFunctions:\n"
        "\thelp\t\tprint this help message\n"
        "\ti2x\n"
        "\tlabels\n"
        "\tnows\n"
        "\trems\n"
        "\tz2p\n"
        "\nCommon Options:\n"
        "\t-a<a>\t--address=<addy>\tStarting memory address\n"
        "\t-b<d>\t--basic=<dialect\tBASIC dialect\n"
        "\t-c\t--cassette\t\tCassette file format\n"
        "\t-d\t--disk\t\t\tDisk file format\n"
        "\t-h\t--help\t\t\tHelp message\n"
        "\t-i<n>\t--input=<file>\t\tinput file\n"
        "\t-o<n>\t--output=<file>\t\toutput file\n"
    )


if __name__ == "__main__":
    if len(sys.argv) == 1:
        helpfn(None)
    else:
        main(sys.argv[1], sys.argv[2:])
