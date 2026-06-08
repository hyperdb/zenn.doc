---
title: "［AtCoder］ABC-459｜A - Hell, World!"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-459 A - Hell, World!](https://atcoder.jp/contests/abc459/tasks/abc459_a)

## 提出結果

```python
def getInt():
    return int(input())


def main():
    N = getInt()
    S = "HelloWorld"

    # 起点は0
    print(S[: N - 1] + S[N:])


if __name__ == "__main__":
    main()
```
