highest = -float("inf")

with open("books_and_chapters.txt") as books_and_chapters:
    input_group = input("Which volume of scritpure would you like to learn more about? ")

    for line in books_and_chapters:
        book, chapters, group = line.strip().split(":")
        chapters = int(chapters)

        if group.lower() == input_group.lower():
            if chapters > highest:
                highest = chapters
                highest_data = (book, chapters, group)

print(f"The book with the most chapters in {input_group} is {highest_data[0]} with {highest_data[1]} chapters.")



        

