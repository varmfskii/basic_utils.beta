p2am_m = {0x7e: 0x01fb96, 0x7f: 0x01fb98, 0xa9: 0x01fb99, 0xba: 0x2713}
p2au_m = {
    0x7e: 0x03c0, 0x7f: 0x25e5, 0xa9: 0x25e4, 0xba: 0x01fb7f,
    0x61: 0x2660, 0x62: 0x01fb72, 0x63: 0x01fb78, 0x64: 0x01fb77,
    0x65: 0x01fb76, 0x66: 0x01fb7a, 0x67: 0x01fb71, 0x68: 0x01fb74,
    0x69: 0x256e, 0x6a: 0x2570, 0x6b: 0x256f, 0x6c: 0x01fb7c,
    0x6d: 0x2572, 0x6e: 0x2571, 0x6f: 0x01fb7d, 0x70: 0x01fb7e,
    0x71: 0x25cf, 0x72: 0x01fb7b, 0x73: 0x2665, 0x74: 0x01fb70,
    0x75: 0x256d, 0x76: 0x2573, 0x77: 0x25cb, 0x78: 0x2663,
    0x79: 0x01fb75, 0x7a: 0x2666
}
p2a_m = {
    0x5c: 0xa3, 0x5e: 0x2191, 0x5f: 0x2190, 0x60: 0x01fb79,
    0x7b: 0x253c, 0x7c: 0x01fb8c, 0x7d: 0x01fb8c, 0x7e: 0x2502,
    0xa1: 0x258c, 0xa2: 0x2584, 0xa3: 0x2594, 0xa4: 0x2581,
    0xa5: 0x258f, 0xa6: 0x2592, 0xa7: 0x2595, 0xa8: 0x01fb8f,
    0xaa: 0x01fb87, 0xab: 0x251c, 0xac: 0x2597, 0xad: 0x2514,
    0xae: 0x2510, 0xaf: 0x2582, 0xb0: 0x250c, 0xb1: 0x2534,
    0xb2: 0x252c, 0xb3: 0x2524, 0xb4: 0x2584, 0xb5: 0x258d,
    0xb6: 0x1fb88, 0xb7: 0x01fb82, 0xb8: 0x01fb83, 0xb9: 0x2583,
    0xbb: 0x2596, 0xbc: 0x259d, 0xbd: 0x2518, 0xbe: 0x2598,
    0xbf: 0x259a
}


def p2am(petscii):
    if 0xc0 <= petscii <= 0xdf:
        petscii = (petscii & 0x1f) | 0x60
    elif 0xe0 <= petscii <= 0xff:
        petscii = (petscii & 0x1f) | 0xa0
    if petscii <= 0x40 or petscii in [0x5b, 0x5d, 0xa0]:
        return petscii
    elif 0x41 <= petscii <= 0x5a:
        return petscii | 0x20
    elif 0x61 <= petscii <= 0x7a:
        return petscii & 0xdf
    elif petscii in p2am_m.keys():
        return p2am_m[petscii]
    else:
        return p2a_m[petscii]


def p2au(petscii):
    if 0xc0 <= petscii <= 0xdf:
        petscii = (petscii & 0x1f) | 0x60
    elif 0xe0 <= petscii <= 0xff:
        petscii = (petscii & 0x1f) | 0xa0
    if petscii <= 0x5b or petscii in [0x5d, 0xa0]:
        return petscii
    elif petscii in p2au_m.keys():
        return p2au_m[petscii]
    else:
        return p2a_m[petscii]


data = {}
for a in range(0x20, 0x80):
    c = p2au(a)
    if c != a:
        data[a] = c
for a in range(0xa0, 0x100):
    c = p2au(a)
    if c != a:
        data[a] = c
print(f'p2au = {data}')

data1 = {}
for a in data.keys():
    c = data[a]
    if c not in data1.keys():
        data1[c] = a
print(f'a2pu = {data1}')

data = {}
for a in range(0x20, 0x80):
    c = p2am(a)
    if c != a:
        data[a] = c
for a in range(0xa0, 0x100):
    c = p2am(a)
    if c != a:
        data[a] = c
print(f'p2am = {data}')

data1 = {}
for a in data.keys():
    c = data[a]
    if c not in data1.keys():
        data1[c] = a
print(f'a2pm = {data1}')
