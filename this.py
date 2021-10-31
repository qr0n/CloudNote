from db_handler import ldb
file = "subjects/test.json"

def aaa():
  ldb._append(k="test", v=["111", "112", "123"], f=file)
  if "111" in ldb._unappend(f=file)["test"]:
    print("found")
  else:
    print("no")
  
aaa()