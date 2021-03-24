import gzip
import shutil

def main():
    with gzip.open('Zm-B73-REFERENCE-NAM-5.0.fa.gz','rb') as f_in:
        with open('Zm-B73-REFERENCE-NAM-5.0','wb') as f_out:
            shutil.copyfileobj(f_in,f_out)

main()