import os
import re
from typing import List
from dictogram2 import Dictogram  # Assuming Dictogram is in the same directory


class MarkovGenerator:
    def __init__(self, order: int = 1):
        self.order = order
        self.dictogram = Dictogram(order=order)

    def read_file(self, file_name: str) -> List[str]:
        """
        Reads given source file and returns list of words
        """
        with open(file_name) as f:
            lines = f.readlines()
            words = []
            for line in lines:
                line = line.strip()  # Remove leading/trailing whitespace
                if line and not line.endswith(']'):  # Ignore empty lines and lines ending with ']'
                    line = line.replace("’", "'")
                    line_without_numbers = re.sub(r"\d+", "", line)  # Remove all numbers from the line
                    words.extend([match.group() for match in re.finditer(r"[a-zA-Z0-9_'.:,-;!?]+", line_without_numbers)])
                    words.append('\n')  # Add a line break after each line
            return words

    def process_directory(self, directory: str):
        """
        Processes all files in the given directory
        """
        all_words = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):  # Assuming the song lyrics are in .txt files
                    file_path = os.path.join(root, file)
                    words = self.read_file(file_path)
                    all_words.extend(words)
        self.dictogram = Dictogram(all_words, self.order)

    def create_dictogram(self, file_path: str):
        """
        Creates a histogram from the given file
        """
        words = self.process_directory(file_path)
        self.dictogram = Dictogram(words, self.order)

    def generate_lyrics(self, num_lines: int = 6) -> str:
        """
        Generate lyrics of a given number of lines using the dictogram
        """
        current_word_tuple = self.dictogram.sample_start()
        lyrics = list(current_word_tuple)
        line_count = 0

        # Generate the rest of the words
        while line_count < num_lines:
            next_word_tuple = self.dictogram.sample_next(current_word_tuple)
            lyrics.append(next_word_tuple[-1])  # Append the last word of the next word tuple
            current_word_tuple = next_word_tuple

            # If the last word is a line break, increment the line count
            if next_word_tuple[-1] == '\n':
                line_count += 1

        # Join the words into a string and return the lyrics
        return ' '.join(lyrics).replace(' \n ', '\n')


if __name__ == "__main__":
    generator = MarkovGenerator(order=2)
    generator.process_directory('data/songs/taylor_swift')  # Replace 'lyrics_directory' with the path to your directory of song lyrics
    lyrics = generator.generate_lyrics(num_lines=6)
    print(lyrics)
