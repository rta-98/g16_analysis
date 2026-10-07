from rdkit import Chem 
from pathlib import Path 
from openbabel import pybel 

storage = Path("/home/yang/projects/62_ftab/storage")
g16 = storage / "./g16"
log = storage / "./log" 

log.mkdir(parents=True, exist_ok=True) 

for file in g16.iterdir():
    with open(file, 'r') as file_in:
        content = file_in.read() 
    stem = Path(file).stem
    newlog = f"{stem}.log" 
    newlog_path = log / newlog
    with open(newlog_path, 'w') as file_out:
        file_out.write(content) 
               
for file in log.iterdir():
    moles = list(pybel.readfile("g09", file))
    print(moles)


#|%%--%%| <KIuPdZlsMM|IjuBTAaA6p>
for file in log.iterdir():
    moles = list(pybel.readfile("g09", str(file)))
    if moles: 
        fname = Path(file).stem 
        smi_name = f"{fname}.smi"
        mol = moles[-1]
        smi_str = mol.write("smi", fname, overwrite=True)
        print(smi
