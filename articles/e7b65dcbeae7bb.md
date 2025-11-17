---
title: "［AtCoder］ABC-421｜B - Fibonacci Reversed"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["python", "AtCoder", "abc"]
published: true
---

## 設問ページ

-   🔗[ABC-421 B - Fibonacci Reversed](https://atcoder.jp/contests/abc421/tasks/abc421_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def fx(n):
    s = list(f"{n}")
    s.reverse()

    return int("".join(s))


def main():
    X, Y = getIntMap()
    n = [0, X, Y] + [0 for _ in range(10)]

    for i in range(3, 11):
        n[i] = fx(n[i - 1] + n[i - 2])

    print(n[10])


if __name__ == "__main__":
    main()
```
