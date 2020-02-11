from support_symbol import text00, text01, text02, text03, text04, text05
def cartesian(get_value):
    for get in range(get_value):
        print(text00)
        if get ==(get_value/2-1):
            for get in range(int(get_value/2), int(get_value/2) +1):
                print(text00 +(text04*get_value))