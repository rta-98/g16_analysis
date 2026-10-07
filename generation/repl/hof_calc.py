from pathlib import Path 
import cclib 
import pandas as pd
from cclib.parser.utils import convertor
#|%%--%%| <gJ5NIBVJAv|a7jdvMErnr>
storage = Path("/home/yang/projects/62_ftab/data/storage/")
logs_dir = storage / "./log" 
h_kcal = 627.5
#|%%--%%| <a7jdvMErnr|GglzriCACQ>
qm_mols = {}

for files in logs_dir.iterdir():
    data = cclib.io.ccread(files)
    fname = Path(files.stem)
    if data and hasattr(data, 'zpve'):
        e_elec_ev = data.scfenergies[-1]
        e_elec_hartree = convertor(e_elec_ev, "eV", "hartree") 
        zpve_hartree = data.zpve 
        H_0K = e_elec_hartree + zpve_hartree 
        H_0K_kcal = H_0K * h_kcal
        print(f"{fname} {H_0K * h_kcal} kcal/mol")
        qm_mols[f"{fname}"] = H_0K_kcal 

#|%%--%%| <GglzriCACQ|SHxod52WFE>
df = pd.DataFrame(data=[qm_mols])
df.T.to_csv("62_ftab_beta_dhf.csv")
