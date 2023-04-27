---
title: "［AtCoder］ABC-214｜A - New Generation ABC"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-214 A - New Generation ABC](https://atcoder.jp/contests/abc214/tasks/abc214_a)

## 提出結果

```python
def getInt():
    return int(input())


def main():
    n = getInt()

    print(4 if n <= 125 else 6 if n <= 211 else 8)


if __name__ == "__main__":
    main()
```
