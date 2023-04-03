while(1):
    st = input()
    lst = st.lower()
    find_list = ["a","e","i","o","u"]
    count = 0
    if lst == '#':
        break;
    for i in range(len(lst)):
        for find in find_list:
            if find == lst[i]:
                # print(count)
                count += 1
                
    print(count)