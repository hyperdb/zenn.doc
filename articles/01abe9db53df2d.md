---
title: "［AtCoder］ABC-351｜B - Spot the Difference"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-351 B - Spot the Difference](https://atcoder.jp/contests/abc351/tasks/abc351_b)

## 提出結果

```python
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    n = getInt()
    a = getStringRow(n)
    b = getStringRow(n)

    for i in range(n):
        if a[i] == b[i]:
            continue
        else:
            for j in range(n):
                if a[i][j] == b[i][j]:
                    continue
                else:
                    print(i + 1, j + 1)
                    break
            break


if __name__ == "__main__":
    main()
```
