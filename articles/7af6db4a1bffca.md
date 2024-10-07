---
title: "［AtCoder］ABC-373｜B - 1D Keyboard"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-372 B - 1D Keyboard](https://atcoder.jp/contests/abc373/tasks/abc373_b)

## 提出結果

```python
def getString():
    return input()


def main():
    S = list(getString())
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    p = [S.index(x) for x in a]
    q = [abs(p[i] - p[i - 1]) for i in range(1, len(p))]

    print(sum(q))


if __name__ == "__main__":
    main()
```
