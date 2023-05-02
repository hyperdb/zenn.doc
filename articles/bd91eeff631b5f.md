---
title: "［AtCoder］ABC-217｜A - Lexicographic Order"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-217 A - Lexicographic Order](https://atcoder.jp/contests/abc217/tasks/abc217_a)

## 提出結果

```python
def getStringList():
    return list(input().split())


def main():
    s = getStringList()
    t = sorted(s)

    print('Yes' if s[0] == t[0] else 'No')


if __name__ == "__main__":
    main()
```
