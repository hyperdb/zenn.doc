---
title: "［AtCoder］ABC-324｜B - 3-smooth Numbers"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-324 B - 3-smooth Numbers](https://atcoder.jp/contests/abc324/tasks/abc324_b)

## 提出結果

```python
def getInt():
    return int(input())


def div(n, x):
    while n % x == 0:
        n //= x
    return n


def main():
    n = getInt()

    print('Yes' if div(div(n, 2), 3) == 1 else 'No')


if __name__ == "__main__":
    main()
```
