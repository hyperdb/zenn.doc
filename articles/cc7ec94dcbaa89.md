---
title: "［AtCoder］ABC-374｜C - Separated Lunch"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-374 C - Separated Lunch](https://atcoder.jp/contests/abc374/tasks/abc374_c)

## 提出結果

```python
import itertools


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    K = getIntList()

    a = sum(K)
    b = a
    for i in range(1, N):
        c = itertools.combinations(K, i)
        for x in list(c):
            y = sum(x)
            b = min(b, max(y, a - y))
    print(b)


if __name__ == "__main__":
    main()
```
