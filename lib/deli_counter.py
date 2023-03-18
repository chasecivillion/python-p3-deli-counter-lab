katz_deli = []

def line(name):
    if name == []:
        print("The line is currently empty.")
    else:
        current_line = "The line is currently:"
        for i in range(len(name)):
            current_line += f' {i+1}. {name[i]}'
        print(current_line)

    
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if katz_deli == []:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        katz_deli.remove(katz_deli[0])