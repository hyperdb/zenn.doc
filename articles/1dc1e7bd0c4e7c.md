---
title: "［AtCoder］ABC-427｜B - Sum of Digits Sequence"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["python", "AtCoder", "abc"]
published: true
---

## 設問ページ

- 🔗[ABC-427 B - Sum of Digits Sequence](https://atcoder.jp/contests/abc427/tasks/abc427_b)

## 提出結果

```python
def getInt():
    return int(input())


def colSum(N):
    return N if N < 10 else sum([int(i) for i in list(str(N))])


def main():
    N = getInt()
    A = [0] * (N + 1)

    A[0] = 1
    for i in range(1, N + 1):
        for j in range(i):
            A[i] += colSum(A[j])
    print(A[-1])


if __name__ == "__main__":
    main()
```
