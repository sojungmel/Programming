ans = ''
def foo(s):
    global ans
    ans = ''
    adj = {}
    for ix, i in enumerate(s):
        if i not in adj:
            adj[i] = set([])
        if ix > 0:
            adj[i] = adj[i].union(set([s[ix - 1]]))
        if ix < len(s) - 1:
            adj[i] = adj[i].union(set([s[ix + 1]]))

    cnt = {}
    for i in s:
        if i in cnt:
            cnt[i] = cnt[i] + 1
        else:
            cnt[i] = 1

    # cnt = {}
    # for i in s:
    #     if i in cnt:
    #         continue
    #     else:
    #         cnt[i] = 1

    # print(cnt)

    def func(ori, cnt, used, buf):
        global ans
        # print(used)
        if used >= len(ori):
            # print('found')
            ans = buf
            return
        else:
            for i in cnt:
                if cnt[i] <= 0:
                    continue
                else:
                    if len(buf) <= 0 or i not in adj[buf[-1]]:
                        cnt_new = cnt.copy()
                        cnt_new[i] = cnt_new[i] - 1
                        func(ori, cnt_new, used + 1, buf + [i])

    func(s, cnt, 0, [])
    # print(''.join(ans))
    ret = ''.join(ans)
    return ret

def bar(s):
    global ans
    ans = ''
    adj = {}
    for ix, i in enumerate(s):
        if i not in adj:
            adj[i] = set([])
        if ix > 0:
            adj[i] = adj[i].union(set([s[ix - 1]]))
        if ix < len(s) - 1:
            adj[i] = adj[i].union(set([s[ix + 1]]))

    cnt = {}
    for i in s:
        if i in cnt:
            continue
        else:
            cnt[i] = 1

    # print(cnt)

    def func(ori, cnt, used, buf):
        global ans
        # if used >= len(ori):
        if used >= len(cnt):
            # print('found')
            ans = buf
            return
        else:
            for i in cnt:
                if cnt[i] <= 0:
                    continue
                else:
                    if len(buf) <= 0 or i not in adj[buf[-1]]:
                        cnt_new = cnt.copy()
                        cnt_new[i] = cnt_new[i] - 1
                        func(ori, cnt_new, used + 1, buf + [i])

    func(s, cnt, 0, [])
    # print(''.join(ans))
    ret = ''.join(ans)
    return ret

if __name__ == '__main__':
    s = 'abcde'
    s = 'abc'
    # s = ''
    # s = 'cacebd'
    s = 'abcdcef'
    print(foo(s))
    print(bar(s))