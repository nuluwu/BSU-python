## Лабораторная работа 4, Задание 2, Вариант 12

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

Records = list(SeqIO.parse("combined_records.gb", "genbank"))
GC_Data = []

for record in Records:
    GC_Value = gc_fraction(record.seq)
    GC_Percent = GC_Value * 100
    Description = f"{record.id}: {record.description}"
    GC_Data.append((GC_Percent, Description))

GC_Data.sort()

for gc, desc in GC_Data:
    print(f"{desc}, GC = {gc:.2f}%")