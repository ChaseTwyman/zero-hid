from ocr import text_finder
from move_mouse import Move_mouse
logo_dimentions = {
    "width" : 1422-464,
    "height" : 851-636,
    "x" : 464,
    "y" : 636
}
with text_finder("Bluebook", False, "background") as found_text:
    for i in range(0,len(found_text[0])):
        if "bluebook" == found_text[0][i].lower():
            print(found_text[1][i])
            with Move_mouse(found_text[1][i][2]+found_text[1][i][0]/2, found_text[1][i][3]+found_text[1][i][1]/2) as m: {}