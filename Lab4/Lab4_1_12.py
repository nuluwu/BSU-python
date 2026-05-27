## Лабораторная работа 4, Задание 1, Вариант 12

from Bio import SeqIO

CabbageRecords = list(SeqIO.parse("brassicaoleracea.gb", "genbank"))
print(f"Прочитано записей из файла капустки: {len(CabbageRecords)}")

HumanRecords = list(SeqIO.parse("homosapiens.gb", "genbank"))
print(f"Прочитано записей из файла человечка: {len(HumanRecords)}")

Combined = CabbageRecords + HumanRecords

TotalCDS = 0
for record in Combined:
    for feature in record.features:
        if feature.type == "CDS":
            TotalCDS += 1

print(f"Общее количество записей: {len(Combined)}")
print(f"Общее количество найденных кодирующих областей: {TotalCDS}")

SeqIO.write(Combined, "combined_records.gb", "genbank")
print("Итоговый файл успешно создан")