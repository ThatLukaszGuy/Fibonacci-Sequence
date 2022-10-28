import questionary
from colorama import Fore, Style,init
from fibonacci import Fibonacci
import time

# needed for colorama
init()

# class init
Fi = Fibonacci()

# color config for shortcuts in print statements
s = Style.RESET_ALL
sb = Style.BRIGHT
f = {
    'r': Fore.RED,  
    'g': Fore.GREEN,
    'y': Fore.YELLOW,
    'b': Fore.BLUE,
    'm': Fore.MAGENTA,
    'c': Fore.CYAN,
    'w': Fore.WHITE, 
}

# handle specific answers
def check_block(answer):
    if answer == 'Show x amount of fibonacci values (starting at 1)':
        sequence_num = int(input('State how many numbers of the sequence you want shown: '))
        for n in range(1, sequence_num + 1):
            print(f"{f['y']}{sb} {n} {s}: {f['g']}{sb}{Fi.fibonacci(n)} {s}{chr(10)} {f['y']}{sb}Ratio: {s}{f['g']}{sb}{Fi.fibonacci(n + 1) / Fi.fibonacci(n)} {s}{chr(10)}") # it looks weird due to the colors

        else:
            confirm()        

    elif answer == 'Get previous sequence value':
        n = int(input('Input the number you want to get the previous position of: '))
        print(f"{f['m']}{sb}Previous Value is approx.{s} :{f['c']}{sb} {str(Fi.previous_num(n))} {s}")
        confirm()

    elif answer == 'Get next sequence value':
        n = int(input('Input the number you want to get the next position of: '))
        print(f"{f['m']}{sb}Next Value is approx.{s} :{f['c']}{sb} {str(Fi.next_num(n))} {s}")
        confirm()

    elif answer == "Access certain position in the sequence and it's ratio (e.g. 7th position has the value of 13)":
        search_index = int(input("Access certain position in the sequence and it's ratio (e.g. 7th position has the value of 13): "))
        print(f"{f['m']}{sb}Value at postion {search_index}{s}:{f['c']}{sb} {Fi.fibonacci(search_index)} {s},{f['m']}{sb} ratio:{s} {f['c']}{sb} {Fi.fibonacci(search_index + 1) / Fi.fibonacci(search_index)}{s}")
        confirm()

    elif answer == 'Get value between two different values that are one apart (e.g. 144, 377 => 233)':
        prev_n, next_n = [int(n) for n in input("input two values of the sequence, that are one apart: ").split(",")]
        print(f"{f['w']}{sb}The value between{s} {f['r']}{sb}{prev_n}{s} {f['w']}{sb} and{s} {f['g']}{sb} {next_n}{s}{f['w']}{sb} is approximately: {s}{f['y']}{sb}{Fi.between_val(prev_n, next_n)} {s}")
        confirm()

    elif answer == 'Get list of neighboring previous or following values':
        try:
            val, amount, direction = [int(n) for n in input("input the sequence value (e.g 144), how many neighboring values to print (e.g. 10) and whether to print the previous or following values (1 = following, 0 = previous)  (example input: 144 10 0) : ").split(' ')]
            list = Fi.get_neighbor_vals(val, amount, direction)      
            print(f"{f['m']}{sb}Neighboring values in chosen direction starting from nearest{s}")
            count = 1
            for i in list:
                print(f"{f['c']}{count} :{sb} {i} {s}")
                count += 1
            confirm()
        except:
            print(f"{f['r']}{sb} Check that all arguments are provided and seperated with a space (e.g:144 10 0) {s}")
            confirm()
    
    elif answer == 'Visualize x amount of fibonacci values':
        vis = int(input('State how many values of the sequence you want shown: '))
        Fi.visualize(vis)
        confirm()
    else:
        pass

def asking():
    answer = False
    answer = questionary.select(
    "What do you want to do?",
        choices=[
            'Show x amount of fibonacci values (starting at 1)',
            'Get previous sequence value',
            'Get next sequence value',
            "Access certain position in the sequence and it's ratio (e.g. 7th position has the value of 13)",
            'Get value between two different values that are one apart (e.g. 144, 377 => 233)',
            'Get list of neighboring previous or following values',
            'Visualize x amount of fibonacci values',
            'Quit'

        ]).ask()  # returns value of selection
    return answer


# check whether some1 wants to go back 
def confirm():
    confirm_val = questionary.confirm("Do you want to continue and go back to the main menu?").ask()
    if confirm_val:
        check_block(asking())
    else:
        print(f"{f['b']}{sb}Closing Program... Bye! {s}")
        time.sleep(2)
        pass

# first run
a = asking()
check_block(a)
