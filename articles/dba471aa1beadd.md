---
title: "［AtCoder］ABC-082｜C - Good Sequence"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-082 C - Good Sequence](https://atcoder.jp/contests/abc082/tasks/arc087_a)

## 提出結果

```python
import collections


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()

    # 種類別にカウント
    c = collections.Counter(a)

    result = 0
    # 各種類についてチェック
    for k, v in c.items():
        # 種類と個数が同じ場合は良い数列なので何もしない
        if k == v:
            continue
        # キーより個数が多い場合は、キーに合わせて削除
        elif k < v:
            result += v - k
        # それ以外はキーごと削除
        else:
            result += v

    print(result)


if __name__ == "__main__":
    main()
```
