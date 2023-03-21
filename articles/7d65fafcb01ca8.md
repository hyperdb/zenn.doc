---
title: "［AtCoder］ABC-177｜A - Don't be late"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-177 A - Don't be late](https://atcoder.jp/contests/abc177/tasks/abc177_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    d, t, s = getIntMap()

    print('Yes' if d / s <= t else 'No')


if __name__ == "__main__":
    main()
```
