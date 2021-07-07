def checkMagazine1(magazine, note):
    m = magazine.split()
    n = note.split()
    for i in n:
        if i in m:
            m.pop(m.index(i))
        else:
            print('No')
            return

    print('Yes')


def checkMagazine(magazine, note):
    for i in note:
        if i in magazine:
            magazine.remove(i)
        else:
            print('No')
            return

    print('Yes')


magazine = 'give me one grand today night'
note = 'give one grand today'

magazine = 'ive got a lovely bunch of coconuts'
note = 'ive got some coconuts'

magazine = 'two times three is not four'
note = 'two times two is four'


checkMagazine(magazine.split(), note.split())
