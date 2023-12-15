import requests
import json
import xlrd

# Definisikan konstanta

BASE_URL = None

# Definisikan fungsi untuk mendapatkan hasil voting

def get_results():
  book = xlrd.open_workbook("voting.xlsx")
  sheet = book.sheet_by_name("Sheet1")
  results = []
  for row in range(sheet.nrows):
    candidate_id = sheet.cell_value(row, 0)
    votes = sheet.cell_value(row, 1)
    results.append({
      "candidate_id": candidate_id,
      "votes": votes
    })
  return results

# Definisikan fungsi untuk memberikan suara

def vote(pps_id, votes):
  book = xlrd.open_workbook("voting.xlsx")
  sheet = book.sheet_by_name("Sheet1")
  for row in range(sheet.nrows):
    if sheet.cell_value(row, 0) == pps_id:
      sheet.cell_value(row, 1) += votes
  book.save("voting.xlsx")

  return True

# Definisikan fungsi untuk menampilkan hasil voting

def show_results(results):
  for result in results:
    print(f"{result['candidate_id']}: {result['votes']}")

# Tampilkan formulir voting

def show_form():
  print("Pilih PPS yang akan Anda pilih:")
  candidates = get_results()
  for candidate in candidates:
    print(f"{candidate['candidate_id']}: PPS {candidate['candidate_id']}")

# Tampilkan formulir voting

show_form()

# Tunggu input dari pengguna

user_input = input("Masukkan pilihan Anda: ")
pps_id = int(user_input)

# Proses voting

votes_input = input("Masukkan jumlah suara yang akan diberikan: ")
votes = int(votes_input)

if vote(pps_id, votes):
  print("Suara Anda berhasil diberikan.")
else:
  print("Suara Anda gagal diberikan.")

# Tampilkan hasil voting

results = get_results()
show_results(results)