---
title: "［AtCoder］ABC-071｜A - Meal Delivery"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-071 A - Meal Delivery](https://atcoder.jp/contests/abc071/tasks/abc071_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    x, a, b = getIntMap()
    print('A' if abs(a - x) <= abs(b - x) else 'B')


if __name__ == "__main__":
    main()
```
