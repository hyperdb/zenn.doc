---
title: "［AtCoder］ABC-276｜B - Adjacency List"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-276 B - Adjacency List](https://atcoder.jp/contests/abc276/tasks/abc276_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    ab = getIntListRow(m)

    r = [[] for _ in range(n + 1)]

    for a, b in ab:
        r[a].append(b)
        r[b].append(a)

    for i in range(1, len(r)):
        r[i].sort()
        r[i] = [len(r[i])] + r[i]
        print(" ".join(list(map(str, r[i]))))


if __name__ == "__main__":
    main()
```
