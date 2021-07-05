import re
tests=["test_flipkartuser1.py","test_snapdealuser1.py","test_snapdealuser2.py","test_flipkartuser2.py"]
for test in tests:
    f = open(test, "r")
    print('clicks in "'+test+'" : ',len(re.findall("click", f.read())))
    f = open(test, "r")
    print('cancel a course of action in "'+test+'" : ',len(re.findall(".close()", f.read())))

