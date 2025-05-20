import math

W2 = 0/10
W3 = 0/10
W4 = 0/10
W5 = 0/10
W6 = 0/10
W7 = 0/10
W8 = 0/8
W9 = 0/10
W10 = 0/10
W11 = 0/10
W12 = 0/10
W13 = 0/10
QuizWeight = 0.01
QuizList = [W2, W3, W4, W5, W6, W7, W8, W9, W10, W11, W12, W13]
QuizList.sort()
QuizCounted = QuizList[-10:]  # Highest 10 quizzes
QuizTotal = sum(QuizCounted)

Proj1 = 0/100
Proj1Weight = 0.1

Proj2 = 0/100
Proj2Weight = 0.1

GCPresi = 0/100
GCPresiWeight = 0.05

GCReport = 0/100
GCReportWeight = 0.15

Final = 0/100
FinalWeight = 0.5

FinalMark = QuizWeight * QuizTotal + Proj1 * Proj1Weight + Proj2 * Proj2Weight + GCPresi * GCPresiWeight + GCReport * GCReportWeight + Final * FinalWeight


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

if QuizCounted != 0: 
    ScaledTotal += QuizWeight*10
if Proj1 != 0: 
    ScaledTotal += Proj1Weight
if Proj2 != 0: 
    ScaledTotal += Proj2Weight
if GCPresi != 0: 
    ScaledTotal += GCPresiWeight
if GCReport != 0: 
    ScaledTotal += GCReportWeight
if Final != 0: 
    ScaledTotal += FinalWeight

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