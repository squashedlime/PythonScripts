def test_func(large, small):
    print"This is large %r" % large
    print"This is small %r" % small
    print"They are so different!\n"
    
print"parsing directly"
test_func(1000, 2)


print"doing it with a bit of math"
big_num = 1000
small_num = 4

test_func(big_num*3, small_num*2)




