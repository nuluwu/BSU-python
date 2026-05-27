## Лабораторная работа 2, Вариант 1

TestData = """
    >Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT
    """


def GC(Data):
    
    ## Для выполнения работы удобно использовать список
    Sequences = {}
    CurrentID = ""
    
    ## Избавляем исходный код от пробелов и пустых символов при помощи .strip(), разделяем строки при помощи .split()
    for line in Data.strip().split('\n'):

        ## Используем .strip() второй раз, на случай, если исходные данные сделаны криво
        line = line.strip()

        ## Если строка начинается с символа >, это имя последовательности (в силу формата FASTA)
        if line.startswith('>'):
            CurrentID = line[1:]
            Sequences[CurrentID] = ""

        ## В ином случае это последовательность (или ее часть, поэтому используем +=)
        else:
            Sequences[CurrentID] += line

    ## Переменная начинается с -1, на случай, если процент GC во всех последовательностях окажется равен 0        
    BestPercent = -1
    BestID = ""
    
    for seq_id, sequence in Sequences.items():
        GC_Count = sequence.count('G') + sequence.count('C')
        GC_Percent = (GC_Count / len(sequence)) * 100
        
        if GC_Percent > BestPercent:
            BestPercent = GC_Percent
            BestID = seq_id
            
    ## Процент выводим с 6-ю знаками после запятой
    print(BestID)
    print(f"{BestPercent:.6f}")


## Тест
GC(TestData)
