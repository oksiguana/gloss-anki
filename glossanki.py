from deep_translator import GoogleTranslator
import genanki

if __name__ == "__main__":
  print("gloss-anki start")

  # efine a Unique Model (Card Template)
  my_model = genanki.Model(
    1607392319,  # Unique ID for the model
    'Simple Model',  # Model name
    fields=[
      {'name': 'Question'},
      {'name': 'Answer'},
    ],
    templates=[
      {
        'name': 'Card 1',
        'qfmt': '{{Question}}',  # Question template (front of the card)
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',  # Answer template (back of the card)
      },
    ])

  # Create the Deck
  my_deck = genanki.Deck(
    2059400110,  # Unique deck ID
    'English Aug 27 - Jun 30')  # Deck name

  filename = "C:\\Users\\chuwi\\Documents\\Projects\\gloss-anki\\testdata\\takeout-20240829T092105Z-001\\Takeout\\My Activity\\Google Translate\\MyActivity.html"
  with open(filename,"r", encoding="utf-8") as file:
    # start date: Aug 27
    # end date: Jun 30
    start_date_met = ''
    for line in file:
      if "Aug 27" in line:
        start_date_met = True

      if start_date_met:
        arr = line.split(">&quot;")
        for data_line in arr:
          try:
            data_index = data_line.index("&quot;<", )
            question = data_line[:data_index]
            translated = GoogleTranslator(source='en', target='ru').translate(question)
            print(f"{question} - {translated}")
            # Add Notes (Flashcards)
            note1 = genanki.Note(
              model=my_model,
              fields=[question, translated])

            # Add the notes (cards) to the deck
            my_deck.add_note(note1)
          except ValueError:
            pass
        # print(line.rstrip())

      if "Jun 30" in line:
        break


  # Export the Deck to a File
  genanki.Package(my_deck).write_to_file('output.apkg')

  print("Deck created successfully: 'output.apkg'")