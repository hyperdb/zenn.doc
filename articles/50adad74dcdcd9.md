---
title: "［AtCoder］ABC-067｜B Snake Toy"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-067 B - Snake Toy](https://atcoder.jp/contests/abc067/tasks/abc067_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    l = getIntList()

    d = sorted(l, reverse=True)

    print(sum(d[:k]))


if __name__ == "__main__":
    main()
```
