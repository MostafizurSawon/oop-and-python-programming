def fun(arg1, **kwargs):
    print("arg1->", arg1)
    print("**kwargs->", kwargs)

fun(arg1=1, arg2=2, arg3=3)