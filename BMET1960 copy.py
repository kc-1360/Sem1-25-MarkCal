import math

W1 = 0/5
W2 = 0/5
W4 = 0/5
W5 = 0/5
W6 = 0/5
W7 = 0/5
W8 = 0/5
W9 = 0/5
W10 = 0/5
W11 = 0/5
QuizWeight = 0.015
QuizTotal = W1 + W2 + W4 + W5 + W6 + W7 + W8 + W9 + W10 + W11

EFT = 0/10
EFTWeight = 0.02

Final = 0/20
FinalWeight = 0.03

Arduino = 0/10
SW = 0/10
ENGSkillsWeight = 0.1
ENGSkillsTotal = Arduino + SW

Assign1 = 0/50
Assign1Weight = 0.15

Assign2 = 0/100
Assign2Weight = 0.15

Assign3 = 0/65
Assign3Weight = 0.2

TutPort = 0/10
TutPortWeight = 0.1

FinalMark = QuizTotal*QuizWeight + EFT*EFTWeight + ENGSkillsTotal*ENGSkillsWeight + Assign1*Assign1Weight + Assign2*Assign2Weight + Assign3*Assign3Weight +TutPort*TutPortWeight

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

if W1 != 0: 
    ScaledTotal += QuizWeight
if W2 != 0: 
    ScaledTotal += QuizWeight
if W4 != 0: 
    ScaledTotal += QuizWeight
if W5 != 0: 
    ScaledTotal += QuizWeight
if W6 != 0: 
    ScaledTotal += QuizWeight
if W7 != 0: 
    ScaledTotal += QuizWeight
if W8 != 0: 
    ScaledTotal += QuizWeight
if W9 != 0: 
    ScaledTotal += QuizWeight
if W10 != 0: 
    ScaledTotal += QuizWeight
if W11 != 0: 
    ScaledTotal += QuizWeight
if EFT != 0: 
    ScaledTotal += EFTWeight
if Final != 0: 
    ScaledTotal += FinalWeight
if Arduino != 0: 
    ScaledTotal += ENGSkillsWeight
if SW != 0: 
    ScaledTotal += ENGSkillsWeight
if Assign1 != 0: 
    ScaledTotal += Assign1Weight
if Assign2 != 0: 
    ScaledTotal += Assign2Weight
if Assign3 != 0: 
    ScaledTotal += Assign3Weight
if TutPort != 0: 
    ScaledTotal += TutPortWeight

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

print(f'{(ScaledMark*100):.0f}%, {ScaledLetterGrade}')

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