from ocr import text_finder
logo_dimentions = {
    "width" : 1422-464,
    "height" : 851-636,
    "x" : 464,
    "y" : 636
}
with text_finder("Bluebook", False, "background_text") as found_text:
    print(found_text)
