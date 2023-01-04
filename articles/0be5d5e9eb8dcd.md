---
title: "［AtCoder］ABC-049｜A - 居合を終え、青い絵を覆う"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-049 A - 居合を終え、青い絵を覆う](https://atcoder.jp/contests/abc049/tasks/abc049_a)

## 提出結果

```python
def getString():
    return input()


def main():
    c = getString()
    print('vowel' if c in ['a', 'i', 'u', 'e', 'o'] else 'consonant')


if __name__ == "__main__":
    main()
```
