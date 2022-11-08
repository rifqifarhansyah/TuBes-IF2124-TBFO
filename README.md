# TuBes-IF2124-TBFO
<h2 align="center">
  🐍 JavaScript Compiler with Python 🐍<br/>
</h2>
<hr>

<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/Line-00C300?style=for-the-badge&logo=line&logoColor=white">
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
</p>

## Table of Contents
1. [General Info](#general-information)
2. [Member List](#member-list)
3. [Features](#features)
4. [Structure](#structure)
5. [Contact](#contact)

<a name="general-information"></a>

## General Information
Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat dieksekusi oleh mesin, terdapat `pemeriksaan sintaks bahasa atau parsing yang dibuat oleh programmer untuk memastikan program dapat dieksekusi tanpa menghasilkan error`. Parsing ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai dilakukan.
Dibutuhkan grammar bahasa dan algoritma parser untuk melakukan parsing. Sudah sangat banyak grammar dan algoritma yang dikembangkan untuk menghasilkan compiler dengan performa yang tinggi. Terdapat `CFG, CNF-e, CNF+e, 2NF, 2LF, dll` untuk grammar yang dapat digunakan, dan terdapat `LL(0), LL(1), CYK, Earley’s Algorithm, LALR, GLR, Shift-reduce, SLR, LR(1), dll` untuk algoritma yang dapat digunakan untuk melakukan parsing.

<a name="member-list"></a>

## Member List

| Nama                    | NIM      |
| ----------------------- | -------- |
| M. Abdul Aziz Ghazali   | 13521128 |
| M. Zaki Amanullah       | 13521146 |
| M. Rifqi Farhansyah     | 13521166 |

## Features

Pada tugas besar ini, telah diimplementasikan `parser JavaScript (Node.js)` untuk beberapa statement dan sintaks bawaan JavaScript. Konsep `CFG (Context Free Grammar)` digunakan untuk pengerjaan parser yang mengevaluasi syntax program. Sementara itu, nama variabel dan operasi (+, -, >, dll) dalam program, akan dievalusi menggunakan `FA (Finite Automata)`.

<a name="structure"></a>

## Structure
```
│   parser_main.py
│   README.md
│
├───fileProcessing
│       file.txt
│       file_processing.py
│
└───grammar
        grammar.txt
        grammar_convert.py
        grammar_parser.py
        grammar_processing.py
```

## Contact
<h4 align="center">
  Created by JawaScript<br/>
  2022
</h4>
<hr>