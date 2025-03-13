---
title: "［AtCoder］ABC-395｜A - Strictly Increasing?"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-395 A - Strictly Increasing?](https://atcoder.jp/contests/abc395/tasks/abc395_a)

## 提出結果

```python
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    B = [A[i] - A[i - 1] for i in range(1, N)]

    print("Yes" if min(B) > 0 else "No")


if __name__ == "__main__":
    main()
```
