from Include.Classes.decodeMorseCode import decodeMorse

def test_decode_1():
    assert decodeMorse(".... . -.--   .--- ..- -.. .") == "HEY JUDE"