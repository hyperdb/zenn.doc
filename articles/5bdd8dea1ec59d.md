---
title: "［AtCoder］ABC-116｜A - Right Triangle"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-116 A - Right Triangle](https://atcoder.jp/contests/abc116/tasks/abc116_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    print(a * b // 2)


if __name__ == "__main__":
    main()
```
