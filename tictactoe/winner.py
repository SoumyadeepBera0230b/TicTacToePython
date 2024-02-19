def check_winner(x_values, o_values):
    x_values = set(x_values)
    o_values = set(o_values)
    case1 = {1, 2, 3}
    case2 = {4, 5, 6}
    case3 = {7, 8, 9}
    case4 = {1, 4, 7}
    case5 = {2, 5, 8}
    case6 = {3, 6, 9}
    case7 = {1, 5, 9}
    case8 = {3, 5, 7}
    if (case1.issubset(x_values) or case2.issubset(x_values)or
        case3.issubset(x_values)or case4.issubset(x_values) or
        case5.issubset(x_values) or case6.issubset(x_values) or
        case7.issubset(x_values) or case8.issubset(x_values)):
        # print("X is the winner"
        return "x"
    elif (case1.issubset(o_values) or case2.issubset(o_values) or
        case3.issubset(o_values) or case4.issubset(o_values) or
        case5.issubset(o_values) or case6.issubset(o_values) or
        case7.issubset(o_values) or case8.issubset(o_values)):
        # print("O is the winner")
        return "o"
    return " "
