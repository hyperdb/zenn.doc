---
title: "［AtCoder］ABC-139｜B - Power Socket"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-139 B - Power Socket](https://atcoder.jp/contests/abc139/tasks/abc139_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = 1
    i = 0
    while c < b:
        c += a - 1
        i += 1
    print(i)


if __name__ == "__main__":
    main()
```
