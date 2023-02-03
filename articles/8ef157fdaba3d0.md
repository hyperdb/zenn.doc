---
title: "［AtCoder］ABC-115｜B - Christmas Eve Eve"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-115 B - Christmas Eve Eve](https://atcoder.jp/contests/abc115/tasks/abc115_b)

## 提出結果

```python
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    n = getInt()
    p = getIntRow(n)

    p.sort()
    p.reverse()

    p[0] = p[0] // 2

    print(sum(p))


if __name__ == "__main__":
    main()```
