## Лабораторная работа 4, Задание 3, Вариант 12

from Bio import SeqIO

Records = list(SeqIO.parse("combined_records.gb", "genbank"))

for record in Records:
    print(f"\nЗапись: {record.id} ({record.description[:50]}...)")
    CDS_Counter = 0
    
    for feature in record.features:
        if feature.type == "CDS":
            CDS_Counter += 1
            CDS_Seq = feature.location.extract(record.seq)
            Protein_Seq = CDS_Seq.translate()
            
            print(f"  [CDS #{CDS_Counter}] Длина нуклеотидов: {len(CDS_Seq)} bp")
            print(f"  Частичный белок: {Protein_Seq[:30]}...")