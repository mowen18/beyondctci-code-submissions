# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def find_duplicate_files(paths):
    content_path = {}

    for path in paths:
        contentstart = path.index('(')
        content = path[contentstart + 1:-1]
        pathtrim = path[:contentstart]

        if content not in content_path:
            content_path[content] = []
        content_path[content].append(pathtrim)
    res = []
    for files in content_path.values():
        if len(files) > 1:
            res.append(files)
    return res


        

