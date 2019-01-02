def coin_toss(n):

      
      import random

      contrl_sum = 0
      contrl_sum1 = 0
      
      for i in range(0,n) :
          result = random.randint(0,1)
          if result == 0:
              contrl_sum += 1
          elif result == 1:
              contrl_sum1 += 1
      print("Heads - %s" % contrl_sum1)
      print("Tails - %s" % contrl_sum)


    
              



        
        
    
