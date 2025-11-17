---
title: "［AtCoder］ABC-419｜A - AtCoder Language"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["python", "AtCoder", "abc"]
published: true
---

## 設問ページ

-   🔗[ABC-419 A - AtCoder Language](https://atcoder.jp/contests/abc419/tasks/abc419_a)

## 提出結果

```python
def getString():
    return input()


def main():
    S = getString()
    d = {"red": "SSS", "blue": "FFF", "green": "MMM"}

    print(d[S] if S in d else "Unknown")


if __name__ == "__main__":
    main()
```
