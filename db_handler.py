import httpx
import os
import json

url = "https://db.infinityiron.xyz/api/{}".format(os.environ['pkey'])
pull_pack = "https://db.infinityiron.xyz/packages"

class db:
  @staticmethod
  def store(k, v, f):
    r = httpx.get(f"{url}/store?key={k}&value={v}&file={f}")
    return r.text
  
  @staticmethod
  def delete(k):
    r = httpx.get(f"{url}/del?key={k}&file=notes")
    return r.text
  
  @staticmethod
  def delete_db(f):
    r = httpx.get(f"{url}/delete_db?file={f}")
    return r.text
  
  @staticmethod
  def create_db(f):
    r = httpx.get(f"{url}/create_db?file={f}")
    return r.text
  
  @staticmethod
  def render():
    r = httpx.get(f"{url}/list?file=notes")
    return r.text

  @staticmethod
  def key_focus(k, f):
    r = httpx.get(f"{url}/get?key={k}&file={f}")
    return r.text
  
  @staticmethod
  def pull(package, app):
    r = httpx.get(f"{pull_pack}?p={package}&app_id={app}")
    with open(f"packages/{package}.py", "w") as E:
      E.write(r.text)
      return print(f"{package} has been added successfully!")

class ldb:
  @staticmethod
  def _append(k, v, f):
    """Appends the user to a JSON file with the scopes"""
    with open(f, "r") as E:
      lE = json.load(E)
      lE[k] = v
    with open(f, "w") as E:
      json.dump(lE, E)
  
  @staticmethod
  def _unappend(f):
    """Unappends the user to handle :name:, :password:, :ID:, :etc:"""
    with open(f, "r") as E:
      lE = json.load(E)
      return dict(lE)
  
  @staticmethod
  def _kf(k, f):
    try:
      return ldb._unappend(f)[k]
    except KeyError:
      return "N"

class render:
  @staticmethod
  def online():
    with os.scandir('/home/runner/db/cdn') as i:
      return [entry.name for entry in i]