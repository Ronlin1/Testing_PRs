# This is a test file containing test function code:
# If you do not know Python: Just Add A comment by numbering them:
# comment 1: Test 1 By Ronlin .....
# My initial pr -> Test 2 by Ronlin
#
#

def test_pr(code):
    pr = list()
    pr.insert(0, "Add Anything")

    if code != " ":
        pr.append(code)
        print("Merged pull request, congs >>")
        print(f"Main is now {pr}")
    else:
        print(f"Your empty '{code}' code has been rejected")
your_pull_request = "food"
test_pr(your_pull_request)

# Just Add Anything in the function above if you know some python
