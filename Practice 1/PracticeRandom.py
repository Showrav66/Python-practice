def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print("list contains an even number")
            break

    # This else executes only if break is NEVER
    # reached and loop terminated after all iterations.
    else:
        print("list does not contain an even number")