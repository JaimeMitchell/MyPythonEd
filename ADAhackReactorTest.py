import math

#define function
def subscription_summary():
  num = int(input("How many accounts would you like to enter? "))
  print("Welcome to the Ada+ Account Dashboard")
  print()
    
  account = {}
  months_list = []
  for i in range(num):
    months_subscribed = int(input("months_subscribed: "))
    months_subscribed=float(months_subscribed)
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
    months_list.append(months)
    #account["months"] = months
    
    #AD-FREE1
  ad_free_list = []
  for i in range(num):
    ad_free_months  = float(input("ad_free_months: "))
    ad_free = ad_free_months * 2.00
    ad_free_list.append(ad_free)
   # account["ad_free"] = ad_free
    #print(f'ad-free {account["ad_free"]}')
      
  #VOD
  vod_list = []
  for i in range(num):
    video_on_demand_purchases = int(input("video_on_demand_purchases: "))
    video_on_demand_purchases = float(video_on_demand_purchases)
    vod = video_on_demand_purchases * 27.99
    vod_list.append(vod)
   # account["vod"] = vod_list


  #total amount for ad_free and vod, keep out of loop, print once
  # but need a loop to grab numbers from these lists
  premium = 0
  for i in range (num): 
    premium = premium + ad_free_list[i] + vod_list[i]
    
  #Sum of arguments per account & appending to a list for sum of all three accounts and tracking the best customer.
  best_customer = 0 
  account_total = []
  for i in range (num):     
    total = months_list[i] + ad_free_list[i] + vod_list[i]
    account_total.append(total) 
    if account_total[i] > best_customer:
      best_customer = account_total[i]
  
  #account["account_total"] = account_total[i]
  
  name = 0
  name_list = []
  for i in range (num):
      name = name + 1
      name_list.append(name)  
      namesAndTotals = (list(zip(name_list, account_total)))
      
  #Sum of ALL accounts, outside the loop
  all_total = 0
  for i in range (num):
    all_total = all_total + account_total[i]     
     
  #OUTPUT
  for i in range(0,num,1):
    print(f'Account {namesAndTotals[i][0]} made {account_total[i]:.2f} total')
    print()
    print(f'>>> {months_list[i]:.2f} from monthly accounts fees')
    print()
    print(f'>>> {ad_free_list[i]:.2f} from Ad-free upgrades')
    print()
    print(f'>>> {vod_list[i]:.2f} from Video on Demand purchases')
    print()
  print(f'Combined all accounts made {all_total:.2f} total')
  print(f'Premium content (Ad-free watching and Video on Demand) made {premium:.2f}')
  print()
  print(f'{best_customer:.2f} was the most earned by any single account')
  print(f'The accounts that earned the most were: {best_customer:.2f}')
  print('')          

#print(f'{account["Account"]} made {account["user_total"]:.2f} total\n\n>>>{account["months"]:.2f} from monthly accounts fees\n\n>>> {account["ad_free"]:.2f} from Ad-free upgrades\n\nCombined all accounts made {all_total:.2f} total\n\nPremium content (Ad-free watching and Video on Demand) made{premium}{best_customer}was the most earned by any single accountThe accounts that earned the most were:{best_customer}')
   
subscription_summary()