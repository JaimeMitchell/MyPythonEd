
'''for i in range(3):
        accounts = []   #account 1, account 2, account 3
        ask_months = float(input("months: "))
        accounts.append(ask_months)
        ask_ad_free = float(input("ad_free: "))
        accounts.append(ask_ad_free)
        ask_vod = float(input("voc: "))
        accounts.append(ask_vod)
        accounts.append(accounts)
        print(accounts)
        print(accounts)'''
#months_subscribed = int(input("How many months would you like to subscribe? "))
#ad_free_months = int(input("How many ad_free months would you like "))
#video_on_demand_purchases = int(input("How many overpriced Videos on Demand would you like?"))

from ctypes.wintypes import FLOAT
import math

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):

    #This only prints once but output is making it print twice. It's outside the loops :(
    print("Welcome to the Ada+ Account Dashboard")
    print()
    #accounts = ["Account 1", "Account 2", "Account 3"]
    account = []   
    accounts = [] 
    #account.append(months_subscribed)
    #account.append(ad_free_months)
    #account.append(video_on_demand_purchases)
       
    #Add months to list
    months_list = []
    for i in range (3):
        
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
            months_list.append(months)
            account.append(months)
        #AD-FREE
    ad_free_list = []
    for i in range(3):
        ad_free = ad_free_months * 2
        ad_free_list.append(ad_free) #for ad_free + vod loop below All accounts
        account.append(ad_free) #for individual customer
        
      
    #VOD
    vod_list= []
    for i in range(3):
        vod = video_on_demand_purchases * 27.99
        vod_list.append(vod) #for ad_free + vod loop below All accounts
        account.append(vod) #for individual customer
    
    #user sum total
    user_total_list = []
    for i in range(3):
        user_total = months + ad_free + vod
        user_total_list.append(user_total)
        account.append(user_total)
    
    #put all accounts in here    
    accounts.append(account)
    #Sum of all accounts, keep out of loop, print once
    all_total = sum(user_total_list)        
       
    #total amount for ad_free and vod, keep out of loop, print once
    # but need a loop to grab numbers from these lists
    
    premium = lambda x,y: x + y
    x = [ad_free_list]
    y = [vod_list]
    print(f'premium{premium}')


#$92.97 was the most earned by any single account
#The accounts that earned the most were: #1
    accounts.append(account)
    best_customer = 0
    for i in accounts:
        for j in user_total_list:
            if user_total > best_customer:
                best_customer = user_total
#OUTPUT
        
    print(f"{accounts[0:3:1]} made {user_total:.2f} total")
    print(f'>>> {months:.2f} from monthly accounts fees')
    print(f'>>> {ad_free:.2f} from Ad-free upgrades')
    print(f'>>> {vod:.2f} from Video on Demand purchases')
    print(f'Combined all accounts made {all_total:.2f} total')
    print(f'Premium content (Ad-free watching and Video on Demand) made{premium}')
    print(f'{best_customer:2f}was the most earned by any single account')
    print(f'The accounts that earned the most were:{best_customer:2f}')
        

for i in range(3): 
    ask_months = float(input("months: "))
    ask_ad_free = float(input("ad_free: "))
    ask_vod = float(input("voc: "))
    subscription_summary(ask_months,ask_ad_free,ask_vod)