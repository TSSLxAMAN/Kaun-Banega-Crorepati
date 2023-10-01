def gameover(money):
    print(f"Opps wromg answer you won {money},\nBetter luck time....")
questions = [
    "What is the capital city of India?",
    "Which river is often referred to as the 'Ganga' in India?",
    "Who is known as the Father of the Indian Constitution?",
    "Which famous monument in India is often called the 'Symbol of Love'?",
    "What is the national bird of India?",
    "In which year did India gain independence from British colonial rule?",
    "Which Indian state is known as the 'Land of Five Rivers'?",
    "Who wrote the Indian national anthem, 'Jana Gana Mana'?",
    "Which famous Indian leader was assassinated by Nathuram Godse in 1948?",
    "What is the highest civilian award in India, often awarded for exceptional service to the nation?",
    "Which Indian state is known for the celebration of the Kumbh Mela?",
    "Who is the author of the book 'The Discovery of India'?",
    "What is the currency of India?",
    "Which Indian state is known as the 'Land of Five Rivers'?",
    "Who was the first woman Prime Minister of India?"
            ]
options = [
    ["A) New Delhi" "B) Mumbai", "C) Kolkata", "D) Chennai"],
    ["A) Brahmaputra", "B) Yamuna", "C) Godavari", "D) Indus"],
    ["A) Mahatma Gandhi", "B) Jawaharlal Nehru", "C) Bhagat Singh", "D) B.R. Ambedkar"],
    ["A) Red Fort", "B) Qutub Minar", "C) Hawa Mahal", "D) Taj Mahal"],
    ["A) Peacock", "B) Sparrow", "C) Pigeon", "D) Parrot"],
    ["A) 1942", "B) 1945", "C) 1947", "D) 1950"],
    ["A) Punjab", "B) Haryana", "C) Gujarat", "D) Rajasthan"],
    ["A) Rabindranath Tagore", "B) Bankim Chandra Chattopadhyay", "C) Sarojini Naidu", "D) Subhas Chandra Bose"],
    ["A) Sardar Patel", "B) Lal Bahadur Shastri", "C) Jawaharlal Nehru", "D) Mahatma Gandhi"],
    ["A) Padma Bhushan", "B) Bharat Ratna", "C) Padma Vibhushan", "D) Padma Shri"],
    ["A) West Bengal", "B) Rajasthan", "C) Uttar Pradesh", "D) Kerala"],
    ["A) Jawaharlal Nehru", "B) Subhas Chandra Bose", "C) Bhagat Singh", "D) Sardar Patel"],
    ["A) Rupee", "B) Rupiah", "C) Taka", "D) Yen"],
    ["A) Punjab", "B) Haryana", "C) Gujarat", "D) Rajasthan"],
    ["A) Indira Gandhi", "B) Sonia Gandhi", "C) Priyanka Gandhi", "D) Mamata Banerjee"] 
        ]
correct_answers = ['A','B','D','D','A','C','A','A','D','B','C','A','A','A','A']
prizemoney = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,70000000]
print('''Welcome to KAUN BANEGA CROREPATI
      RULES : 
      1. THERE WILL BE 15 QUESTION
      2. YOU WILL RECIEVE A SPECIFIC AMOUNT OF MONEY AFTER ANSWERING EVERY RIGHT ANSWER 
      3. IF ANY WRONG ANSWER GIVEN AT ANY POINT OF GAME THE GAME WILL QUIT WITH THE AMOUNT YOU WIN.
      4. PLEASE INPUT THE CORRECT OPTIONS IN A,B,C,D FORMAT''')
money = 0

for i in range (1,16):
    print(f"Question {i} : {questions[i-1]}")
    print(f"{options[i-1]}")
    userinput = input("Enter your option : ")
    if userinput.upper() == correct_answers[i - 1]:
        money = money + prizemoney[i-1]
        print(f'''RIGHT ANSWER!!!
              YOU WON {money}
            WELL PLAYED NOW WE MOVE ON TO THE NEXT QUESTION''')
    else:
        gameover(money)
        break

