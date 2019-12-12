from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def passwordCracker(passwords, loginAttempt, memo={}):
    """
    Checks if the loginAttempt is valid or not based on the problem definition,
    i.e. the loginAttempt can be made up from the given by concatenation.
    :param passwords: The passwords of all the users.
    :param loginAttempt: The loginAttempt to be validated.
    :param memo: A dictionary to hold the combinations for a password.
    :return:
    """
    # If we already have the answer return it.
    if loginAttempt in memo: return memo[loginAttempt]

    # If the attempted password is already a valid password, return it.
    if loginAttempt in passwords:
        memo[loginAttempt] = [loginAttempt]
        return memo[loginAttempt]

    # For every password,
    for password in passwords:
        _len = len(password)

        # We try to match the current loginAttempt to the current password,
        # If we find a match, we try again on the remainder of the loginAttempt
        if loginAttempt[:_len] == password:
            result = passwordCracker(passwords, loginAttempt[_len:], memo)

            # If we find a valid combination, return.
            if result != 'WRONG PASSWORD':
                memo[loginAttempt] = [password] + result
                return memo[loginAttempt]

            # Otherwise no combination is possible for the given attempt.
            else:
                memo[loginAttempt] = 'WRONG PASSWORD'
                return memo[loginAttempt]


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt)
        if result != False:
            print(' '.join(result))
        else:
            print('WRONG PASSWORD')

        print('"' + " ".join(result) + '"')