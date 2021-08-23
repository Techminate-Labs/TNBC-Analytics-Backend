from v1.constants.constants import TIMESHEET_MEMO_TAG, PROJECT_MEMO_TAG, BOUNTY_REQUEST_MEMO_TAG

from ..models.transactions import Transaction


def parse_memo(memo):

    memo_type = Transaction.UNIDENTIFIED
    github_issue = 0

    splited_memo = memo.split('_')

    if len(splited_memo) >= 3:

        if splited_memo[1] in TIMESHEET_MEMO_TAG:
            memo_type = Transaction.TIMESHEET
        elif splited_memo[1] in PROJECT_MEMO_TAG:
            memo_type = Transaction.PROJECT
        elif splited_memo[1] in BOUNTY_REQUEST_MEMO_TAG:
            memo_type = Transaction.BOUNTY
        
        try:
            github_issue = int(splited_memo[2])
        except:
            pass

    return memo_type, github_issue
