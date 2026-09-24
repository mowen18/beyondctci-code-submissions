# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def find_password(check_password, max_length):
    def visit(password):
        if check_password(password):
            return password
        if len(password) >= max_length:
            return
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in password:
                continue
            result = visit(password + char)
            if result:
                return result
        return
    return visit("")
