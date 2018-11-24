  1 import random
  2 board_size = 10
  3 computer = 'c'
  4 user = 'u'
  5 EMPTY = '_'
  6 def create_board():
  7     board1 = [[EMPTY for x in range(board_size)]for x in range(board_size)]
  8     return board1
  9 def print_board(num1, coin1, num2, coin2):
 10     board = create_board()
 11     if num1 <= 10:
 12         if num1 == 0:
 13             board[9][num1] = EMPTY
 14         else:
 15             board[9][num1 - 1] = coin1
 16     elif num1 <= 20:
 17         board[8][20 - num1] = coin1
 18     elif num1 <= 30:
 19         board[7][num1 - 21] = coin1
 20     elif num1 <= 40:
 21         board[6][40 - num1] = coin1
 22     elif num1 <= 50:
 23         board[5][num1 - 41] = coin1
 24         elif num1 <= 60:
 25         board[4][60 - num1] = coin1
 26     elif num1 <= 70:
 27         board[3][num1 -61] = coin1
 28     elif num1 <= 80:
 29         board[2][80 - num1] = coin1
 30     elif num1 <= 90:
 31         board[1][num1 - 81] = coin1
 32     elif num1 <= 100:
 33         board[0][100 - num1] = coin1
 34 
 35     if num2 <= 10:
 36         if num2 == 0:
 37             board[9][num2] = EMPTY
 38         else:
 39             board[9][num2 - 1] = coin2
 40     elif num2 <= 20:
 41         board[8][20 - num2] = coin2
 42     elif num2 <= 30:
 43         board[7][num2 - 21] = coin2
 44     elif num2 <= 40:
 45         board[6][40 - num2] = coin2
 46     elif num2 <= 50:
 47         board[5][num2 - 41] = coin2
 48     elif num2 <= 60:
 49         board[4][60 - num2] = coin2
 50     elif num2 <= 70:
 51         board[3][num2 - 61] = coin2
 52     elif num2 <= 80:
 53         board[2][80 - num2] = coin2
 54     elif num2 <= 90:
 55         board[1][num2 - 81] = coin2
 56     elif num2 <= 100:
 57         board[0][100 - num2] = coin2
 58     for row in range(len(board)):
 59         print(*board[row])
 60     print('\n')
 61     board = create_board()
 62 def snakes_and_ladders():
 63     computer = 'c'
 64     user = 'u'
 65     print("\n\t\tWELCOME TO GAME OF SNAKES AND LADDERS\n\n")
 66     print("About the game:\n")
 67     print("It is played with dice between two players and here it will be wi    th user and computer\n")
 68     print("SNAKES : if you land on a number and it is prime go to the previo    us prime number\n")
 69     print("LADDER : if you land on a perfect square number, you will ladder     up by its square root of a number\n")
 70     print("Let's start the game\n")
 71     def check_snake_or_ladder(n):
 72         snakes = {11 : 9, 13 : 11, 17 : 13, 19 : 17, 23 : 19, 29 : 23, 31 :     29, 37 : 31, 41 : 37, 43 : 41, 47 : 43, 53 : 47, 59 : 53, 61 : 59, 67 : 61,     71 : 67, 73 : 71, 79 : 73, 83 : 79, 89 : 83, 97 : 89 }
 73         ladder = {4 : 6, 9 : 12, 16 : 20, 25 : 30, 36 : 42}
 74         if n in snakes.keys():
 75             print("Oops!it is a snake:")
 76             n = snakes[n]
 77         elif n in ladder.keys():
 78             print("Woah!it is a ladder.")
 79             n = ladder[n]
 80         return n
 81     def random_num():
 82         num = random.randint(1, 6)
 83         return num
 84     def roll_dice(pos):
 85         z = 0
 86         z = random_num()
 87         print("On dice:",z)
 88         pos = pos + z
 89         pos = check_snake_or_ladder(pos)
 90         return pos
 91     pos_1 = 0
 92     pos_2 = 0
 93     while pos_1 < 100 or pos_2 < 100:
 94         print("Turn of user")
 95         result = input("Press enter")
 96         if result == "" :
 97             pos_1 = roll_dice(pos_1)
 98             print ("Position of user is:",pos_1,",computer:",pos_2)
 99             print_board(pos_1, user, pos_2, computer)
100             if pos_1 > 99:
101                 print("\t\tUSER IS WINNER")
102                 break
103         print("Turn of computer")
104         pos_2 = roll_dice(pos_2)
105         print("Position of computer is:",pos_2,",user:",pos_1)
106         print_board(pos_1, user, pos_2, computer)
107         if pos_2 >99:
108             print("COMPUTER IS WINNER\n")
109             print("Better luck next time")
110             break
111 
112 snakes_and_ladders()

