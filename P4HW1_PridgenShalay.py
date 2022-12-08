# CTI-110
# P4HW1 - Score List
# Shalay Pridgen 
# 16 Nov 2022
#

#input


Scoreslist = []
numScores = int(input("How many numbers do you want to enter? "))
current_numScores = 0

#process
while True:
    while(current_numScores < numScores):
        scores = float(input('Enter score #{}: '.format(current_numScores + 1)))
        while True:
            if (scores<0 or scores>100):
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(current_numScores + 1)))
                
            else:
                Scoreslist.append(scores)
                break
        current_numScores += 1

    if(current_numScores==numScores):
        break


minScore = min(Scoreslist)
Scoreslist.remove(min(Scoreslist))
average = sum(Scoreslist) / len(Scoreslist)

if(average>=93 and average<=100):
    grade = 'A'

elif(average>=90 and average<=92.9):
    grade = 'B+'
    
elif(average>=87 and average<=89.9):
    grade = 'B'
    
elif(average>=83 and average<=86.9):
    grade = 'B-'
    
elif(average>=80 and average<=82.9):
    grade = 'C+'
    
elif(average>=77 and average<=79.9):
    grade = 'C'
    
elif(average>=73 and average<=76.9):
    grade = 'C-'
    
elif(average>=70 and average<=72.9):
    grade = 'D+'
    
elif(average>=67 and average<=69.9):
    grade = 'D'
    
elif(average>=60 and average<=66.9):
    grade = 'D-'
    
elif(average<59.9):
    grade = 'F'


#output

print('-----------Results----------')
print("{:25}{:<5}".format("Lowest Score:",minScore))
print("{:25}{:<5}".format("Modified List:",f'{Scoreslist}'))
print("{:25}{:<5}".format("Scores Average:",average ))
print("{:25}{:<5}".format("Grade:",grade))
print('----------------------------')
                   
