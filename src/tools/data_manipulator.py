import os
import csv

from bs4 import BeautifulSoup
 

def check_no_align(tag):
	return tag.name == "td" and not tag.has_attr("align")


def write_firstnames():
	with open("../data/raw/names.html", "r") as f:
		html_content = f.read()
		soup = BeautifulSoup(html_content, "html.parser")
		names_raw = soup.find_all(check_no_align)

		with open("../data/firstnames.csv", "a") as f2:
			for x in names_raw:
				x = str(x)
				x = x.replace("<td>", "").replace("</td>", "")
				f2.write(x + ";" + "USA" + "\n")


def add_country_to_csv(country_name):
	with open("../data/surnames.csv", "a"):
		pass


def format_table():
	with open("../data/surnames.csv", "r") as rf:
		with open("../data/surnames-target.csv", "w+") as tf:
			content = rf.readlines()

			for x in content:
				tab_index = x.find("\t")
				
				if tab_index != -1:
					tf.write(x[:tab_index] + ";USA,Canada" + "\n")


def remove_symbols():
	with open("../data/surnames.csv", "r") as rf:
		with open("../data/surnames-target.csv", "w+") as tf:
			content = rf.readlines()

			for x in content:
				tf.write(x.replace("()", ""))


def read_csv():
	with open("../data/raw/surnames-english.csv", "r") as f:
		with open("../data/surnames.csv", "a") as f2:
			csvf = csv.DictReader(f)

			for row in csvf:
				f2.write(row["name"] + ";USA,UK,Ireland,Scotland,Australia\n")


def make_rel_path(path: str) -> str:
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, path)


if __name__ == "__main__":
	read_csv()




