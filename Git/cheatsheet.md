### To stash your working directory including untracked files
```bash
git stash -u
```

question id: 999cc5aa-d495-498d-87d4-02c175a34d9a

### How to stash by name:
```bash
git stash push -m aNameForYourStash
```

question id: 6c1d011d-9417-479c-93e7-763b8cbc309e


### How to pop stash by name

```bash
git stash list
git stash pop --index 0
```

question id: d126492e-21e6-44a7-a8e0-5c26ef08b6b1


### How to apply your stash without deleting it?

answer:

git stash apply
or
git stash apply --index 0  # by name

question id: 2812e8c5-a3cf-45d2-b392-addcaf09ccf9


### How to abort applying of a stash when it caused conflicts?

answer:

git reset --merge

then delete untracked files

question id: f103f098-d77b-4373-ac17-8fbf8af976de


### Clear all your stashes

```bash
git stash clear
```

question id: 1d50ac23-c007-408b-92c7-62d2ac810a64


### How to do git rebase step by step?

0.1 git checkout master
0.2 git pull
0.3 git checkout your_branch
---  
1. git rebase origin/master
2. if there are any conflicts: 
    2.1(Pycharm > VCS > Git > Resolve Conflicts > Merge - there will be a window for resolving conflicts)
    2.2 git add .
    2.3. git rebase --continue
    2.4 (sometimes 2-4 you have to do several times until there is no conflicts anymore)
3. If there are any staged files:
    3.1 git commit --amend --no-edit
4. if your have your branch already pushed
    4.1 git push --force-with-lease
    else
    git push
    
question id: 809e6dc5-116d-4f3d-a1e6-976696afb592


### How to revert last commit?
```
git revert HEAD
```
question id: 0652bc77-9d44-49d6-a85e-06ce7586bca3


### How to revert last 3 commits?

```
git revert HEAD~2^..HEAD
```
or

```
git revert HEAD~3..HEAD
```
where HEAD it the latest commit, HEAD~1 is second to last commit, and HEAD~2 is your third commit

There is good picture of how it looks like (B's and G's are commits, where B3 is the latest commit and
G1 is the sixth commit from the latest)
```
G1 - G2 - G3 - B1 - B2 - B3
           \    \    \    \-- HEAD
            \    \    \------ HEAD~1
             \    \---------- HEAD~2
              \-------------- HEAD~3
```

http://serebrov.github.io/html/2014-01-04-git-revert-multiple-recent-comments.html

question id: 7ad17af3-98bd-409b-8f73-486b87b2787b


### How to undo last LOCAL commit, but retain what was changed

```
git reset HEAD~1
but if you have something that is not commited, non commited changes will be erased, so
git stash
git reset HEAD~1
git stash pop
```

question id: d8d4e36e-f50b-4c0a-99e2-941e03635e3f


### How to unstage file? 

answer

unstage file:
git reset filename

question id: d3ee8353-4284-43ae-8e73-5d621b8ab8c1


### How to see what was changed in a commit?

Last commit: git show
Several commits: git show -3 (or another number of commits)

question id: 39b2f12c-ed46-40d1-97ca-9715d1fa94be


### How to rename a branch you are in?

answer:

git branch -m new-branch-name

question id: a34bef12-9205-4547-b004-1137466ad83f


### How to create a new branch from a specific commit?

answer
git checkout -b new-branch-name <commit-sha>

question id: 096eaf66-b71e-40d1-93cd-734f47fdee56