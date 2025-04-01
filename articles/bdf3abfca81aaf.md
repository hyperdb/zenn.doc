---
title: "［AtCoder］ABC-396｜B - Card Pile"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-396 B - Card Pile](https://atcoder.jp/contests/abc396/tasks/abc396_b)

## 提出結果

```python
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    A = getStringRow(N)

    C = [0 for _ in range(100)]

    for i in range(N):
        if A[i][0] == "2":
            print(C.pop())
        else:
            _, n = map(int, A[i].split(" "))
            C += [n]


if __name__ == "__main__":
    main()
```
