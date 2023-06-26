---
title: "［AtCoder］ABC-252｜B - Takahashi's Failure"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-252 B - Takahashi's Failure](https://atcoder.jp/contests/abc252/tasks/abc252_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    a = getIntList()
    b = getIntList()
    c = [i + 1 for i in range(n) if max(a) == a[i]]

    r = False
    for i in c:
        if i in b:
            r = True
            break

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
```
