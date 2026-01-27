---
title: "［AtCoder］ABC-067｜C - Splitting Pile"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-067 C - Splitting Pile](https://atcoder.jp/contests/abc067/tasks/arc078_a)

## 提出結果

```python
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()

    sum_left = 0
    sum_right = sum(a)

    diff = -1

    for i in range(N - 1):
        # 左側に要素を1つ追加
        sum_left += a[i]
        # 右側から要素を1つ削除
        sum_right -= a[i]
        # 初回は差分を設定、以降は最小値を更新
        diff = abs(sum_left - sum_right) if diff == -1 else min(diff, abs(sum_left - sum_right))

    print(diff)


if __name__ == "__main__":
    main()
```
