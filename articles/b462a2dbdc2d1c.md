---
title: "［AtCorder］ABC-042｜A 和風いろはちゃんイージー"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'atcorder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC042 A - 和風いろはちゃんイージー](https://atcoder.jp/contests/abc042/tasks/abc042_a)

## 提出結果

```python
def getIntList():
    return list(map(int, input().split()))


def main():
    d = getIntList()
    d.sort()

    print('YES' if d == [5, 5, 7] else 'NO')


if __name__ == "__main__":
    main()
 ```
