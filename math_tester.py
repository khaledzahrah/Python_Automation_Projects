import pyinputplus as pyip
import time , random
numberOfQuestions=3
correctAnswer=0
for questionNumber in range(numberOfQuestions):
    Num1=random.randint(0,9)
    Num2=random.randint(0,9)
    prompt=f"questionNumber  {questionNumber+1} what is : {Num1 }*{Num2} =\n"
    try:
        response=pyip.inputStr(prompt , allowRegexes=[f'^{Num1*Num2}$'] , blockRegexes=[('.*', 'لا يصلح')] , limit=2,
    timeout=5)
    except pyip.TimeoutException:
        print('انتهى الوقت!')
    except pyip.RetryLimitException:
        print('نفدت المحاولات!')
    else:
        print('إجابة صحيحة!')
        correctAnswer+= 1
print(f': لديك {correctAnswer} من {numberOfQuestions} correcrt  ')


