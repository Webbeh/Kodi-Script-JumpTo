import sys
import xbmc

TAG = '[jumpto] '
def log(m): xbmc.log(TAG + m, xbmc.LOGINFO)

def item_key(cid, i):
    L = xbmc.getInfoLabel('Container(%s).ListItemAbsolute(%d).SortLetter' % (cid, i))
    if not L:
        L = xbmc.getInfoLabel('Container(%s).ListItemAbsolute(%d).Label' % (cid, i))[:1]
    return L.upper()

def matches(key, target):
    if target.isalpha():
        return key == target
    # target is a digit or '#': match the first numeric/symbol-sorted item
    return key[:1].isdigit() or key[:1] == '#'

def main():
    if len(sys.argv) < 2 or not sys.argv[1]:
        return
    target = sys.argv[1][:1].upper()

    cid = xbmc.getInfoLabel('System.CurrentControlID')
    if not cid:
        log('no focused control'); return
    try:
        n = int(xbmc.getInfoLabel('Container(%s).NumItems' % cid) or 0)
    except ValueError:
        n = 0
    if n <= 0:
        log('control %s is empty or not a list' % cid); return

    for i in range(n):
        if matches(item_key(cid, i), target):
            xbmc.executebuiltin('SetFocus(%s,%d,absolute)' % (cid, i))
            log('jumped to %r at index %d' % (target, i))
            return
    log('%r not present' % target)

if __name__ == '__main__':
  main()
