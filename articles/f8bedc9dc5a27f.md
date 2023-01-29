---
title: "［AtCoder］ABC-110｜A - Maximize the Formula"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-110 A - Maximize the Formula](https://atcoder.jp/contests/abc110/tasks/abc110_a)

## 提出結果

```python
def getIntList():
    return list(map(int, input().split()))


def main():
    n = getIntList()

    n.sort()
    n[2] = n[2] * 10

    print(sum(n))


if __name__ == "__main__":
    main()
```
