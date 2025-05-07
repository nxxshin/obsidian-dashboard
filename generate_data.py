import obsidiantools.api as otools
import numpy as np
np.NaN = np.nan

import os
from pathlib import Path

directory = Path(os.path.abspath("../../../library/areas/obsidian"))
print(directory)

vault = otools.Vault(directory).connect().gather()

df = vault.get_note_metadata()

df.to_csv('output.csv', index=False)