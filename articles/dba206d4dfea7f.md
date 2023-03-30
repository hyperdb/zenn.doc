---
title: "［AtCoder］ABC-186｜A - Brick"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-186 A - Brick](https://atcoder.jp/contests/abc186/tasks/abc186_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    n, w = getIntMap()

    print(n // w)


if __name__ == "__main__":
    main()
```
