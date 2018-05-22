import time
def typer(to_print):
    count = 0
    printing = list(to_print)        
    while count < len(to_print):
        print(printing[count],end="")
        time.sleep(0.005)
        count = count + 1
    print('')
