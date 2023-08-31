---
title: "［AtCoder］ABC-296｜A - Alternately"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-296 A - Alternately](https://atcoder.jp/contests/abc296/tasks/abc296_a)

## 提出結果

```python
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    print('Yes' if s.find('MM') == -1 and s.find('FF') == -1 else 'No')


if __name__ == "__main__":
    main()
```
