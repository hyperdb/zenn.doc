---
title: "［AtCoder］ABC-338｜C - Leftover Recipes"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-338 C - Leftover Recipes](https://atcoder.jp/contests/abc338/tasks/abc338_c)

## 提出結果

```python
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    q = getIntList()
    a = getIntList()
    b = getIntList()

    max_a = min([q[i] // a[i] if a[i] > 0 else 10 ** 6 for i in range(n)])

    ab = 0
    for x in range(max_a + 1):
        qz = [q[i] - a[i] * x for i in range(n)]
        max_b = min([qz[i] // b[i] if b[i] > 0 else 10 ** 6 for i in range(n)])
        ab = max(ab, x + max_b)
    print(ab)


if __name__ == "__main__":
    main()
```
