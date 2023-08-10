class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def gen(ss):
    root = Node(3, None)
    prev = root
    for i in ss[1:]:
        curr = Node(i, None)
        prev.next = curr
        prev = curr
    return root


def print_list(s):
    print('[', end='')
    curr = s
    while curr:
        print(curr.data, end='')
        if curr.next != None:
            print(', ', end='')
        curr = curr.next
    print(']')

def palindrome(s):
    # rev
    curr = s
    last = None
    while curr:
        # print(curr.data, end='')
        rnode = Node(curr.data, last)
        last = rnode
        curr = curr.next

    # algo
    curr_left = s
    curr_right = rnode
    while True:
        if curr_left == None:
            break
        # print(curr_left.data, curr_right.data)
        if curr_left.data != curr_right.data:
            return False
        curr_left = curr_left.next
        curr_right = curr_right.next
    return True

def sub_list(s, t):
    pivot = s
    while True:
        curr_s = pivot
        curr_t = t
        while True:
            if curr_t == None:
                # print('found')
                return True
            if curr_s == None:
                return False

            # print(curr_s.data, curr_t.data)
            if curr_s.data == curr_t.data:
                pass
            else:
                break
            curr_s = curr_s.next
            curr_t = curr_t.next

        pivot = pivot.next
    return False


if __name__ == '__main__':
    s = gen([3, 7, 6, 8])
    print(print_list(s))
    s = gen([1, 2, 1])
    print(palindrome(s))
    s = gen([1, 2, 1, 3, 1])
    # t = gen([1, 3, 1])
    # t = gen([2, 1, 3])
    t = gen([1, 3, 1])
    print(sub_list(s, t))