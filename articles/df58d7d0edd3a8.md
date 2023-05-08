---
title: "［AtCoder］ABC-219｜B - Maritozzo"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-219 B - Maritozzo](https://atcoder.jp/contests/abc219/tasks/abc219_b)

## 提出結果

```python
def getStringRow(N):
    return [input() for _ in range(N)]


def getString():
    return input()


def main():
    s = getStringRow(3)
    t = map(int, list(getString()))
    u = []

    for i in t:
        u.append(s[i - 1])
    print("".join(u))


if __name__ == "__main__":
    main()
```
