---
title: "［AtCoder］ABC-389｜B - tcaF"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-389 B - tcaF](https://atcoder.jp/contests/abc389/tasks/abc389_b)

## 提出結果

```python
def getInt():
    return int(input())


def main():
    X = getInt()

    f = 1
    for i in range(2, X):
        f *= i
        if f == X:
            print(i)
            break


if __name__ == "__main__":
    main()
```
