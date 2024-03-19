---
title: "［AtCoder］ABC-340｜B - Append"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-340 B - Append](https://atcoder.jp/contests/abc340/tasks/abc340_b)

## 提出結果

```python
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    q = getIntListRow(n)

    buf = []

    for i, j in q:
        if i == 1:
            buf.append(j)
        else:
            print(buf[j * -1])


if __name__ == "__main__":
    main()
```
