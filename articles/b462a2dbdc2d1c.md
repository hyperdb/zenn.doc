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

    if d == [5, 5, 7]:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
```

## ふりかえり

普段プログラムを書いている時は配列同志を比較するようなケースがなかったので、単純に比較演算子が使えるという事実を思い出した時に目から鱗が落ちる思いでした。
