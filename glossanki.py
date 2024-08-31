from deep_translator import GoogleTranslator


if __name__ == "__main__":
  print("gloss-anki start")
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
          except ValueError:
            pass
        # print(line.rstrip())

      if "Jun 30" in line:
        break
