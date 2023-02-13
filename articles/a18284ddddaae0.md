---
title: "［AtCoder］ABC-127｜B - Algae"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-127 B - Algae](https://atcoder.jp/contests/abc127/tasks/abc127_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def weight(r, d, x):
    return r * x - d


def main():
    r, d, x = getIntMap()

    for i in range(10):
        x = weight(r, d, x)
        print(x)


if __name__ == "__main__":
    main()
```
