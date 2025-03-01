def o_m_s(l):
    if len(l) <= 1: return l
    m = len(l) // 2
    l_h = o_m_s(l[:m])
    r_h = o_m_s(l[m:])
    r = []
    i = j = 0
    while i < len(l_h) and j < len(r_h):
        if l_h[i] < r_h[j]: r.append(l_h[i]); i += 1
        else: r.append(r_h[j]); j += 1
    r.extend(l_h[i:])
    r.extend(r_h[j:])
    return r

def obf_sort(a):
    _1 = lambda x: x[0] if len(x) == 1 else None
    _2 = lambda x, y: x > y
    _3 = lambda x, y: x + y
    _4 = lambda x: len(x)
    _5 = lambda x: x // 2
    _6 = lambda x, y: x[y:]
    _7 = lambda x, y: x[:y]
    _8 = lambda x, y: x.extend(y)
    _9 = lambda x, y: x.append(y)
    _10 = lambda x, y: x[y]
    _11 = lambda x: [] if not x else x
    _12 = lambda x: x[0]
    _13 = lambda x: x[1:]
    _14 = lambda x : len(x) <= 1
    _15 = lambda x : len(x)//2
    _16 = lambda x,y : x[y:]
    _17 = lambda x,y : x[:y]

    if _14(a): return a
    b = _15(a)
    c = obf_merge_sort(_17(a,b))
    d = obf_merge_sort(_16(a,b))
    e = _11([])
    f = g = 0
    while f < _4(c) and g < _4(d):
        if _3(_10(c,f), _10(d,g)):
            _9(e, _10(c,f))
            f += 1
        else:
            _9(e, _10(d,g))
            g += 1
    _8(e, _16(c,f))
    _8(e, _16(d,g))
    return e