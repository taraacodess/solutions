from test_twttr import shorten

def main ():
    test()

def test():
    assert shorten("hello")=="hll"  

if __name__ == "__main__":
    main()
   
        