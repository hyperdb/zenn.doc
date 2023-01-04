---
title: "［AtCoder］ABC-066｜B - ss"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-066 B - ss](https://atcoder.jp/contests/abc066/tasks/abc066_b)

## 提出結果

```python
def getString():
    return input()


def main():
    s = list(getString())

    for i in range(len(s) - 1):
        s.pop(-1)
        l = len(s)

        if l % 2 == 1:
            continue

        if s[:int(l / 2)] == s[int(l / 2) * -1:]:
            print(l)
            break


if __name__ == "__main__":
    main()
```
