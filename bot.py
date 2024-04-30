import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["흥미롭네요, 자세히 말해주세요.",
                    "알겠습니다, 계속하세요.",
                    "왜 그렇게 생각하시나요?",
                    "이상한 날씨입니다. 그렇지 않나요?",
                    "다른 얘기 하실까요?",
                    "어제 게임 이기셨나요?"]

print("안녕하세요 저는 마빈입니다. 간단한 로봇입니다.")
print("'잘가'라고 말하면 대화를 종료합니다.")
print("대답을 한 후에 'enter'를 누르세요")
print("안녕하세요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "잘가":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("좋은 대화였어요. 안녕히 가세요")
