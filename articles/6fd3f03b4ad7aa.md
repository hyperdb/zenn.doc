---
title: "［AtCoder］ABC-354｜B - AtCoder Janken 2"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-354 B - AtCoder Janken 2](https://atcoder.jp/contests/abc354/tasks/abc354_b)

## 提出結果

```python
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    n = getInt()
    sc = getStringListRow(n)

    t = 0
    m = []
    for s, c in sc:
        t += int(c)
        m.append(s)
    m.sort()
    print(m[t % n])


if __name__ == "__main__":
    main()
```
