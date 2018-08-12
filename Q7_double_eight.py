def double_eights(n):
    ''' Return true if n has two eights in a row.'''

    n = str(n)

    if n == '':
        return False
    else:
        if n.find('88') >= 0:
            return True
        else:
            return False

print(double_eights(80808080))