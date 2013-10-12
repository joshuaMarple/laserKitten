import pygame, sys
from pygame.mixer import *
class music:
	def __init__(self):

		print pygame.mixer.music.get_volume()*100
		self.song1 = "./res/DST-2ndBallad.mp3"
		self.bossSong = "./res/DST-Cv-X.mp3"
		self.play(self.song1)


	def loadMusic(self, path):
		pygame.mixer.music.load(path)

	def play(self, song):
		pygame.mixer.music.load(song)
		pygame.mixer.music.play(-1, 0.1)

	def stop(self):
		pygame.mixer.music.stop()
		pygame.mixer.stop()
		pygame.mixer.quit()
	def bossSong(self):
		play("./res/DST-Cv-X.mp3")
	def levelSong(self):
		self.play("./res/DST-2ndBallad.mp3")