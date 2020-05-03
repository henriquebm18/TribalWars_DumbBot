

def chancer(tanto, qnts_nbs):
    s = []
    l = range(20,36)

    if qnts_nbs == 5:
        for x in l:
            for w in l:
                for y in l:
                    for z in l:
                        for a in l:
                            s += [x+w+y+z+a]
    elif qnts_nbs == 4:
        for x in l:
            for w in l:
                for y in l:
                    for z in l:
                        s += [x+w+y+z]
    elif qnts_nbs == 3:
        for x in l:
            for w in l:
                for y in l:
                    s += [x+w+y]
    elif qnts_nbs == 2:
        for x in l:
            for w in l:
                s += [x+w]

    p = []
    cs = 0
    for so in set(s):
        if so<tanto:
            pass
        else:
            cs += s.count(so)/len(s)

    print("chance: {:.1f}%".format(cs*100))
