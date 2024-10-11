---
title: "［AtCoder］ABC-372｜C - Count ABC Again"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-372 C - Count ABC Again](https://atcoder.jp/contests/abc372/tasks/abc372_c)

## 提出結果

```python
import re


def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    N, Q = getIntMap()
    S = [""] + list(getString())
    XC = getStringListRow(Q)

    # -> 初期の"ABC"を数える
    m = len(re.findall(r"ABC", "".join(S)))

    for X, C in XC:
        # -> 指定位置の前後２つまでを求める
        a = max(int(X) - 2, 1)
        b = min(int(X) + 2, len(S))

        t = "".join(S[a : b + 1])
        tm = 1 if "ABC" in t else 0

        # -> 指定位置を書き換えて同様に
        S[int(X)] = C

        u = "".join(S[a : b + 1])
        um = 1 if "ABC" in u else 0

        # -> 書き換えて変化があれば反映する
        m += 1 if tm < um else -1 if tm > um else 0

        print(m)


if __name__ == "__main__":
    main()
```
