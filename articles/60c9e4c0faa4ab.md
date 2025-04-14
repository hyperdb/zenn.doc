---
title: "［AtCoder］ABC-400 ｜A - ABC400 Party"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-400 A - ABC400 Party](https://atcoder.jp/contests/abc400/tasks/abc400_a)

## 提出結果

```python
def getInt():
    return int(input())


def main():
    A = getInt()

    d, m = divmod(400, A)

    print(d if m == 0 else -1)


if __name__ == "__main__":
    main()
```
