---
title: "［AtCoder］ABC-227｜A - Last Card"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-227 A - Last Card](https://atcoder.jp/contests/abc227/tasks/abc227_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def num(i, n):
    return n if i % n == 0 else i % n


def main():
    n, k, a = getIntMap()

    p = [num(i, n) for i in range(a, a + k)]

    print(p[-1])


if __name__ == "__main__":
    main()
```
