---
title: "［AtCoder］ABC-057｜A Remaining Time"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-057 A - Remaining Time](https://atcoder.jp/contests/abc057/tasks/abc057_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print((a + b) % 24)


if __name__ == "__main__":
    main()
```
