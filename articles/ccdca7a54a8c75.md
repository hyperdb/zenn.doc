---
title: "［AtCoder］ABC-350｜A - Past ABCs"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-350 A - Past ABCs](https://atcoder.jp/contests/abc350/tasks/abc350_a)

## 提出結果

```python
def getString():
    return input()


def main():
    s = getString()
    q = int(s[3:])

    print('Yes' if q != 316 and 0 < q < 350 else 'No')


if __name__ == "__main__":
    main()

```
