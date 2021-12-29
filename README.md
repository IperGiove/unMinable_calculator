# unMinable
Unofficial unMinable calculator python library.
It returns the gain per day for every minable crypto in USDT.

## Installation and updating
```bash
pip install --upgrade --force-reinstall git+http://github.com/IperGiove/unminable.git
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

#### Exemple:
```
{
 "ATOMUSDT": 1.6331,
 "YFIUSDT": 1.633,
 "BNBUSDT": 1.6327,
 "LINKUSDT": 1.6325,
 "SUSHIUSDT": 1.6325,
 "1INCHUSDT": 1.6325,
 "ETHUSDT": 1.6323,
 "LTCUSDT": 1.6322,
 "ALGOUSDT": 1.6321,
 "AAVEUSDT": 1.6321,
 "XRPUSDT": 1.632,
 "MATICUSDT": 1.632,
 "BTCUSDT": 1.6318,
 "WAVESUSDT": 1.6318,
 "ENJUSDT": 1.6316,
 "SOLUSDT": 1.6316,
 "ADAUSDT": 1.6314,
 "CHZUSDT": 1.6314,
 "SHIBUSDT": 1.6314,
 "XMRUSDT": 1.6313,
 "ZECUSDT": 1.6312,
 "DASHUSDT": 1.6311,
 "BCHUSDT": 1.6311,
 "MANAUSDT": 1.6311,
 "UNIUSDT": 1.6311,
 "EOSUSDT": 1.631,
 "ETCUSDT": 1.631,
 "MTLUSDT": 1.631,
 "QTUMUSDT": 1.6309,
 "BATUSDT": 1.6307,
 "TRXUSDT": 1.6305,
 "WINUSDT": 1.6305,
 "KNCUSDT": 1.6305,
 "XTZUSDT": 1.6303,
 "BTTUSDT": 1.6301,
 "ZRXUSDT": 1.6301,
 "HOTUSDT": 1.63,
 "BANDUSDT": 1.63,
 "ICXUSDT": 1.6298,
 "VETUSDT": 1.6298,
 "REPUSDT": 1.6298,
 "XLMUSDT": 1.6296,
 "BTGUSDT": 1.6284,
 "DOGEUSDT": 1.6277,
 "ZILUSDT": 1.6273,
 "NANOUSDT": 1.6257,
 "RVNUSDT": 1.6256,
 "LSKUSDT": 1.6184,
 "DGBUSDT": 1.6154,
 "SCUSDT": 1.6138,
 "RSRUSDT": 1.6106,
 "XVGUSDT": 1.6081,
 "FUNUSDT": 1.6023,
 "NEOUSDT": 1.311
}

```
