---
title: "［AtCoder］ABC-072｜ A Sandglass2"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-072 A - Sandglass2](https://atcoder.jp/contests/abc072/tasks/abc072_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    x, t = getIntMap()

    r = x - t
    print(r if r >= 0 else 0)


if __name__ == "__main__":
    main()
```
