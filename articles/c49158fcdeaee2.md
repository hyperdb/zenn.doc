---
title: "［AtCoder］ABC-223｜A - Exact Price"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-223 A - Exact Price](https://atcoder.jp/contests/abc223/tasks/abc223_a)

## 提出結果

```python
def getInt():
    return int(input())


def main():
    x = getInt()

    print('No' if x == 0 or x % 100 > 0 else 'Yes')


if __name__ == "__main__":
    main()
```
