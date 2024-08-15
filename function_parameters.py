
def fun_a(p1, p2):
    pass

fun_a(5, 10)
fun_a("abc", "monkey-business")

def fun_b(p1, *p2):
    pass

fun_b(10)
fun_b(1, 2, 5, 99, "wombat", 38, "rumpus")

def fun_c(*, spam, ham):
    pass

fun_c(spam=10, ham=20)
fun_c(ham=10, spam=20)

def grep(pattern, *files, ignore_case=False):
    pass

grep("wombat", "australian_mammals.txt", "funny_names.txt", "something_else.txt")
grep("Lincoln", "presidents.txt", ignore_case=True)

grep("foobar", *file_list)

