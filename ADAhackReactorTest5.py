
from ctypes.wintypes import CHAR
from pickle import FALSE
import math

#define function
def subscription_summary():       
    for i in range(3):
        months_subscribed = int(input("months: "))
        ad_free_months  = int(input("ad_free: "))
        video_on_demand_purchases = int(input("voc: "))
    
    print("Welcome to the Ada+ Account Dashboard")
    print()
    #{Account 3 made $45.99 total  

    #>>> $14.00 from monthly subscription fees
    #>>> $4.00 from Ad-free upgrades
    #>>> $27.99 from Video on Demand purchases

    #Combined all accounts made $152.96 total

    #Premium content (Ad-free watching and Video on Demand) made premium = ad_free_list + vod_list total

    #{user_total_key} was the most earned by any single account
    #The accounts that earned the most were: # {user_total_key[value]}}'''

    #print(f'{account["Account"]} made {account["user_total"]:.2f} total\n\n>>>{account["months"]:.2f} from monthly accounts fees\n\n>>> {account["ad_free"]:.2f} from Ad-free upgrades\n\nCombined all accounts made {all_total:.2f} total\n\nPremium content (Ad-free watching and Video on Demand) made{premium}{best_customer}was the most earned by any single accountThe accounts that earned the most were:{best_customer}')
    #print(f'{account["name"]} made {account["user_total"]:.2f} total')
    
    account = {}

    for i in range(3):
        months_subscribed = float(months_subscribed)
        if months_subscribed == 1.00:
            months = 7.00
        elif months_subscribed == 2.00:
            months = 14.00
        elif months_subscribed % 3.00 == 0.00: 
            months = months_subscribed / 3.00 * 18.00
        elif months_subscribed % 3.00 == 1.00:
            months = months_subscribed - 1.00
            months = months_subscribed / 3.00 * 18.00 + 7.00 #remaining number that's now divisible by 3
        elif months_subscribed % 3.00 == 2.00:
            months = months_subscribed - 2.00 
            months = months_subscribed / 3.00 * 18.00 + 14.00 #remaining number that's now divisible by 3
        account["months"] = months
    print(f'months {account["months"]}')
    
    #AD-FREE
    ad_free_list = []
    ad_free = ad_free_months * 2.00
    account["ad_free"] = ad_free
    print(f'ad-free {account["ad_free"]}')
    
    #VOD
    vod_list = []
    video_on_demand_purchases = float(video_on_demand_purchases)
    vod = video_on_demand_purchases * 27.99
    account["vod"] = (vod)
    vod_list.append(vod)
    print(f'vod {account["vod"]}')
    
    #total amount for ad_free and vod , keep out of loop, print once
    # but need a loop to grab numbers from these lists
    
    premium = ad_free + vod
    print(f'premium {premium}')
    
    #Sum of arguments per account & appending to a list for sum of all three accounts and tracking the best customer.
       
    user_total = account["months"] + account["ad_free"] + account["vod"]
    account["user_total"] = user_total
    user_total_list = []
    user_total_list.append(user_total)
    print(f'user_total value {account["user_total"]}')
    print(f'user_total_list {user_total_list}')

    all_total = sum(user_total_list)
    print(f'all_total {all_total}')


    #best_customer
    best_customer = 0
    for i in user_total_list:
        if user_total > best_customer:
            best_customer = user_total
    print(f'best_customer {best_customer}')
    # append all account dictionaries to a list:

    roster = []
    roster.append(account)
    print(f'roster {roster}')
   
    #Sum of ALL accounts, outside the loop
    

            
#{Account 3 made $45.99 total  

#>>> $14.00 from monthly subscription fees
#>>> $4.00 from Ad-free upgrades
#>>> $27.99 from Video on Demand purchases

#Combined all accounts made $152.96 total

#Premium content (Ad-free watching and Video on Demand) made premium = ad_free_list + vod_list total

#{user_total_key} was the most earned by any single account
#The accounts that earned the most were: # {user_total_key[value]}}'''

    #print(f'{account["Account"]} made {account["user_total"]:.2f} total\n\n>>>{account["months"]:.2f} from monthly accounts fees\n\n>>> {account["ad_free"]:.2f} from Ad-free upgrades\n\nCombined all accounts made {all_total:.2f} total\n\nPremium content (Ad-free watching and Video on Demand) made{premium}{best_customer}was the most earned by any single accountThe accounts that earned the most were:{best_customer}')
    #print(f'{account["name"]} made {account["user_total"]:.2f} total')
    print()
    print(f'>>> {account["months"]:.2f} from monthly accounts fees')
    print()
    print(f'>>> {account["ad_free"]:.2f} from Ad-free upgrades')
    print()
    print(f'>>> {vod:.2f} from Video on Demand purchases')
    print()
    print(f'Combined all accounts made {all_total:.2f} total')
    print(f'Premium content (Ad-free watching and Video on Demand) made{premium}')
    print()
    print(f'{best_customer}was the most earned by any single account')
    print(f'The accounts that earned the most were:{best_customer}')   

# calling function
subscription_summary()