---
title: "［AtCoder］ABC-406｜B - Product Calculator"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-406 B - Product Calculator](https://atcoder.jp/contests/abc406/tasks/abc406_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, K = getIntMap()
    A = getIntList()

    d = 1
    for i in range(N):
        d *= A[i]
        if d >= 10**K:
            d = 1
    print(d)


if __name__ == "__main__":
    main()
```
