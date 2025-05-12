# s = open('highscore.txt')
# score = int(s.read())
# def game():
#     return score
# y = int(input("Enter your score: "))
# s.close()
# t = open('highscore.txt','w')
# if y>score:
#     t.write(str(y))
#     t.close()
# else:
#     t.close()
# print("Updated!") ####Errors

def game():
    return 64

score = game()

with open('highscore.txt') as f:
    prevScore = f.read()

if prevScore=='':
    with open('highscore.txt','w') as f:
        f.write(str(score))

elif int(prevScore)<score:
    with open('highscore.txt','w') as f:
        f.write(str(score))
else:
    pass