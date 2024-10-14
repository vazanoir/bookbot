# bookbot

First project from [boot.dev](https://www.boot.dev/courses/build-bookbot). It was meant to teach how to create a simple CLI tool while using dev tools, and showing a simple workflow.

Give it a book (raw text only) like [this one](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt) as an argument, and it will get the word count and the count of every letters.

Example:
```
git clone https://github.com/vazanoir/bookbot
cd bookbot
mkdir books
curl https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt -o books/frankenstein.txt
python main.py books/frankenstein.txt
```

Output:
```
╺ books/frankenstein.txt ╸
┌───────┬─────────────────┐
│ words │           77986 │
└───────┴─────────────────┘
┌───────────┬─────────────┐
│ character │ occurrences │
├───────────┼─────────────┤
│         e │       46043 │
│         t │       30365 │
│         a │       26743 │
│         o │       25225 │
│         i │       24613 │
│         n │       24367 │
│         s │       21155 │
│         r │       20818 │
│         h │       19725 │
│         d │       16863 │
│         l │       12739 │
│         m │       10604 │
│         u │       10407 │
│         c │        9243 │
│         f │        8731 │
│         y │        7914 │
│         w │        7638 │
│         p │        6121 │
│         g │        5974 │
│         b │        5026 │
│         v │        3833 │
│         k │        1755 │
│         x │         677 │
│         j │         504 │
│         q │         324 │
│         z │         243 │
└───────────┴─────────────┘

```
