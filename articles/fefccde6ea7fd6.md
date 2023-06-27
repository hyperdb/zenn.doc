---
title: "［AtCoder］ABC-253｜B - Distance Between Tokens"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-253 B - Distance Between Tokens](https://atcoder.jp/contests/abc253/tasks/abc253_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input()) for _ in range(N)]


def main():
    h, w = getIntMap()
    s = getStringListRow(h)

    p = []
    for y in range(h):
        for x in range(w):
            if s[y][x] == 'o':
                p.append([y, x])

    print(abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]))


if __name__ == "__main__":
    main()
```
