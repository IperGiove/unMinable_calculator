# DB
DB library to interact with sql from python.

## Installation and updating
```bash
pip install --upgrade --force-reinstall git+http://github.com/1marte/unminable.git
```
## Usage
Features:
* get_symbol
* get_reward
* conversion

#### Demo:
```python
from unMinable.unMinable import unMinable

MHs = 25, 
algo = 'ethash'

un_minable = unMinable(MHs, algo)
un_minable.menage_get_reward()
un_minable.conversion()
print(json.dumps(un_minable.reward_day_usdt, indent=1))
```
