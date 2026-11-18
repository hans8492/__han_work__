# Git 常用指令與語法速查表 (Git Cheat Sheet)

本文件整理了在開發與日常協作中最常使用的 Git 指令，適合課堂練習、個人開發與團隊協作時查閱。

---

## 目錄
1. [初次設定（Config）](#1-初次設定config)
2. [建立與取得儲存庫（Init & Clone）](#2-建立與取得儲存庫init--clone)
3. [日常核心工作流（Status, Add, Commit）](#3-日常核心工作流status-add-commit)
4. [比對差異（Diff）](#4-比對差異diff)
5. [檢視歷史紀錄（Log）](#5-檢視歷史紀錄log)
6. [分支管理（Branch & Switch）](#6-分支管理branch--switch)
7. [遠端協作與同步（Remote, Push, Pull）](#7-遠端協作與同步remote-push-pull)
8. [暫存工作進度（Stash）](#8-暫存工作進度stash)
9. [復原與撤銷（Restore, Reset, Revert）](#9-復原與撤銷restore-reset-revert)
10. [常用忽略設定（.gitignore）與注意事項](#10-常用忽略設定gitignore與注意事項)

---

## 1. 初次設定（Config）

在剛安裝好 Git 或換新電腦時，需先設定個人識別資料：

```bash
# 設定使用者名稱
git config --global user.name "你的名字或 GitHub 帳號"

# 設定使用者 Email
git config --global user.email "your_email@example.com"

# 檢視目前的所有設定
git config --list

# 檢視特定設定項
git config user.name
```

---

## 2. 建立與取得儲存庫（Init & Clone）

```bash
# 在目前資料夾初始化一個全新的本地 Git 儲存庫
git init

# 從遠端（如 GitHub）下載複製現有的儲存庫到本地
git clone <儲存庫網址>

# 複製並指定本機資料夾名稱
git clone <儲存庫網址> my_project
```

---

## 3. 日常核心工作流（Status, Add, Commit）

這是每次撰寫程式碼時最頻繁使用的「三部曲」：

```bash
# 1. 檢查工作區狀態（哪些檔案被修改、暫存或未追蹤）
git status

# 2. 將修改加入暫存區（Staging Area）
git add <檔案名稱>       # 加入特定檔案
git add 2026_11_18/     # 加入特定資料夾
git add .               # 加入當前目錄下的所有變更

# 3. 提交變更到本地儲存庫並附上說明訊息
git commit -m "更新說明訊息"

# 一步完成「已追蹤檔案的加入暫存與提交」（不包含全新未追蹤的檔案）
git commit -am "更新說明訊息"
```

---

## 4. 比對差異（Diff）

在 commit 前檢查具體修改了哪些程式碼行數：

```bash
# 比對工作區 vs 暫存區（尚未 git add 的修改）
git diff

# 比對暫存區 vs 最新 commit（已 git add 準備要 commit 的修改）
git diff --staged
# 或
git diff --cached

# 比對特定檔案的修改
git diff <檔案名稱>
```

---

## 5. 檢視歷史紀錄（Log）

```bash
# 檢視完整的提交歷史紀錄（按 q 鍵離開）
git log

# 單行簡潔模式，適合快速瀏覽歷史
git log --oneline

# 限制顯示最近 N 筆紀錄
git log --oneline -n 5

# 圖形化分支歷史樹
git log --graph --oneline --all
```

---

## 6. 分支管理（Branch & Switch）

```bash
# 列出本地所有分支（* 代表目前所在分支）
git branch

# 建立新分支
git branch <分支名稱>

# 切換到指定分支（現代建議語法）
git switch <分支名稱>
# 傳統語法：git checkout <分支名稱>

# 建立並直接切換到新分支
git switch -c <新分支名稱>
# 傳統語法：git checkout -b <新分支名稱>

# 合併分支（需先切換到接收合併的分支，例如 main）
git switch main
git merge <要合併過來的分支名稱>

# 刪除已合併的分支
git branch -d <分支名稱>

# 強制刪除未合併的分支
git branch -D <分支名稱>
```

---

## 7. 遠端協作與同步（Remote, Push, Pull）

與 GitHub 等遠端平台同步：

```bash
# 檢視目前關聯的遠端儲存庫資訊
git remote -v

# 關聯遠端儲存庫（首次建立時常用）
git remote add origin <遠端倉庫網址>

# 首次推送到遠端並設定預設上游分支（upstream）
git push -u origin main

# 後續推送已設定過上游的當前分支
git push

# 從遠端下載並自動合併最新進度到當前分支
git pull

# 僅獲取遠端最新資訊（不自動合併）
git fetch origin
```

---

## 8. 暫存工作進度（Stash）

當工作做到一半需要臨時切換分支修復其他問題時，可先將未完成的工作打包暫存：

```bash
# 暫存目前未 commit 的修改
git stash

# 暫存並加上備註說明
git stash save "功能做到一半"

# 檢視暫存清單
git stash list

# 取出並套用最近一次暫存的內容，同時從清單刪除
git stash pop

# 放棄/刪除最近一次暫存
git stash drop
```

---

## 9. 復原與撤銷（Restore, Reset, Revert）

> [!CAUTION]
> 包含 `reset --hard` 的操作會永久捨棄未提交的程式碼，執行前請確認已無需要的變更。

```bash
# 放棄工作區特定檔案的修改（尚未 git add 的變更）
git restore <檔案名稱>

# 將檔案從暫存區移回工作區（Unstage，撤銷 git add）
git restore --staged <檔案名稱>

# 修改上一次 commit 的訊息（或補加遺漏的檔案）
git add <遺漏的檔案>
git commit --amend -m "新的說明訊息"

# 軟重設：撤銷上一次 commit，但保留修改在暫存區
git reset --soft HEAD~1

# 混合重設（預設）：撤銷 commit，修改回到工作區（未暫存）
git reset HEAD~1

# 硬重設：完全捨棄上一次 commit 及所有變更（危險操作）
git reset --hard HEAD~1
```

---

## 10. 常用忽略設定（.gitignore）與注意事項

在 Python 與 `uv` 專案中，不建議將虛擬環境、暫存檔與快取提交至 Git。專案根目錄的 `.gitignore` 建議加入：

```gitignore
# Python 快取與編譯檔
__pycache__/
*.py[cod]

# uv 與虛擬環境
.venv/
env/
venv/

# Jupyter 筆記本暫存檔
.ipynb_checkpoints/

# 編輯器暫存
.vscode/*
!.vscode/settings.json
.DS_Store
*.tmp
```

---

### 速查精選：最常打的一套流程

```bash
git status                   # 先看狀態
git add .                    # 加入所有修改
git commit -m "feat: 說明"   # 提交並留紀錄
git push                     # 推到 GitHub
```
