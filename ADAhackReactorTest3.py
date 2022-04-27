for i in range(3):
    m= input("months_subscribed:")
for i in range(3):
    a= input("ad_free_months:")
for i in range(3):
    v= input("video_on_demand_purchases")

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    
    #account = integer 3, user input prompt added to parameters
    #This only prints once but output is making it print twice. It's outside the loops :(
    print("Welcome to the Ada+ Account Dashboard")
    print()
    months_list = []
    for i in range (3):
        months = 0 #reset months for next pass
        months_subscribed = float(months_subscribed)
        if months_subscribed == 1:
            months = 7.00
        elif months_subscribed == 2:
            months = 14.00
        elif months_subscribed % 3 == 0:
            months = months_subscribed /3 * 18.00
        elif months_subscribed % 3 == 1:
            months = months_subscribed - 1
            months = months_subscribed /3 * 18.00 + 7.00 #remaining number that's now divisible by 3
        elif months_subscribed % 3 == 2:
            months = months_subscribed - 2 
            months = months_subscribed /3 * 18.00 + 14.00 #remaining number that's now divisible by 3
    ad_free_list = []
    for i in range(3):
        ad_free_months = int(ad_free_months) 
        ad_free = ad_free_months * 2.00
        ad_free_list.append(ad_free) #for ad_free + vod loop below All accounts
    vod_list= []
    for i in range(3):
        video_on_demand_purchases = float(video_on_demand_purchases)
        vod = video_on_demand_purchases * 27.99
        vod_list.append(vod) #for ad_free + vod loop below All accounts
    user_total_list = []
    for i in range(3):
        user_total = 0.00
        user_total = months + ad_free
        print(sum(user_total_list))
    best_customer = 0
    for i in range(3):
        for j in user_total_list:
            if user_total > best_customer:
                best_customer = user_total
    premium = ad_free + vod
    
#print(f'accounts {Account}\n\ntotal months {months}\nad_free {ad_free}\nvod {vod}\nuser total {user_total}\nall_total {all_total}\npremium {premium}\nbest_customer{best_customer}')

subscription_summary(m,a,v)