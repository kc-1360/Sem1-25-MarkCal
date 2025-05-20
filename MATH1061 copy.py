import math

Q1 = 0/1
Q2 = 0/1
Q3 = 0/1
Q4 = 0/1
Q5 = 0/1
Q6 = 0/1
Q7 = 0/1
Q8 = 0/1
Q9 = 0/1
Q10 = 0/1
QuizWeight = 0.01
QuizTotal = Q1 + Q2 + Q3+ Q4 + Q5 + Q6 + Q7 + Q8 + Q9 + Q10

Assign1 = 0/10
Assign1Weight = 0.05

Assign2 = 0/20
Assign2Weight = 0.1

MidSem = 0/12
MidSemWeight = 0.15

Final = 0/60
FinalWeight = 0.6

Attendace = 0/2
AttendaceWeight = 0.02


FinalMark = QuizTotal*QuizWeight + Assign1*Assign1Weight + Assign2*Assign2Weight + MidSem*MidSemWeight + Final*FinalWeight + Attendace * AttendaceWeight

if FinalMark < 0.5: 
    FinalLetterGrade = 'Fail'
elif FinalMark <= 0.64: 
    FinalLetterGrade = 'Pass'
elif FinalMark <= 0.74: 
    FinalLetterGrade = 'Credit'
elif FinalMark <= 0.84: 
    FinalLetterGrade = 'Distinction'
else: 
    FinalLetterGrade = 'High Distinction'

print(f'{(FinalMark*100):.0f}%, {FinalLetterGrade}')

ScaledTotal = 0

if Q1 != 0: 
    ScaledTotal += QuizWeight
if Q2 != 0: 
    ScaledTotal += QuizWeight
if Q3 != 0: 
    ScaledTotal += QuizWeight
if Q4 != 0: 
    ScaledTotal += QuizWeight
if Q5 != 0: 
    ScaledTotal += QuizWeight
if Q6 != 0: 
    ScaledTotal += QuizWeight
if Q7 != 0: 
    ScaledTotal += QuizWeight
if Q8 != 0: 
    ScaledTotal += QuizWeight
if Q9 != 0: 
    ScaledTotal += QuizWeight
if Q10 != 0: 
    ScaledTotal += QuizWeight
if Assign1 != 0: 
    ScaledTotal += Assign1Weight
if Assign2 != 0: 
    ScaledTotal += Assign2Weight
if MidSem != 0: 
    ScaledTotal += MidSemWeight
if Final != 0: 
    ScaledTotal += FinalWeight
if Attendace != 0: 
    ScaledTotal += AttendaceWeight

# Avoid divide-by-zero error
if ScaledTotal == 0:
    ScaledMark = 0
else:
    ScaledMark = FinalMark / ScaledTotal

if ScaledMark < 0.5: 
    ScaledLetterGrade = 'Fail'
elif ScaledMark <= 0.64: 
    ScaledLetterGrade = 'Pass'
elif ScaledMark <= 0.74: 
    ScaledLetterGrade = 'Credit'
elif ScaledMark <= 0.84: 
    ScaledLetterGrade = 'Distinction'
else: 
    ScaledLetterGrade = 'High Distinction'

print(f'{(ScaledMark*100):.0f}%, {ScaledLetterGrade}')\

RemainingScaling = 1 - ScaledTotal

if RemainingScaling == 0:
    print('Course Complete.')
    # no need to break if not in a loop
else:
    PassMin = (0.5 - (ScaledMark * ScaledTotal)) / RemainingScaling
    CreditMin = (0.65 - (ScaledMark * ScaledTotal)) / RemainingScaling
    DMin = (0.75 - (ScaledMark * ScaledTotal)) / RemainingScaling
    HDMin = (0.85 - (ScaledMark * ScaledTotal)) / RemainingScaling

    # Helper function to print messages
    def print_result(min_val, grade_name):
        if min_val > 1:
            print(f'It is impossible for you to get a {grade_name}.')
        elif min_val > 0:
            print(f'The Minimum Average you need to get a {grade_name} is {min_val * 100:.2f}%.')
        else:
            print(f'You are on track to get a {grade_name}!')

    print_result(PassMin, 'Pass')
    print_result(CreditMin, 'Credit')
    print_result(DMin, 'Distinction')
    print_result(HDMin, 'High Distinction')