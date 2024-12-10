import json



def create_file() -> None:
  with open("funnel.csv", "w+") as file:
    file.write("")



def add_line(line: str) -> None:
  with open("funnel.csv", "a+") as file:
    file.write(f"{line}\n")



def get_purchase_log() -> dict:
  purchases = {}
  with open("purchase_log.txt", "r") as file:
    for line in file:
      purchase = json.loads(line)
      purchases[purchase["user_id"]] = purchase["category"]
  return purchases



def write_to_funnel() -> None:
  purchases = get_purchase_log()
  with open("visit_log.csv", "r") as file:
    for line in file:
      parts = line.split(',')
      if parts[0] in purchases:
        new_line=f"{line.rstrip()},{purchases[parts[0]]}"
        add_line(new_line)



def print_results() -> None:
  with open("funnel.csv", "r") as file:
    for line in file:
      print(f"{line.rstrip()}")



def main() -> None:
  create_file()
  write_to_funnel()
  print_results()



main()
