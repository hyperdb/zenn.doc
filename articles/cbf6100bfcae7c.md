---
title: "［AtCoder］ABC-124｜A - Buttons"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-124 A - Buttons](https://atcoder.jp/contests/abc124/tasks/abc124_a)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(max([a + b, a * 2 -1, b * 2 - 1]))


if __name__ == "__main__":
    main()
```
