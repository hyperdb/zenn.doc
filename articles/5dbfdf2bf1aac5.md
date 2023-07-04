---
title: "［AtCoder］ABC-258｜A - When?"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-258 A - When?](https://atcoder.jp/contests/abc258/tasks/abc258_a)

## 提出結果

```python
def getInt():
    return int(input())


def main():
    n = getInt()

    m = n % 60
    h = 21 + n // 60

    print('%02d:%02d' % (h, m))


if __name__ == "__main__":
    main()
```
