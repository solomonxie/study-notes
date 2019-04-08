# Pip specify branch, commit or tag to install in `requirements.txt` [DRAFT]

Sometime we need to fix a bug in a lib or package, but before testing it in the caller module, we don't want to merge the bug-fixing branch to master.
At this point, what we should do is to temporarily specify the `feature-branch` of the package, and install it then to test it with the caller.

[Refer to: How to state in requirements.txt a direct github source](https://stackoverflow.com/a/35998253/9172013)

Format:
```
# requirements.txt

LIB-NAME @ git+ssh://git@git.github.com/Jason/LIB-NAME.git@BRANCH-NAME#egg=LIB-NAME
```

The `branch-name` could also be `tag-name` or `commit-id`.
