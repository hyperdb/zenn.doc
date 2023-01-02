---
title: "［AtCoder］ABC-072｜ B OddString"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-072 B - OddString](https://atcoder.jp/contests/abc072/tasks/abc072_b)

## 提出結果

```python
def getString():
    return input()


def main():
    s = list(getString())

    r = ''
    for i in range(len(s)):
        if i % 2 == 0:
            r += s[i]
    print(r)


if __name__ == "__main__":
    main()
```
