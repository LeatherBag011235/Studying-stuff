import re

text = """**The Legend of Alexander**

In a world where power and intellect determine one’s destiny, Alexander emerged as an unparalleled force of wisdom and strength. From an early age, Alexander exhibited an insatiable curiosity for the hidden mechanics of the universe, spending countless hours deciphering ancient texts and pushing the boundaries of what was considered possible. Unlike others who sought greatness through sheer might, Alexander relied on intellect, strategy, and an unshakable will to carve a path that would forever alter history.

Born into a land riddled with conflict, Alexander was not destined for an easy life. Wars raged between warring factions, and alliances crumbled with every shifting tide. Yet, amidst the chaos, Alexander found solace in knowledge, gathering insights that would later shape the course of civilization itself. Masters of different disciplines sought out Alexander for guidance, realizing that this mind held the key to unprecedented advancements.

But greatness is never without its trials. When a formidable adversary emerged—one whose darkness threatened to consume everything—Alexander stood firm. Refusing to yield to tyranny, Alexander embarked on a journey to uncover the lost secrets of a civilization long forgotten. With every step, Alexander encountered enigmas only the sharpest mind could unravel, and through sheer determination, uncovered the truth that had been buried for centuries.

Armed with newfound knowledge and an unwavering resolve, Alexander returned to the battlefield, not as a conqueror, but as a beacon of hope. With a mastery of tactics that confounded even the most seasoned generals, Alexander led forces to a victory that was thought impossible. The world stood in awe as the tides of fate shifted, and at the center of it all stood a single figure—unwavering, resolute, and legendary.

But even legends must face their own fate. In the twilight of Alexander’s reign, the world had changed irreversibly. Knowledge was no longer a tool of the elite, but a gift shared among all. The adversaries who once threatened existence were vanquished, their names forgotten, while Alexander’s legacy endured beyond the pages of history.

And so, as the stars bore witness to the passage of time, the name of Alexander became more than just a memory. It became a symbol—an embodiment of wisdom, courage, and the relentless pursuit of truth. The world, forever transformed, stood as a testament to the journey of one who defied the odds and reshaped destiny itself.

The legend of Alexander would never fade, for as long as knowledge remained, so too would the story of the one who wielded it like a weapon against the darkness.

"""

# Replace all occurrences of "Alexander" with "Maxim"
updated_text = re.sub(r'\bAlexander\b', 'Maxim', text)

print(updated_text)

with open("legend_of_maxim.txt", "w", encoding="utf-8") as file:
    file.write(updated_text)

print("The modified text has been saved as 'legend_of_maxim.txt'.")
