
#1. Search algorithms
#Searching is the most rudimentary form of artificial intelligence. 
#To be fair, there are differences between machine learning and 
#artificial intelligence but lets avoid those for now 
#and instead focus on the topic of algorithms that make the chat bot talk intelligently.
#Search is a crucial part of how a chat bot quickly and 
#efficiently retrieves the possible candidate statements that it can respond with.
#Some examples of attributes that help the chat bot select a response include
# * the similarity of an input statement to known statements
# * the frequency in which similar known responses occur
# * the likeliness of an input statement to fit into a category that known statements are a part of

#2. Classification algorithms
#Several logic adapters in ChatterBot use naive Bayesian classification algorithms to determine
#if an input statement meets a particular set of criteria that warrant a response to be generated
#from that logic adapter.
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from PIL import ImageTk, Image

bot = ChatBot("Ice Bear")
main = Tk()
main.geometry("400x600")
main.configure(background="black")
main.title("Ice Bear")

# Resize the image
img = Image.open("AIML_Bear.jpg")
img = img.resize((600, 400), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

photoL = Label(main, image=img)
photoL.pack(pady=5)

def bear_answer():
    query=textF.get()
    bear_answer=bot.get_response(query)
    msgs.insert(END, "You : " + query)
    msgs.insert(END, "Ice_Bear : " + str(bear_answer))
    textF.delete(0,END)
    msgs.yview(END)
  
frame=Frame(main)
scroll=Scrollbar(frame)
msgs=Listbox(frame,width=100,height=10,yscrollcommand=scroll.set)
scroll.pack(fill=Y,side=RIGHT)
msgs.configure(background="white")
msgs.pack(fill=BOTH,side=LEFT,pady=20)

frame.pack()
#text entry

textF=Entry(main,font=("Arial",20))
textF.pack(fill=X,pady=10)

btn=Button(main,text="ASK BEAR",font=("Arial",20), command=bear_answer)
btn.pack()
main.mainloop()





bot = ChatBot("Ice Bear")

convo = animal_dataset = ["Hello","HI","hi","how are you","how may i help you","My name is AnimaleXpert","Bye","good day",
    
    "Tigers", "Tigers are the largest cats in the world and are known for their distinctive orange fur with black stripes. They are excellent swimmers and can leap distances of up to 30 feet in a single jump.",
    "Elephants", "Elephants are the largest land animals and have a highly developed brain. They are known for their long trunks, which they use for breathing, drinking, and grabbing objects. Elephants also have a strong sense of social bonding and live in close-knit family groups.",
    "Dolphins", "Dolphins are highly intelligent marine mammals known for their playful behavior and social nature. They communicate using a series of clicks, whistles, and body movements. Dolphins are also known for their acrobatic displays and can swim at speeds of up to 20 miles per hour.",
    "Penguins", "Penguins are flightless birds that live in the Southern Hemisphere. They have a unique way of getting around by sliding on their bellies over ice and snow. Penguins are excellent swimmers and can dive to great depths in search of food.",
    "Lions", "Lions are majestic big cats known for their impressive manes. They are highly social animals and live in groups called prides. Lions are skilled hunters and work together in coordinated attacks to bring down prey.",
    "Giraffes", "Giraffes are the tallest land animals and have long necks that allow them to reach leaves and shoots in tall trees. They have a unique patterned coat and use their long tongues to feed on vegetation.",
    "Kangaroos", "Kangaroos are marsupials found in Australia. They are known for their powerful hind legs, which enable them to hop at high speeds and cover large distances. Kangaroos also have a pouch where they carry and nurse their young called joeys.",
    "Cheetahs", "Cheetahs are the fastest land animals, capable of reaching speeds up to 70 miles per hour in short bursts. They have a slender body, distinctive black tear stripes on their face, and are excellent hunters.",
    "Hummingbirds", "Hummingbirds are the smallest birds in the world and are capable of hovering in mid-air due to their rapid wing beats. They have vibrant feathers and consume nectar from flowers using their long beaks.",
    "Gorillas", "Gorillas are the largest primates and share about 98 percent of their DNA with humans. They are herbivores and live in groups called troops. Gorillas are known for their strength and gentle nature.",
    "Whales", "Whales are the largest animals on Earth and are found in oceans around the world. They are known for their spectacular breaching behavior and complex communication using songs and vocalizations.",
    "Sharks", "Sharks are apex predators in the ocean and have been around for millions of years. They have a keen sense of smell and electroreceptors to detect prey. Sharks play a crucial role in maintaining the balance of marine ecosystems.",
    "Owls", "Owls are nocturnal birds of prey known for their silent flight and exceptional night vision. They have specialized feathers that allow them to fly silently and capture prey in complete darkness.",
    "Crocodiles", "Crocodiles are large, aquatic reptiles found in tropical regions. They have a powerful bite and are well adapted for life in water. Crocodiles have been around for millions of years and are often considered living dinosaurs.",
    "Butterflies", "Butterflies are beautiful insects known for their vibrant colors and delicate wings. They undergo a remarkable transformation from caterpillar to butterfly through a process called metamorphosis.",
    "Octopuses", "Octopuses are intelligent marine creatures with soft bodies and multiple arms. They have the ability to change color and shape, allowing them to camouflage and escape from predators. Octopuses are also skilled hunters and problem solvers.",
    "Polar Bears", "Polar bears are large bears that inhabit the Arctic regions. They have a thick layer of blubber and a dense fur coat to withstand the extreme cold. Polar bears are excellent swimmers and primarily feed on seals.",
    "Eagles", "Eagles are large birds of prey known for their keen eyesight and powerful talons. They are skilled hunters and can soar at great heights in search of prey. Eagles are symbols of strength and freedom in many cultures.",
    "Snakes", "Snakes are elongated, legless reptiles found in various habitats around the world. They use their forked tongues to sense their surroundings and capture prey. Snakes play important roles in ecosystems as both predator and prey.",
    "Bees", "Bees are flying insects known for their role in pollination and honey production. They live in organized colonies and have a highly developed system of communication through dance movements.",
    "Wolves", "Wolves are social animals that live and hunt in packs. They have a complex communication system and work together to take down prey. Wolves are highly adaptable and can be found in a variety of habitats.",
    "Komodo Dragons", "Komodo dragons are the largest lizards on Earth and are found in the Indonesian islands. They have a venomous bite and powerful jaws, making them formidable predators. Komodo dragons also have a keen sense of smell to locate prey.",
    "Jellyfish", "Jellyfish are gelatinous creatures that live in marine waters. They have tentacles armed with stinging cells used to capture prey. Jellyfish come in a variety of shapes and sizes, and some species are bioluminescent.",
    "Ants", "Ants are social insects that live in organized colonies. They have a highly structured society with different roles for each member. Ants are known for their strength and ability to work together to accomplish tasks.",
    "Pandas", "Pandas are iconic black and white bears native to China. They primarily feed on bamboo and have a unique thumb-like structure that helps them grasp bamboo stalks. Pandas are endangered and conservation efforts are in place to protect them.",
    "Bats", "Bats are the only mammals capable of sustained flight. They are nocturnal animals and use echolocation to navigate and locate prey. Bats play a vital role in pollination and insect control.",
    "Komodo Dragons", "Komodo dragons are the largest lizards on Earth and are found in the Indonesian islands. They have a venomous bite and powerful jaws, making them formidable predators. Komodo dragons also have a keen sense of smell to locate prey.",
    "Jellyfish", "Jellyfish are gelatinous creatures that live in marine waters. They have tentacles armed with stinging cells used to capture prey. Jellyfish come in a variety of shapes and sizes, and some species are bioluminescent.",
    "Ants", "Ants are social insects that live in organized colonies. They have a highly structured society with different roles for each member. Ants are known for their strength and ability to work together to accomplish tasks.",
    "Pandas", "Pandas are iconic black and white bears native to China. They primarily feed on bamboo and have a unique thumb-like structure that helps them grasp bamboo stalks. Pandas are endangered and conservation efforts are in place to protect them.",
    "Bats", "Bats are the only mammals capable of sustained flight. They are nocturnal animals and use echolocation to navigate and locate prey. Bats play a vital role in pollination and insect control.",
    "Horses", "Horses are large, majestic animals known for their speed, strength, and endurance. They have been domesticated for thousands of years and have played a significant role in human history and development.",
    "Chameleons", "Chameleons are unique reptiles known for their ability to change color. They do so to communicate, regulate body temperature, and camouflage. Chameleons have long, sticky tongues to capture insects as their main food source.",
    "Rhinoceroses", "Rhinoceroses are massive herbivores with a horn on their noses. They are known for their armor-like skin and are critically endangered due to illegal hunting for their horns.",
    "Platypuses", "Platypuses are unusual mammals found in Australia. They have a duck-billed snout, webbed feet, and lay eggs. Platypuses are semiaquatic and primarily feed on small invertebrates.",
    "Sloths", "Sloths are slow-moving mammals found in the rainforests of Central and South America. They have a unique lifestyle, spending most of their time hanging upside down from trees. Sloths move so slowly that algae can grow on their fur.",
    "Gazelles", "Gazelles are slender antelopes found in Africa and Asia. They are known for their speed and agility, allowing them to escape from predators. Gazelles have excellent vision and are capable of leaping great distances.",
    "Camels", "Camels are large mammals adapted to desert environments. They have humps on their backs that store fat reserves, allowing them to survive for long periods without water. Camels are well-suited for travel in arid regions and are often referred to as the 'ships of the desert'.",
    "Humpback Whales", "Humpback whales are large marine mammals known for their spectacular breaching displays and haunting songs. They undertake long migrations each year and are known for their acrobatic behaviors in the water.",
    "Fireflies", "Fireflies are insects known for their bioluminescent ability. They produce light through a chemical reaction in their bodies, which is used to attract mates. Firefly displays are often seen during warm summer nights.",
    "Orangutans", "Orangutans are large apes found in the rainforests of Borneo and Sumatra. They are highly intelligent and have a remarkable ability to use tools. Orangutans are critically endangered due to habitat loss and illegal hunting.",
    "Peacocks", "Peacocks are large birds known for their strikingly beautiful plumage. Male peacocks display their colorful tail feathers in elaborate courtship displays to attract females. Peacocks are native to South Asia but are now found in many parts of the world.",
    "Chimpanzees", "Chimpanzees are intelligent primates and are our closest living relatives. They have complex social structures and use tools for various purposes, such as extracting termites from mounds. Chimpanzees also exhibit advanced problem-solving skills.",
    "Flamingos", "Flamingos are tall, wading birds known for their vibrant pink feathers and long, slender necks. They live in large colonies and perform synchronized displays during courtship. Flamingos have a unique filtering system in their beaks to extract small organisms from water and mud.",
    "Starfish", "Starfish, also known as sea stars, are marine invertebrates with a distinct star-shaped body. They have the ability to regenerate lost limbs and can even regenerate into complete individuals from a single severed arm.",
    "Koalas", "Koalas are marsupials native to Australia. They are known for their cuddly appearance, eucalyptus diet, and low energy levels. Koalas spend most of their time sleeping or resting in trees.",
    "Komodo Dragons", "Komodo dragons are the largest lizards on Earth and are found in the Indonesian islands. They have a venomous bite and powerful jaws, making them formidable predators. Komodo dragons also have a keen sense of smell to locate prey.",
    "Jellyfish", "Jellyfish are gelatinous creatures that live in marine waters. They have tentacles armed with stinging cells used to capture prey. Jellyfish come in a variety of shapes and sizes, and some species are bioluminescent.",
    "Ants", "Ants are social insects that live in organized colonies. They have a highly structured society with different roles for each member. Ants are known for their strength and ability to work together to accomplish tasks.",
    "Pandas", "Pandas are iconic black and white bears native to China. They primarily feed on bamboo and have a unique thumb-like structure that helps them grasp bamboo stalks. Pandas are endangered and conservation efforts are in place to protect them.",
    "Bats", "Bats are the only mammals capable of sustained flight. They are nocturnal animals and use echolocation to navigate and locate prey. Bats play a vital role in pollination and insect control.",
    "Horses", "Horses are large, majestic animals known for their speed, strength, and endurance. They have been domesticated for thousands of years and have played a significant role in human history and development.",
    "Chameleons", "Chameleons are unique reptiles known for their ability to change color. They do so to communicate, regulate body temperature, and camouflage. Chameleons have long, sticky tongues to capture insects as their main food source.",
    "Rhinoceroses", "Rhinoceroses are massive herbivores with a horn on their noses. They are known for their armor-like skin and are critically endangered due to illegal hunting for their horns.",
    "Platypuses", "Platypuses are unusual mammals found in Australia. They have a duck-billed snout, webbed feet, and lay eggs. Platypuses are semiaquatic and primarily feed on small invertebrates.",
    "Sloths", "Sloths are slow-moving mammals found in the rainforests of Central and South America. They have a unique lifestyle, spending most of their time hanging upside down from trees. Sloths move so slowly that algae can grow on their fur.",
    "Gazelles", "Gazelles are slender antelopes found in Africa and Asia. They are known for their speed and agility, allowing them to escape from predators. Gazelles have excellent vision and are capable of leaping great distances.",
    "Camels", "Camels are large mammals adapted to desert environments. They have humps on their backs that store fat reserves, allowing them to survive for long periods without water. Camels are well-suited for travel in arid regions and are often referred to as the 'ships of the desert'.",
    "Humpback Whales", "Humpback whales are large marine mammals known for their spectacular breaching displays and haunting songs. They undertake long migrations each year and are known for their acrobatic behaviors in the water.",
    "Fireflies", "Fireflies are insects known for their bioluminescent ability. They produce light through a chemical reaction in their bodies, which is used to attract mates. Firefly displays are often seen during warm summer nights.",
    "Orangutans", "Orangutans are large apes found in the rainforests of Borneo and Sumatra. They are highly intelligent and have a remarkable ability to use tools. Orangutans are critically endangered due to habitat loss and illegal hunting.",
    "Peacocks", "Peacocks are large birds known for their strikingly beautiful plumage. Male peacocks display their colorful tail feathers in elaborate courtship displays to attract females. Peacocks are native to South Asia but are now found in many parts of the world.",
    "Chimpanzees", "Chimpanzees are intelligent primates and are our closest living relatives. They have complex social structures and use tools for various purposes, such as extracting termites from mounds. Chimpanzees also exhibit advanced problem-solving skills.",
    "Flamingos", "Flamingos are tall, wading birds known for their vibrant pink feathers and long, slender necks. They live in large colonies and perform synchronized displays during courtship. Flamingos have a unique filtering system in their beaks to extract small organisms from water and mud.",
    "Starfish", "Starfish, also known as sea stars, are marine invertebrates with a distinct star-shaped body. They have the ability to regenerate lost limbs and can even regenerate into complete individuals from a single severed arm.",
    "Koalas", "Koalas are marsupials native to Australia. They are known for their cuddly appearance, eucalyptus diet, and low energy levels. Koalas spend most of their time sleeping or resting in trees."
]






trainer = ListTrainer(bot)

# now training the bot with the help of trainer
trainer.train(convo)
print("Talk to bot ")
while True:
    query = input("You : ")
    if query == 'exit':
        break
    answer = bot.get_response(query)
    print("Ice Bear : ", answer)
