---
title: "［AtCoder］ABC-311｜B - Vacation Together"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-311 B - Vacation Together](https://atcoder.jp/contests/abc311/tasks/abc311_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def main():
    n, d = getIntMap()
    s = getStringListRow(n)

    # x -> y transform
    t = []
    for i in range(d):
        w = []
        for v in s:
            w.append(v[i])
        t.append(w)

    # count
    c = 0
    r = 0
    for u in t:
        if 'x' in u:
            c = 0
        else:
            c += 1
        r = max(r, c)

    print(r)


if __name__ == "__main__":
    main()
```
