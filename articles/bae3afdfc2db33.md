---
title: "［AtCoder］ABC-343｜C - 343"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-343 C - 343](https://atcoder.jp/contests/abc343/tasks/abc343_c)

## 提出結果

```python
import math


def getInt():
    return int(input())


def main():
    n = getInt()

    # 三乗根を求めて誤差補正
    m = int(math.pow(n, 1/3)) + 1

    # m 以下を上からチェック
    for i in range(m):
        x = pow(m - i, 3)
        y = int(str(x)[::-1])

        if x <= n and x == y:
            print(x)
            break


if __name__ == "__main__":
    main()
```
