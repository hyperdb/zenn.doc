---
title: "［AtCoder］ABC-237｜B - Matrix Transposition"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-237 B - Matrix Transposition](https://atcoder.jp/contests/abc237/tasks/abc237_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]

def main():
    h, w = getIntMap()
    a = getIntListRow(h)

    for x in range(w):
        print(' '.join([str(a[y][x]) for y in range(h)]))

if __name__ == "__main__":
    main()
```
