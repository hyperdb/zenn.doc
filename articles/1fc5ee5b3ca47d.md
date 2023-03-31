---
title: "［AtCoder］ABC-187｜A - Large Digits"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-187 A - Large Digits](https://atcoder.jp/contests/abc187/tasks/abc187_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def s(x):
    return sum(map(int, list(str(x))))


def main():
    a, b = getIntMap()

    print(max(s(a), s(b)))


if __name__ == "__main__":
    main()
```
