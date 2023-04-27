
def display_main_menu():
    print("enter some numbers seperated by commas")

def calc_average(x):
    op = sum(x)/len(x)
    print(op)
def get_user_input():
    temp = input('numbers: ')
    float_temp = temp.split(',')
    floats = [float(float_temp[i]) for i in float_temp]
    return floats
def find_min_max(x):
    floats = []
    floats.append(min(x))
    floats.append(max(x))
    return floats
def sort_temperature(x):
    floats = x
    floats.sort()
    return floats
def calc_median_temperature(x):
    float_ = (x[len(x)/2]+x[(len(x)/2)-1])/2 if len(x)%2==0 else x[int(len(x)/2)]
        
    return float_
def main():
    print("DevOps lab2")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    minmax = find_min_max(num_list)
    tempsort = sort_temperature(num_list)
    med = calc_median_temperature(tempsort)
    print(minmax)
    print(tempsort)
    print(med)
    
if __name__ == "__main__":
    main()
