---
title: "［AtCoder］ABC-056｜A HonestOrDishonest"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-056 A - HonestOrDishonest](https://atcoder.jp/contests/abc056/tasks/abc056_a)

## 提出結果

```python
def getStringMap():
    return input().split()


def main():
    a, b = getStringMap()

    if a == 'H':
        print('H' if b == 'H' else 'D')
    else:
        print('D' if b == 'H' else 'H')


if __name__ == "__main__":
    main()
```
