---
title: "［AtCoder］ABC-363｜B - Japanese Cursed Doll"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-363 B - Japanese Cursed Doll](https://atcoder.jp/contests/abc363/tasks/abc363_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, T, P = getIntMap()
    L = getIntList()
    L.sort()
    L.reverse()

    x = L[P - 1]
    print(0 if x >= T else T - x)


if __name__ == "__main__":
    main()
```
