def word_count(text: str) -> int:
    return len(text.split())

def character_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for char in text:
        lowercase_char = char.lower()
        counts[lowercase_char] = counts.get(lowercase_char, 0) + 1
    return counts


def sort_on(item: tuple[str, int]) -> int:
    return item[1]


def chars_dict_to_sorted_list(character_counts: dict[str, int]) -> list[tuple[str, int]]:
    sorted_characters = []  # list of tuples
    for char in character_counts: #running through the dictionary
        count = character_counts[char] #getting the character
        sorted_characters.append((char, count)) #now what is that chacters count and appending it to the list
    return sorted(sorted_characters, key=sort_on, reverse=True) #now sort from biggest to least
