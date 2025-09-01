from App import logic as l


def run_create_dataframes()->dict:
    dataframes = l.create_dataframes()
    dataframe_names = list(dataframes.keys())
    
    print()
    print(dataframe_names, end="\n\n")
    
    df = dataframes[dataframe_names[0]]
    print(df.head(), end="\n\n")
    
    print(df.info(), end="\n\n")
    
    return dataframes


def menu()->int:
    print('WELCOME TO HOUSING PRICING ANALYSIS - CHOOSE OPTION',
          '\n1 - Load datasets')
    
    run = True
    while run:
        try:
            choice = int(input("\nOption: "))
            run = False
        except TypeError:
            print('Invalid option...')
    
    return choice
        

def main()->None:
    choice = menu()
    new_logic = None
    
    if choice == 1:
        new_logic = run_create_dataframes()