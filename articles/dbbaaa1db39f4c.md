---
title: "［AtCoder］ABC-317｜B - MissingNo."
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-317 B - MissingNo.](https://atcoder.jp/contests/abc317/tasks/abc317_b)

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

    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            continue
        print(a[i] + 1)
        break

if __name__ == "__main__":
    main()
```
