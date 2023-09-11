---
title: "［AtCoder］ABC-302｜A - Attack"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-302 A - Attack](https://atcoder.jp/contests/abc302/tasks/abc302_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = a // b

    print(c if a % b == 0 else c + 1)


if __name__ == "__main__":
    main()
```
