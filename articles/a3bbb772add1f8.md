---
title: "［AtCoder］ABC-295｜A - Probably English"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-295 A - Probably English](https://atcoder.jp/contests/abc295/tasks/abc295_a)

## 提出結果

```python
def getInt():
    return int(input())


def getStringList():
    return list(input().split())


def main():
    n = getInt()
    w = getStringList()
    d = ['and', 'not', 'that', 'the', 'you']

    w.sort()

    r = False
    for x in set(w):
        if x in d:
            r = True
            break

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
```
