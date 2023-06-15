---
title: "［AtCoder］ABC-245｜A - Good morning"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-245 A - Good morning](https://atcoder.jp/contests/abc245/tasks/abc245_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())

def m(x, y):
    return x * 60 + y

def main():
    a, b, c, d = getIntMap()

    print('Takahashi' if m(a, b) <= m(c, d) else 'Aoki')

if __name__ == "__main__":
    main()
```
