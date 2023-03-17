---
title: "［AtCoder］ABC-170｜A - Five Variables"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-170 A - Five Variables](https://atcoder.jp/contests/abc170/tasks/abc170_a)

## 提出結果

```python
def getIntList():
    return list(map(int, input().split()))


def main():
    x = getIntList()

    print(x.index(0) + 1)


if __name__ == "__main__":
    main()
```
