from brain.emotion import detect_emotion
from brain.responde import generate_response

print("SAHARA is starting...")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("SAHARA: Goodbye!")
        break

    emotion = detect_emotion(user_input)
    response = generate_response(emotion)

    print("Emotion:", emotion)
    print("SAHARA:", response)