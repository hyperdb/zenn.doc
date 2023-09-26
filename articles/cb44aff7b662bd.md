---
title: "［AtCoder］ABC-312｜A - Chord"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-312 A - Chord](https://atcoder.jp/contests/abc312/tasks/abc312_a )

## 提出結果

```python
def getString():
    return input()


def main():
    s = getString()

    print('Yes' if s in ['ACE', 'BDF', 'CEG', 'DFA', 'EGB', 'FAC', 'GBD'] else 'No')


if __name__ == "__main__":
    main()
```
