def generate_apa_book(author_last, author_initials, year, title, publisher, location=""):
    """Generate an APA citation for a book."""
    citation = f"{author_last}, {author_initials}. ({year}). *{title}*. {location}{publisher}."
    return citation

def generate_apa_article(author_last, author_initials, year, title, journal, volume, issue="", pages=""):
    """Generate an APA citation for a journal article."""
    issue_str = f"({issue})" if issue else ""
    citation = f"{author_last}, {author_initials}. ({year}). {title}. *{journal}, {volume}{issue_str}*, {pages}."
    return citation

def main():
    print("Welcome to the APA Citation Generator!")
    citations = []  # Store citations (CRUD - Read/Delete)

    while True:
        print("\nOptions:")
        print("1. Create a book citation")
        print("2. Create a journal article citation")
        print("3. View all citations")
        print("4. Delete a citation")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Book citation input
            author_last = input("Enter author's last name: ")
            author_initials = input("Enter author's initials (e.g., A. B.): ")
            year = input("Enter publication year: ")
            title = input("Enter book title: ")
            publisher = input("Enter publisher: ")
            location = input("Enter publisher location (optional, press Enter to skip): ")
            citation = generate_apa_book(author_last, author_initials, year, title, publisher, location)
            citations.append(citation)
            print("\nGenerated Citation:")
            print(citation)

        elif choice == "2":
            # Journal article citation input
            author_last = input("Enter author's last name: ")
            author_initials = input("Enter author's initials (e.g., A. B.): ")
            year = input("Enter publication year: ")
            title = input("Enter article title: ")
            journal = input("Enter journal name: ")
            volume = input("Enter volume number: ")
            issue = input("Enter issue number (optional, press Enter to skip): ")
            pages = input("Enter page range (e.g., 45-67): ")
            citation = generate_apa_article(author_last, author_initials, year, title, journal, volume, issue, pages)
            citations.append(citation)
            print("\nGenerated Citation:")
            print(citation)

        elif choice == "3":
            # View all citations
            if citations:
                print("\nYour Citations:")
                for i, cite in enumerate(citations, 1):
                    print(f"{i}. {cite}")
            else:
                print("No citations yet.")

        elif choice == "4":
            # Delete a citation
            if citations:
                print("\nYour Citations:")
                for i, cite in enumerate(citations, 1):
                    print(f"{i}. {cite}")
                del_index = int(input("Enter the number of the citation to delete (1-{}): ".format(len(citations)))) - 1
                if 0 <= del_index < len(citations):
                    citations.pop(del_index)
                    print("Citation deleted.")
                else:
                    print("Invalid number.")
            else:
                print("No citations to delete.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
