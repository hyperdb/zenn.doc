---
title: "［AtCoder］ABC-324｜A - Same"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-324 A - Same](https://atcoder.jp/contests/abc324/tasks/abc324_a)

## 提出結果

```python
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    print('Yes' if len(set(a)) == 1 else 'No')


if __name__ == "__main__":
    main()
```
