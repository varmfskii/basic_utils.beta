from msbasic.labels import clean_labs, renumber, clean_goto
from msbasic.tokens import no_ws, Token
from msbasic.variables import reid


def no_remarks(data):
    # remove all "unnecessary" remarks
    lines = []

    for line in data:
        for tix, token in enumerate(line):
            if token[0] == Token.REM:
                if tix > 1 and line[tix - 2][0] == ord(':'):
                    line = line[:tix - 2]
                else:
                    line = line[:tix - 1]
                break
        if len(line) != 0:
            lines.append(line)

    return lines


def merge_lines(pp, data=None, max_len=0, text_len=False):
    # merge lines in program together where possible to a limit of
    # maxlen (if maxlen is not 0)
    lines = []
    nextline = []
    if text_len:
        old_len = 1
    else:
        old_len = 4
    line_no = 0

    if not data:
        data = pp.full_parse
    for line in data:
        if not line:
            continue
        next_len = get_len(pp, line, text_len=text_len)
        if line[0][0] == Token.LABEL or 0 < max_len < old_len + 1 + next_len:
            if nextline:
                lines.append(nextline)
                line_no += 1
            nextline = line
            old_len = next_len
            if text_len:
                old_len += len(str(line_no)) + 1
            else:
                old_len += 5
        else:
            if nextline:
                if len(nextline) > 1 or nextline[0][0] != Token.LABEL:
                    nextline += [(ord(':'), ':')]
                    old_len += 1
                nextline += line
                old_len += next_len
            else:
                nextline = line
                old_len = 5 + next_len
        for token in line:
            if token[0] == Token.KW and token[1].upper() == 'IF':
                lines.append(nextline)
                line_no += 1
                nextline = []
                if text_len:
                    old_len = len(str(line_no))
                else:
                    old_len = 4
                break

    if nextline:
        lines.append(nextline)
    return lines


def split_lines(data):
    lines = []
    for line in data:
        start = 0
        for ix, field in enumerate(line):
            if field[1].upper() in ["REM", "'", "IF"]:
                break
            if field[0] == ord(':'):
                lines.append(line[start:ix])
                start = ix + 1
        lines.append(line[start:])
    return lines


def get_len(pp, line, text_len=False):
    if len(line) == 0:
        return 0
    if line[0][0] == Token.LABEL:
        line = line[1:]
    if text_len:
        return len(pp.deparse(line))
    len_acc = 0
    for token in line:
        if token[0] != Token.KW:
            len_acc += len(token[1])
        elif token[2] < 0x100:
            len_acc += 1
        elif token[2] < 0x10000:
            len_acc += 2
        else:
            len_acc += 3

    return len_acc


def pack(pp, data=None, max_len=0, text_len=False):
    # pack a basic program
    if not data:
        data = pp.full_parse
    data = no_remarks(clean_goto(clean_labs(no_ws(data))))
    data = reid(pp, data=data)
    data = merge_lines(pp, data=data, max_len=max_len, text_len=text_len)
    data = renumber(data, start=0, interval=1)
    return data
