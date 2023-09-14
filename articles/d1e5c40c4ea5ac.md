---
title: "［AtCoder］ABC-305｜B - ABCDEFG"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-305 B - ABCDEFG](https://atcoder.jp/contests/abc305/tasks/abc305_b)

## 提出結果

```python
def getStringMap():
    return input().split()


def main():
    p, q = getStringMap()
    d = [3, 1, 4, 1, 5, 9]
    s = ord(p) - ord('A')
    e = ord(q) - ord('A')

    print(abs(sum(d[:s]) - sum(d[:e])))


if __name__ == "__main__":
    main()
```
