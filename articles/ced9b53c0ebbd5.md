---
title: "［AtCorder］ABC-064｜B Traveling AtCoDeer Problem"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'atcorder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-064 B - Traveling AtCoDeer Problem](https://atcoder.jp/contests/abc064/tasks/abc064_b)

## 提出結果

```python
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    a.sort()

    print(a[n - 1] - a[0])


if __name__ == "__main__":
    main()
```
