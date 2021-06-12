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
	

if __name__ == "__main__":
	add_country_to_csv("USA")





