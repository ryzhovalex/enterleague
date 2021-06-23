"""
Generation engine of players, clubs and events.
"""

import os
import csv


class Generator:
	def __init__(self, db):
		self.db = db

	def generate_countries(self, Country: type) -> None:
		with open(self._make_rel_path("data/countries.csv"), "r") as file:
			csvf = csv.DictReader(file, delimiter=";")	
			
			for row in csvf:
				assert row["prototype"]

				self.db.session.add(Country(name=row["name"], prototype=row["prototype"]))
				print("Country %s with prototype %s added!" % (row["name"], row["prototype"]))
			
			self.db.session.commit()
	
	@staticmethod
	def _make_rel_path(path: str) -> str:
		script_dir = os.path.dirname(__file__)
		return os.path.join(script_dir, path)


			

			


			