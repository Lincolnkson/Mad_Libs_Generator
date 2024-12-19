# Prompt the user for different words
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
animal = input("Enter the name of an animal: ")
verb_past_tense = input("Enter a verb in past tense: ")
place = input("Enter the name of a place: ")
emotion = input("Enter an emotion (e.g., happy, sad): ")

# Build the story
story = f"On a beautiful {adjective1} day, I went to the {place}. I saw a funny {adjective2} {animal} {verb_past_tense} from the trees. "
story += f"Then, I spotted a majestic {adjective3} lion lounging in the sun. It made me feel so {emotion}!"

# Add some conditional twists based on the user's inputs
if adjective1 == "rainy" or adjective1 == "stormy":
    story += " Luckily, I brought my umbrella to stay dry."
elif adjective1 == "sunny" or adjective1 == "bright":
    story += " I was glad I wore sunglasses because it was so bright!"

if emotion.lower() == "scared":
    story += " It was a thrilling experience that I'll never forget!"
elif emotion.lower() == "excited":
    story += " This adventure filled me with energy for the rest of the day!"

# Display the final story
print("\nHere is your Mad Libs story:\n")
print(story)
