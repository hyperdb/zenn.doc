---
title: "［AtCoder］ABC-238｜B - Pizza"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-238 B - Pizza](https://atcoder.jp/contests/abc238/tasks/abc238_b)

## 提出結果

```python
def getInt():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    n = getInt()
    a = [0] + getIntList()
    b = [0, 360]

    p = 0
    for i in range(1, n + 1):
        p -= a[i]
        if p < 0:
            p += 360
        b.append(p)

    b.sort()
    c = [b[i] - b[i - 1] for i in range(1, len(b))]

    print(max(c))

if __name__ == "__main__":
    main()
```
