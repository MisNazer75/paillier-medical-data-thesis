"""End-to-end SQLite demo: no private key is persisted or published."""
import argparse, csv, json, sqlite3
from decimal import Decimal
from experiment import ROOT, FIELDS, load, cents
from phe import paillier

def run(count=1000,bits=2048):
    rows=load()[:count]
    if len(rows)!=count or count<1: raise ValueError('Requested count not available')
    pub,priv=paillier.generate_paillier_keypair(n_length=bits)
    work=ROOT/'local_run';work.mkdir(exist_ok=True)
    source=work/'cancer_patients_data.db';encrypted=work/'encrypted_cancer_patients_data.db'
    for p in [source,encrypted]:
        if p.exists():p.unlink()
    with sqlite3.connect(source) as con:
        con.execute('CREATE TABLE cancer_patient_data (id INTEGER PRIMARY KEY,patient_name TEXT,age INTEGER,gender TEXT,cancer_type TEXT,cancer_stage TEXT,treatment_type TEXT,diagnosis_date TEXT,metastasis TEXT,blood_test_result TEXT,tumor_marker TEXT)')
        con.executemany('INSERT INTO cancer_patient_data VALUES (?,?,?,?,?,?,?,?,?,?,?)',[[r[k] for k in FIELDS] for r in rows])
    with sqlite3.connect(encrypted) as con:
        con.execute('CREATE TABLE encrypted_cancer_patient_data (id INTEGER PRIMARY KEY,patient_name TEXT,age INTEGER,gender TEXT,cancer_type TEXT,cancer_stage TEXT,treatment_type TEXT,diagnosis_date TEXT,metastasis TEXT,encrypted_blood_test_result TEXT,blood_test_exponent INTEGER,encrypted_tumor_marker TEXT,tumor_marker_exponent INTEGER,scale INTEGER)')
        for r in rows:
            eb=pub.encrypt(cents(r['blood_test_result']));et=pub.encrypt(cents(r['tumor_marker']))
            con.execute('INSERT INTO encrypted_cancer_patient_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[r[k] for k in FIELDS[:9]]+[str(eb.ciphertext()),eb.exponent,str(et.ciphertext()),et.exponent,100])
    with sqlite3.connect(encrypted) as con:
        stored=con.execute('SELECT * FROM encrypted_cancer_patient_data ORDER BY id').fetchall()
    recovered=[];columns=[[],[]]
    for r in stored:
        eb=paillier.EncryptedNumber(pub,int(r[9]),r[10]);et=paillier.EncryptedNumber(pub,int(r[11]),r[12])
        columns[0].append(eb);columns[1].append(et)
        rec=list(r[:9])+[format(Decimal(priv.decrypt(e))/100,'.2f') for e in [eb,et]]
        recovered.append(rec)
    with (work/'recovered.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(FIELDS);w.writerows(recovered)
    totals=[]
    for column in columns:
        encsum=column[0]
        for e in column[1:]:encsum+=e
        encsum.ciphertext()
        totals.append(priv.decrypt(encsum))
    assert all(cents(rec[9+j])==cents(orig[FIELDS[9+j]]) for rec,orig in zip(recovered,rows) for j in range(2))
    assert totals==[sum(cents(r[FIELDS[9+j]]) for r in rows) for j in range(2)]
    report={'patients':count,'key_bits':bits,'scale':100,'exact_recovery':True,'aggregate_totals_scaled':totals,'aggregate_totals':[str(Decimal(v)/100) for v in totals],'aggregate_means':[str(Decimal(v)/100/count) for v in totals],'public_n':str(pub.n),'private_key_saved':False}
    (work/'verification.json').write_text(json.dumps(report,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k!='public_n'},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=1000);p.add_argument('--bits',type=int,default=2048)
    a=p.parse_args();run(a.count,a.bits)
