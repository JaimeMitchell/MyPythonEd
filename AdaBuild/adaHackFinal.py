import math

#define function
def subscription_summary():
  num = int(input("How many accounts would you like to enter? "))
  print("Welcome to the Ada+ Account Dashboard")
  print()

#Months_subscribed
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
    
    #AD-FREE1
  ad_free_list = []
  for i in range(num):
    ad_free_months  = float(input("ad_free_months: "))
    ad_free = ad_free_months * 2.00
    ad_free_list.append(ad_free)
      
  #VOD
  vod_list = []
  for i in range(num):
    video_on_demand_purchases = int(input("video_on_demand_purchases: "))
    video_on_demand_purchases = float(video_on_demand_purchases)
    vod = video_on_demand_purchases * 27.99
    vod_list.append(vod)
   # account["vod"] = vod_list


  #total amount for ad_free and vod, keep out of loop, print once
  premium = 0
  for i in range (num): 
    premium = premium + ad_free_list[i] + vod_list[i]
    
  #Sum of arguments per account & appending to a list for sum of all three accounts and tracking the best customer.
  account_total = []
  for i in range (num):     
    total = months_list[i] + ad_free_list[i] + vod_list[i]
    account_total.append(total) 
  
  #Sum all accounts
  all_total = 0
  for i in range (num):
    all_total = all_total + account_total[i] 
        
  #This is to be able to grab the highest paying customer and also to be able to grab the user's ID number for formatting.
  number = 0
  number_list = []
  for i in range (num):
    number = number + 1
    number_list.append(number)  
    totals_nums = [[i, j] for i, j in zip(account_total,number_list)]
    rev = [[i, j] for i, j in zip(account_total,number_list)]
  rev.sort(reverse=True)
  best = rev[0]
  x = best[1]
  
  #OUTPUT
  for i in range(num):
    print(f'Account {(totals_nums)[i][1]} made ${(account_total)[i]:.2f} total')
    print()
    print(f'>>> ${months_list[i]:.2f} from monthly accounts fees')
    print()
    print(f'>>> ${ad_free_list[i]:.2f} from Ad-free upgrades')
    print()
    print(f'>>> ${vod_list[i]:.2f} from Video on Demand purchases')
    print()
  print(f'Combined all accounts made ${all_total:.2f} total')
  print(f'Premium content (Ad-free watching and Video on Demand) made ${premium:.2f}')
  print()
  print(f'${best[0]:.2f} was the most earned by any single account')
  print(f'The accounts that earned the most were: #{x}')
  print('')          

#Calling function   
subscription_summary()