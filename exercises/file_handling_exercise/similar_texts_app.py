import os
from modules.text_processing_functions import check_text_similarity

def run():
    this_file_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_path)
    
    obama_speech_filepath = os.path.join(BASE_DIR, "files", "obama_speech.txt")
    michelle_obama_speech_filepath = os.path.join(BASE_DIR, "files", "michelle_obama_speech.txt")
    trump_speech_filepath = os.path.join(BASE_DIR, "files", "donald_speech.txt")
    melina_trump_speech_filepath = os.path.join(BASE_DIR, "files", "melina_trump_speech.txt")

    paths = [obama_speech_filepath, michelle_obama_speech_filepath, trump_speech_filepath, melina_trump_speech_filepath]

    _, _, sr1 = check_text_similarity(paths[0], paths[1])
    _, _, sr2 = check_text_similarity(paths[0], paths[2])
    _, _, sr3 = check_text_similarity(paths[0], paths[3])
    _, _, sr4 = check_text_similarity(paths[1], paths[2])
    _, _, sr5 = check_text_similarity(paths[1], paths[3])
    _, _, sr6 = check_text_similarity(paths[2], paths[3])

    print(f"Barak Obama and Michelle Obama's speeches have a similarity of {sr1*100}%")
    print(f"Barak Obama and Donald Trump's speeches have a similarity of {sr2*100}%")
    print(f"Barak Obama and Melina Trump's speeches have a similarity of {sr3*100}%")
    print(f"Michelle Obama and Donald Trump's speeches have a similarity of {sr4*100}%")
    print(f"Michelle Obama and Melina Trump's speeches have a similarity of {sr5*100}%")
    print(f"Donald Trump and Melina Trump's speeches have a similarity of {sr6*100}%")

if __name__ == "__main__":
    run()