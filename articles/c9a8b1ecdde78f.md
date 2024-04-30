---
title: "［AtCoder］ABC-349｜C - Airport Code"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-349 C - Airport Code](https://atcoder.jp/contests/abc349/tasks/abc349_c)

## 提出結果

```python
def getString():
    return input()


def main():
    s = getString()
    t = getString().lower()

    i = 0
    p = []
    for c in t:
        x = s[i:].find(c)
        if x >= 0:
            p.append(i + x)
            i += (x + 1)
        else:
            p.append(x)

    a, b, c = p

    r = False
    if a >= 0 and b >= 0 and a < b:
        if t[-1] == 'x':
            r = True
        elif c >= 0 and b < c:
            r = True

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
```
