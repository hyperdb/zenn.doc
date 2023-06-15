---
title: "［AtCoder］ABC-245｜B - Mex"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-245 B - Mex](https://atcoder.jp/contests/abc245/tasks/abc245_b)

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
    for i in range(0, 2000 + 1):
        if not i in a:
            print(i)
            break

if __name__ == "__main__":
    main()
```
