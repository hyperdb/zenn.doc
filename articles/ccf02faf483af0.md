---
title: "［AtCoder］ABC-103｜B - String Rotation"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-103 B - String Rotation](https://atcoder.jp/contests/abc103/tasks/abc103_b)

## 提出結果

```python
def getString():
    return input()


def main():
    s = getString()
    t = getString()

    r = 'No'
    for i in range(len(s)):
        if t == (s[i:] + s[:i]):
            r = 'Yes'
            break
    print(r)


if __name__ == "__main__":
    main()
```
