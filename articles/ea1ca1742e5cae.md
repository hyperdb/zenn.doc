---
title: "［AtCoder］ABC-332｜B - Glass and Mug"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-332 B - Glass and Mug](https://atcoder.jp/contests/abc332/tasks/abc332_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    k, g, m = getIntMap()

    xg = 0
    xm = 0

    while k > 0:
        if xg == g:
            xg = 0
        elif xm == 0:
            xm = m
        else:
            mv = min(g - xg, xm)
            xg += mv
            xm -= mv
        k -= 1

    print("%d %d" % (xg, xm))


if __name__ == "__main__":
    main()
```
