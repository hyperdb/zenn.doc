---
title: "［AtCoder］ABC-288｜B - Qualification Contest"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-288 B - Qualification Contest](https://atcoder.jp/contests/abc288/tasks/abc288_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n, k = getIntMap()
    s = getStringRow(n)
    t = [w for w in s[0:k]]

    t.sort()

    for hn in t:
        print(hn)


if __name__ == "__main__":
    main()
```
