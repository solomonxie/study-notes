# Study Notes

These are my personal study notes from years ago (2015–2022ish), originally written
directly inside GitHub Issues on this repo — one issue per topic, one comment per note.

This version is a flat export of that content into plain markdown files, meant to be
dragged straight into Notion (or read as-is).

## Structure

- Each top-level folder is one topic (used to be one GitHub Issue)
- Each `.md` file inside is one note (used to be one comment on that issue)
- Files are named `<datetime>_<note title>.md`, timestamped to when the note was
  originally written
- Images referenced in notes are downloaded locally, next to the note, in a matching
  `<note title>_files/` folder
- `scripts/` holds the tooling used to do the export itself (not a notes topic)

## Notes on the notes

- Content quality varies a lot — some are polished, some are half-finished `[DRAFT]`
  scraps, some are just a dumped screenshot
- Topics span programming, math, Linux, networking, statistics, and random personal
  brain-dumps — no single theme
- A couple of very old embedded images (from since-shutdown services) are permanently
  broken and can't be recovered
- git commit dates on these files match the note's real original timestamp, not when
  this export happened — so `git log` reflects the actual note-taking history

## Topics

A quick summary of what's in each folder, note counts in parentheses.

### Programming & Dev Tools

## Python学习笔记 (133 notes)
General-purpose Python practice notes: language quirks and idioms, package
installation gotchas (esp. on Windows), function/type introspection, sorting,
compiling to `.pyc`, unit-test project structure, pip version lookups, set
operations, and more — a running scrapbook of "how do I do X in Python."

## C语言学习笔记 (10 notes)
C fundamentals: data types, pointers, operators, dynamic memory management,
file I/O, a primer on binaries, and using `gdb` on Mac.

## Javascript Everywhere (2 notes)
Early `[DRAFT]` quick-start notes on JavaScript language basics and Node.js.

## Git 学习笔记 (43 notes)
Practical Git troubleshooting and concepts — branches, `checkout`, references,
renaming folders, garbled unicode output, "unprotected private key" push
errors, and conflicts with Python virtualenvs.

## Vim 学习笔记 (77 notes)
The most extensive editor topic: Vim/Neovim configuration and workflow,
`coc.nvim` completion, cursor-lag fixes, persistent edit history, movement
commands, and building Vim with Lua/Python support on Mac.

## IDE 日常操作 (31 notes)
Day-to-day editor/IDE configuration tips across Sublime Text, VS Code, and
Jupyter Notebook (plotting, keybindings, one-shot virtualenv setup).

## API 操作实践 (21 notes)
Hands-on API work: Baidu Translate API, GitHub API pagination and rate
limits, Postman variables, parsing XML in Python, Boto3 against Tencent
Cloud COS (S3-compatible), Swagger mock servers, and a Zhihu scraper.

### Computer Science Fundamentals

## 算法学习笔记 (26 notes)
Core data structures and algorithm theory: arrays/lists, linked lists, hash
tables, maps, abstract data types (ADTs), and how to measure algorithmic
efficiency.

## Data Structure & Algorithms (DSA) (1 note)
A newer, smaller restart of algorithms study, currently just covering Big O
notation.

### Math, Statistics & Machine Learning

## Kindergarten Maths (95 notes)
Despite the tongue-in-cheek name, this covers real pre-calculus/algebra/trig
groundwork: factoring, systems of equations, trig function signs, inverse
functions, parallel/perpendicular line equations, and permutations &
combinations.

## Calculus Basics (96 notes)
Single-variable calculus: limits and continuity, series and convergence
tests, critical points, optimization, and error estimation for alternating
series.

## Linear Algebra Basics (15 notes)
Core linear algebra building blocks: vectors and vector span, matrix
multiplication, inverse matrices, and cross products.

## Linear Algebra Lecture Notes (21 notes)
Lecture-driven linear algebra following MIT OCW 18.06 and "Mathematics for
Machine Learning" — eigenvalues/eigenvectors, orthogonal matrices, and
intuitive ways to think about vectors, matrices, and tensors.

## Statistical Guessing (98 notes)
Introductory statistics and probability: z-scores, density curves, the
Central Limit Theorem, the Law of Large Numbers, Bernoulli distribution,
chi-squared homogeneity tests, central tendency, and significance testing.

## Machine Learning Notes (36 notes)
Classic ML concepts: cross-validation, partial dependence plots, stochastic
gradient descent, what a data scientist does, and a survey of ML task
categories.

## LLM from Scratch (2 notes)
Recently started notes on large language models — what "temperature" means
and a timeline of AI breakthroughs.

## TL;DR. Archive Link 疑惑调研杂项长文汇总 (6 notes)
Curated long-read links and mini research write-ups on assorted questions,
mostly centered on why/how to learn linear algebra, plus MIT OCW course
resources.

### Systems, Networking & Hardware

## Linux 学习笔记 (14 notes)
Bash scripting fundamentals: variables, numeric operations, checking the
current user's identity, stdout/stderr redirection, `xargs`/pipes, epoll
from an HTTP server's perspective, and GNU Autotools.

## Linux 日常维护 (106 notes)
The largest sysadmin topic: day-to-day Linux maintenance — disk usage,
`fstab`/mounting external drives, Homebrew mirror config, CPU temperature,
user management, turning scripts into boot-time services, tmux pane titles,
and terminal recording with `asciinema`.

## OS 操作系统学习笔记 (58 notes)
Desktop OS troubleshooting across Mac/Windows/Linux: Xcode upgrades, Chrome
scrollbar bugs, dual-booting Windows+Linux, Parallels Desktop VMs,
AppleScript from the terminal, and setting custom app icons.

## Network 学习笔记 (93 notes)
Networking fundamentals and ops: setting up Shadowsocks, whether a socket is
a file, Google BBR TCP congestion control, diagnosing connectivity issues,
WebDAV servers, and listing clients connected to the local machine.

## 树莓派及硬件 (41 notes)
Raspberry Pi setup and troubleshooting (Wi-Fi config, missing `ifconfig`,
Ruby/Jekyll install failures, CPU temperature), plus shopping for a 24/7
home server box and reflashing a bricked streaming device.

## Electronic Basics (3 notes)
Recently started notes on electronics fundamentals: transistors and how a
battery works.

### Web, Cloud & Ops

## Web App 学习笔记 (47 notes)
Building and running web apps/servers: Nginx + Keepalived for high
availability, Apache reload failures, Jekyll static sites and GitHub Pages
deployment, ownCloud over HTTPS, rendering math in Markdown, and
browser-specific quirks.

## Cloud 开发笔记 (44 notes)
Cloud server administration: trying out AWS Lightsail (Windows), remote
desktop/VNC access, deploying Shadowsocks, and using Tencent Cloud's
S3-compatible COS object storage.

## Ops 运维笔记 (24 notes)
Docker- and DevOps-flavored ops notes: memory leaks in Docker Desktop,
Portainer as a Docker GUI, containers that exit immediately, Chinese
registry mirrors, cleaning up dangling images, and "what actually is
DevOps."

## Serverless Everywhere (9 notes)
A more structured survey of serverless architecture: overall pros/cons,
industry case studies, API design, CI/CD, cost estimation, task queue
design, and getting started with the AWS SAM CLI.

## DB 数据库基础 (40 notes)
Database fundamentals spanning relational and NoSQL: MySQL clients, MongoDB
advanced queries, SQLAlchemy `GROUP BY`, JSON Schema, the case against
foreign keys, URIs in database design, and database vs. data warehouse.

### Personal, Essays & Life

## Essays & Tweets Archives 随笔随记备录 (119 notes)
A large personal archive of short Chinese-language essays, reflections, and
one-off thoughts on life, learning, dreams, and society — a running journal
more than a study topic.

## Tweets 微博 (64 notes)
Short microblog-style posts and one-liners — observations, humor, and the
occasional rant — in the same spirit as the essays archive but shorter.

## BRAIN STORMS (180 notes)
The single largest topic in the repo: freeform idea dumps tagged by type
(Project / Book / Game / Method / Writing / Experiment) — side-project
concepts, book ideas, small experiments, and tooling ideas.

## Bible Study Notes (8 notes)
Verse-by-verse study working through early Genesis — creation, the Fall,
Cain's lineage, and the Flood — plus general reading notes and questions.

## Bible Questions in Short Answer (5 notes)
Short Q&A-style notes tackling specific theological questions (salvation,
higher dimensions, lifespan limits, etc.) with online resources for
reference.

## English With Solomon (2 notes)
Personal English-learning notes, e.g. plural possessive nouns.

## Wiki-Nerds 理论研究 (7 notes)
A grab-bag of interesting concepts researched Wikipedia-style: the
forgetting curve, software licensing, baseball terms, shopping across
different App Store/PayPal regions, and stomach ulcer treatment.

## Filming & Media Editing 多媒体编辑及摄影相关 (3 notes)
Notes on projecting/mirroring between devices (e.g. iPhone to Mac) and
related media-editing topics.

## Australia Work & Holiday Visa #462 澳洲打工度假情报收集汇总 (1 note)
A single consolidated note collecting intel on Australia's Working Holiday
visa: living, work, and travel information.

## Ebbinghaus' Forgetting Curve 艾宾浩斯遗忘曲线 (1 note)
One idea note: using the forgetting curve to schedule spaced-repetition
review emails as a personal reminder tool.

## TECH STACK 技术栈大览 (1 note)
A personal tech-stack inventory — the apps, CLIs, and pip packages used
day-to-day on Mac, Ubuntu, and in-container.

## 《探讨开源思想与应用》2009 (2 notes)
An old 2009-era essay draft exploring open-source philosophy and its
applications, backed up here for posterity.

## 留白 (4 notes)
Literally "leaving blank" — placeholder entries with little to no content,
a catch-all for unstarted ideas.

### GitHub-Issues Meta / Testing

These topics predate the "real" notes and were just experiments in using
GitHub Issues as a blogging platform — kept for historical completeness.

## First Issue Blog Test~~~~ (4 notes)
Earliest test issue for trying out GitHub-Issues-as-blog features, including
uploading PDF and docx files.

## issue uploading test (2 notes)
Testing file/attachment uploads via GitHub Issues.

## Test close issue (5 notes)
Testing GitHub Issues behavior around closing, locking, and reopening —
whether commenting still works afterward.

## test convert issue to pull request (5 notes)
Exploring whether/how a GitHub Issue can be converted into a pull request.

## 用issues做博客合不合适呢？ (1 note)
A meta reflection on whether using GitHub Issues as a blogging platform was
actually a good idea in the first place.
