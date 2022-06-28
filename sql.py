from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="mysql-rfam-public.ebi.ac.uk",
        database="Rfam",
        port=4497,
        user="rfamro",
        password=none,   
) as connection:
        print(connection)
except Error as e:
    print(e)


#SELECT fr.rfam_acc, fr.rfamseq_acc, fr.seq_start, fr.seq_end
#FROM full_region fr, rfamseq rf, taxonomy tx
#WHERE rf.ncbi_id = tx.ncbi_id
#AND fr.rfamseq_acc = rf.rfamseq_acc
#AND tx.ncbi_id = 10116 -- NCBI taxonomy id of Rattus norvegicus
#AND is_significant = 1 -- exclude low-scoring matches from the same clan
