---
title: "［AtCoder］ABC-375｜A - Seats"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-375 A - Seats](https://atcoder.jp/contests/abc375/tasks/abc375_a)

## 提出結果

```python
def getInt():
    return int(input())


def getString():
    return input()


def main():
    N = getInt()
    S = list(getString())

    c = 0
    for i in range(1, N - 1):
        if S[i] != ".":
            continue
        if S[i - 1] == S[i + 1] == "#":
            c += 1
    print(c)


if __name__ == "__main__":
    main()
```
