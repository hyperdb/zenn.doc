---
title: "［AtCoder］ABC-143｜B - TAKOYAKI FESTIVAL 2019"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-143 B - TAKOYAKI FESTIVAL 2019](https://atcoder.jp/contests/abc143/tasks/abc143_b)

## 提出結果

```python
import itertools


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    d = getIntList()

    print(sum([x * y for x, y in itertools.combinations(d, 2)]))


if __name__ == "__main__":
    main()
```
