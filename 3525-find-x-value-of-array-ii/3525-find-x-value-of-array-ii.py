class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [(1, [0] * k) for _ in range(4 * n)]

        def merge(left, right):
            prod1, pref1 = left
            prod2, pref2 = right

            prod = (prod1 * prod2) % k

            pref = [0] * k

            for r in range(k):
                pref[r] += pref1[r]

            for r in range(k):
                new_rem = (prod1 * r) % k
                pref[new_rem] += pref2[r]

            return (prod, pref)

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                pref = [0] * k
                pref[rem] = 1

                tree[node] = (rem, pref)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                rem = value % k

                pref = [0] * k
                pref[rem] = 1

                tree[node] = (rem, pref)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if r < ql or l > qr:
                return None

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            if left is None:
                return right

            if right is None:
                return left

            return merge(left, right)

        # Build tree
        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            update(1, 0, n - 1, index, value)

            result = query(1, 0, n - 1, start, n - 1)

            answer.append(result[1][x])

        return answer