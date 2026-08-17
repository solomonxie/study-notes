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
General-purpose Python practice notes — a running scrapbook of "how do I do X in Python."
- Language quirks and idioms, function/type introspection, sorting
- Package installation gotchas, especially on Windows
- Compiling to `.pyc`, unit-test project structure, pip version lookups, set operations

## C语言学习笔记 (10 notes)
C fundamentals.
- Data types, pointers, operators
- Dynamic memory management, file I/O
- A primer on binaries, and using `gdb` on Mac

## Git 学习笔记 (43 notes)
Practical Git troubleshooting and concepts.
- Branches, `checkout`, references, renaming folders
- Garbled unicode output
- "Unprotected private key" push errors, and conflicts with Python virtualenvs

## Vim 学习笔记 (77 notes)
The most extensive editor topic.
- Vim/Neovim configuration and workflow, `coc.nvim` completion
- Cursor-lag fixes, persistent edit history, movement commands
- Building Vim with Lua/Python support on Mac

## IDE 日常操作 (31 notes)
Day-to-day editor/IDE configuration tips.
- Sublime Text and VS Code setup
- Jupyter Notebook — plotting, keybindings, one-shot virtualenv setup

## API 操作实践 (21 notes)
Hands-on API work.
- Baidu Translate API, GitHub API pagination and rate limits, Postman variables
- Parsing XML in Python, Boto3 against Tencent Cloud COS (S3-compatible)
- Swagger mock servers, and a Zhihu scraper

### Computer Science Fundamentals

## 算法学习笔记 (26 notes)
Core data structures and algorithm theory.
- Arrays/lists, linked lists, hash tables, maps
- Abstract data types (ADTs)
- How to measure algorithmic efficiency

### Math, Statistics & Machine Learning

## Kindergarten Maths (95 notes)
Despite the tongue-in-cheek name, this covers real pre-calculus/algebra/trig groundwork.
- Factoring, systems of equations, trig function signs
- Inverse functions, parallel/perpendicular line equations
- Permutations & combinations

## Calculus Basics (96 notes)
Single-variable calculus.
- Limits and continuity, series and convergence tests
- Critical points, optimization
- Error estimation for alternating series

## Linear Algebra Basics (15 notes)
Core linear algebra building blocks.
- Vectors and vector span
- Matrix multiplication, inverse matrices
- Cross products

## Linear Algebra Lecture Notes (21 notes)
Lecture-driven linear algebra following MIT OCW 18.06 and "Mathematics for Machine Learning."
- Eigenvalues/eigenvectors, orthogonal matrices
- Intuitive ways to think about vectors, matrices, and tensors

## Statistical Guessing (98 notes)
Introductory statistics and probability.
- Z-scores, density curves, central tendency
- The Central Limit Theorem, the Law of Large Numbers, Bernoulli distribution
- Chi-squared homogeneity tests, significance testing

## Machine Learning Notes (36 notes)
Classic ML concepts.
- Cross-validation, partial dependence plots, stochastic gradient descent
- What a data scientist does
- A survey of ML task categories

## TL;DR. Archive Link 疑惑调研杂项长文汇总 (6 notes)
Curated long-read links and mini research write-ups on assorted questions.
- Mostly centered on why/how to learn linear algebra
- Plus MIT OCW course resources

### Systems, Networking & Hardware

## Linux 学习笔记 (14 notes)
Bash scripting fundamentals.
- Variables, numeric operations, checking the current user's identity
- Stdout/stderr redirection, `xargs`/pipes
- Epoll from an HTTP server's perspective, and GNU Autotools

## Linux 日常维护 (106 notes)
The largest sysadmin topic — day-to-day Linux maintenance.
- Disk usage, `fstab`/mounting external drives, Homebrew mirror config
- CPU temperature, user management
- Turning scripts into boot-time services, tmux pane titles, terminal recording with `asciinema`

## OS 操作系统学习笔记 (58 notes)
Desktop OS troubleshooting across Mac/Windows/Linux.
- Xcode upgrades, Chrome scrollbar bugs
- Dual-booting Windows+Linux, Parallels Desktop VMs
- AppleScript from the terminal, setting custom app icons

## Network 学习笔记 (93 notes)
Networking fundamentals and ops.
- Setting up Shadowsocks, whether a socket is a file
- Google BBR TCP congestion control, diagnosing connectivity issues
- WebDAV servers, listing clients connected to the local machine

## 树莓派及硬件 (41 notes)
Raspberry Pi setup and troubleshooting.
- Wi-Fi config, missing `ifconfig`, Ruby/Jekyll install failures, CPU temperature
- Shopping for a 24/7 home server box
- Reflashing a bricked streaming device

## Electronic Basics (3 notes)
Recently started notes on electronics fundamentals.
- Transistors
- How a battery works

### Web, Cloud & Ops

## Web App 学习笔记 (47 notes)
Building and running web apps/servers.
- Nginx + Keepalived for high availability, Apache reload failures
- Jekyll static sites and GitHub Pages deployment
- ownCloud over HTTPS, rendering math in Markdown, browser-specific quirks

## Cloud 开发笔记 (44 notes)
Cloud server administration.
- Trying out AWS Lightsail (Windows), remote desktop/VNC access
- Deploying Shadowsocks
- Using Tencent Cloud's S3-compatible COS object storage

## Ops 运维笔记 (24 notes)
Docker- and DevOps-flavored ops notes.
- Memory leaks in Docker Desktop, Portainer as a Docker GUI
- Containers that exit immediately, cleaning up dangling images
- Chinese registry mirrors, and "what actually is DevOps"

## Serverless Everywhere (9 notes)
A more structured survey of serverless architecture.
- Overall pros/cons, industry case studies, API design
- CI/CD, cost estimation, task queue design
- Getting started with the AWS SAM CLI

## DB 数据库基础 (40 notes)
Database fundamentals spanning relational and NoSQL.
- MySQL clients, MongoDB advanced queries, SQLAlchemy `GROUP BY`
- JSON Schema, the case against foreign keys
- URIs in database design, database vs. data warehouse

### Personal, Essays & Life

## Essays & Tweets Archives 随笔随记备录 (119 notes)
A large personal archive of short Chinese-language essays and reflections — a running journal more than a study topic.
- One-off thoughts on life, learning, dreams, and society

## Tweets 微博 (64 notes)
Short microblog-style posts and one-liners, in the same spirit as the essays archive but shorter.
- Observations, humor, and the occasional rant

## BRAIN STORMS (180 notes)
The single largest topic in the repo — freeform idea dumps tagged by type.
- Project / Book / Game / Method / Writing / Experiment
- Side-project concepts, book ideas, small experiments, tooling ideas

## Bible Study Notes (8 notes)
Verse-by-verse study working through early Genesis.
- Creation, the Fall, Cain's lineage, and the Flood
- General reading notes and questions

## Bible Questions in Short Answer (5 notes)
Short Q&A-style notes tackling specific theological questions.
- Salvation, higher dimensions, lifespan limits, etc.
- With online resources for reference

## Wiki-Nerds 理论研究 (7 notes)
A grab-bag of interesting concepts researched Wikipedia-style.
- The forgetting curve, software licensing, baseball terms
- Shopping across different App Store/PayPal regions, stomach ulcer treatment

## Filming & Media Editing 多媒体编辑及摄影相关 (3 notes)
Notes on projecting/mirroring between devices.
- e.g. iPhone to Mac
- Related media-editing topics

## 留白 (4 notes)
Literally "leaving blank."
- Placeholder entries with little to no content, a catch-all for unstarted ideas

### GitHub-Issues Meta / Testing

These topics predate the "real" notes and were just experiments in using
GitHub Issues as a blogging platform — kept for historical completeness.

## First Issue Blog Test~~~~ (4 notes)
Earliest test issue for trying out GitHub-Issues-as-blog features.
- Including uploading PDF and docx files

## Test close issue (5 notes)
Testing GitHub Issues behavior around closing, locking, and reopening.
- Whether commenting still works afterward

## test convert issue to pull request (5 notes)
Exploring whether/how a GitHub Issue can be converted into a pull request.
