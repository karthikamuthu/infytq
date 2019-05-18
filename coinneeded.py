def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    t=((no_of_one*1)+(no_of_five*5))
    if(t<rupees_to_make):
        print(-1)
    else:
            if(five_needed<=no_of_five):
                five_needed=rupees_to_make//5
            if(one_needed<=no_of_one):    
               one_needed=rupees_to_make%5
            else:
                print("no_of_five needed:",five_needed)
                print("no_of_one needed:",one_needed)
                print(-1)
 make_amount(28,8,5)               
