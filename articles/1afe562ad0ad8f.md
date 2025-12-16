---
title: "［AtCoder］ABC-427｜A - ABC -> AC"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["python", "AtCoder", "abc"]
published: true
---

## 設問ページ

- 🔗[ABC-427 A - ABC -> AC](https://atcoder.jp/contests/abc427/tasks/abc427_a)

## 提出結果

```python
def getString():
    return input()


def main():
    S = getString()
    m = len(S) // 2

    print(S[:m] + S[m + 1 :])


if __name__ == "__main__":
    main()
```
