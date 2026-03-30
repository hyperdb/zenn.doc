---
title: "［AtCoder］ABC-449｜A - π"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-449 A - π](https://atcoder.jp/contests/abc449/tasks/abc449_a)

## 提出結果

```python
import math


def getInt():
    return int(input())


def main():
    D = getInt()
    # 半径✕半径✕円周率
    print((D / 2) ** 2 * math.pi)


if __name__ == "__main__":
    main()
```
