print('The following events each take place in the Book of Acts. For each event, list the number of the chapter in which they appear. ')

import random
def ask_question(question, correct_answer):
    while True:
        answer = input(question + '').strip()
        if answer == correct_answer:
            print('Correct! ')
            break
        else: 
            print('Incorrect, try again ')
questions_and_answers = [
    ("Jesus ascends into heaven" , "1"),
    ("Matthias is chosen to fill the vacancy in the twelve left by Judas" , "1"),
    ("The Day of Pentecost takes place, in which the Spirit is poured out in abundance" , "2"),
    ("Peter teaches about baptism and the Gift of the Holy Ghost" , "2"),
    ("Peter and John heal a lame man at the temple" , "3"),
    ("Peter speaks of the restitution of all things" , "3"),
    ("Peter identifies Jesus as the prophet of whom Moses spoke" , "3"),
    ("Peter and John are arrested and testify of Christ to the council" , "4"),
    ("Ananias and Sapphira are killed because of their dishonesty" , "5"),
    ("Peter and John are delivered from prison by an angel" , "5"),
    ("Gamaliel, the Pharisee, counsels his brethren to let the apostles alone" , "5"),
    ("Seven men are called and set apart to assist the Twelve" , "6"),
    ("Stephen bears testimony, drawing parallels between Moses and Christ, and is stoned" , "7"),
    ("Simon seeks to purchase admittance to the office of the priesthood and is rebuked" , "8"),
    ("Philip teaches and baptizes an Ethiopian eunuch" , "8"),
    ("Saul sees Jesus on the road to Damascus and begins his ministry" , "9"),
    ("Peter heals Aeneas of palsy" , "9"),
    ("Peter raises Dorcas, also known as Tabitha, from the dead" , "9"),
    ("Peter has a vision in which he is commanded to take the gospel to the Gentiles" , "10"),
    ("Peter baptizes Cornelius and his household" , "10"),
    ("The disciples are first called Christians in Antioch" , "11"),
    ("Peter is confronted my men in Jerusalem for dining with Gentiles" , "11"),
    ("James is martyred by Herod" , "12"),
    ("Peter is delivered from prison for the second time" , "12"),
    ("Herod is smitten and dies for withholding the glory from God" , "12"),
    ("Paul curses a sorcerer with blindness" , "13"),
    ("Barnabas and Paul are mistaken for Jupiter and Mercury respectively after healing a cripple" , "14"),
    ("The apostles discuss whether all believers should be circumcised" , "15"),
    ("Paul and Silas are delivered from prison and convert their jailor" , "16"),
    ("Paul casts an evil spirit out of Lydia, the seller of purple" , "16"),
    ("Paul preaches in Athens about the unknown god" , "17"),
    ("Paul is brought before Gallio, who dismisses his case" , "18"),
    ("Paul baptizes and confirms former disciples of John the Baptist in Ephesus" , "19"),
    ("Certain craftsmen in Ephesus who build pagan shrines conspire against Paul" , "19"),
    ("Eutychus gets mad tired during a sermon and freaking dies. Paul revives him" , "20"),
    ("Paul predicts that the church will apostatize from within saying, 'Grievous wolves [shall] enter in among you'" , "20"),
    ("Paul is arrested and brought before the chief captain" , "21"),
    ("Paul recounts his conversion experience and bears testimony to the chief captain" , "22"),
    ("Paul appears before King Agrippa" , "26"),
    ("Paul travels toward Rome and is shipwrecked" , "27"),
    ("Paul is bitten by a viper and remains unharmed" , "28")
    ]

random.shuffle(questions_and_answers)

for question, correct_answer in questions_and_answers:
    ask_question(question, correct_answer)
print("\nCongratulations! You have completed the quiz.")