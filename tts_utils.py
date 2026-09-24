import asyncio                       # Asynchronous I/O for concurrent programming
import edge_tts                      # Microsoft Edge TTS used for text-to-speech synthesis
import os                            # Operating system interface for file and directory operations
import pygame                        # Pygame library for multimedia applications, including audio playback

pygame.mixer.init()                  # Initialize the Pygame mixer module for audio playback

async def save_audio(text, path, voice="en-US-JennyNeural"):            # Asynchronous function to save audio from text using Microsoft Edge TTS
    communicate = edge_tts.Communicate(text, voice)                     # Create a Communicate object with the specified text and voice
    await communicate.save(path)                                        # Save the synthesized audio to the specified path


def play_audio(path):                                                      # Function to play audio from a specified file path
    pygame.mixer.music.load(path)                                          # Load the audio file into the Pygame mixer
    pygame.mixer.music.play()                                              # Play the loaded audio file

if __name__ == "__main__":                                              # If this script is run directly (not imported as a module)
    path = "test_output.mp3"                                            # Define the output file path for the audio
    asyncio.run(save_audio("Hello, this is a test.", path))             # Run the save_audio function with test text and output file path
    print("Audio saved -- playing now")                                 # Print a message indicating that the audio has been saved and will be played
    play_audio(path)                                                    # Play the generated audio file
    input("Press Enter to exit...")                                     # Wait for user input before exiting the program
    