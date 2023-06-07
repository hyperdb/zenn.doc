---
title: "［AtCoder］ABC-240｜A - Edge Checker"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-240 A - Edge Checker](https://atcoder.jp/contests/abc240/tasks/abc240_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())

def main():
    a, b = getIntMap()

    print('Yes' if abs(a - b) == 1 or abs(a % 10 - b % 10) == 1 else 'No')


if __name__ == "__main__":
    main()
```
