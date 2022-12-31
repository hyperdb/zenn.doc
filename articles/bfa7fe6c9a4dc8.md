---
title: "［AtCoder］ABC-070｜A Palindromic Number"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-070 A - Palindromic Number](https://atcoder.jp/contests/abc070/tasks/abc070_a)

## 提出結果

```python
def getString():
    return input()


def main():
    s = getString()
    r = s[::-1]

    print('Yes' if s == r else 'No')


if __name__ == "__main__":
    main()
```
