---
title: "［AtCoder］ABC-285｜A - Edge Checker 2"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-285 A - Edge Checker 2](https://atcoder.jp/contests/abc285/tasks/abc285_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Yes' if b // 2 == a else 'No')


if __name__ == "__main__":
    main()
```
