# Famous Hacker Movie 1337 - Ticket System
Sistem pembelian tiket berbasis blockchain untuk film "Famous Hacker Movie 1337"

[English version below](#english)

## 🇮🇩 Bahasa Indonesia

### Deskripsi
Sistem pembelian tiket NFT menggunakan smart contract Ethereum dengan antarmuka web yang memiliki tema cyberpunk. Sistem ini memungkinkan pengguna untuk membeli tiket film menggunakan ETH dan menerima tiket dalam bentuk NFT.

### Prasyarat
- Python 3.8 atau lebih baru
- Node.js dan npm
- Ganache (blockchain lokal)
- MetaMask (opsional, untuk pengujian di jaringan testnet)
- Python virtual environment

### Dependensi Python
```bash
pip install flask web3
```

### Cara Instalasi
1. Clone repositori ini
```bash
git clone [url-repositori]
cd ticketing_project
```

2. Setup Virtual Environment
```bash
# Membuat virtual environment
python3 -m venv venv

# Aktivasi virtual environment
# Untuk Linux/Mac:
source venv/bin/activate
# Untuk Windows:
# .\venv\Scripts\activate

# Install dependensi
pip install flask web3
```

3. Jalankan Ganache
- Buka aplikasi Ganache / ganache-cli
- Buat workspace baru atau gunakan QuickStart
- Pastikan Ganache berjalan di `http://127.0.0.1:8545`

4. Deploy Smart Contract
```bash
# Deploy smart contract ke Ganache
python deploy_contract.py
```
- Pastikan file `contract_info.json` sudah ada dan berisi ABI dan alamat kontrak yang benar
- Format `contract_info.json`:
```json
{
    "abi": [...],
    "address": "0x..."
}
```

### Menjalankan Aplikasi
1. Pastikan virtual environment aktif
```bash
# Jika belum aktif, jalankan:
source venv/bin/activate  # Linux/Mac
# atau
# .\venv\Scripts\activate  # Windows
```

2. Jalankan aplikasi Flask
```bash
python app.py
```

3. Buka browser dan akses
```
http://localhost:5000
```

4. Untuk menonaktifkan virtual environment setelah selesai
```bash
deactivate
```

### Fitur
- 🎫 Pembelian tiket menggunakan ETH
- 💰 Tampilan saldo wallet real-time
- 🎨 UI bergaya cyberpunk
- 📱 Responsive design
- 🔗 Integrasi blockchain
- 🎯 Konfirmasi transaksi otomatis

### Troubleshooting
1. **Ganache Connection Error**
   - Pastikan Ganache berjalan
   - Verifikasi URL di `app.py` sesuai dengan Ganache

2. **Smart Contract Error**
   - Periksa file `contract_info.json`
   - Pastikan alamat kontrak benar
   - Verifikasi ABI kontrak

3. **Virtual Environment Error**
   - Pastikan virtual environment aktif (`venv` muncul di prompt)
   - Cek instalasi dependensi dengan `pip list`
   - Jika ada masalah, hapus folder `venv` dan buat ulang

---

<a name="english"></a>
## 🇬🇧 English

### Description
NFT ticket purchasing system using Ethereum smart contract with a cyberpunk-themed web interface. The system allows users to purchase movie tickets using ETH and receive tickets as NFTs.

### Prerequisites
- Python 3.8 or newer
- Node.js and npm
- Ganache (local blockchain)
- MetaMask (optional, for testnet testing)
- Python virtual environment

### Python Dependencies
```bash
pip install flask web3
```

### Installation
1. Clone this repository
```bash
git clone [repository-url]
cd ticketing_project
```

2. Setup Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# For Linux/Mac:
source venv/bin/activate
# For Windows:
# .\venv\Scripts\activate

# Install dependencies
pip install flask web3
```

3. Run Ganache
- Open Ganache application
- Create new workspace or use QuickStart
- Ensure Ganache is running at `http://127.0.0.1:8545`

4. Deploy Smart Contract
```bash
# Deploy smart contract to Ganache
python deploy_contract.py
```
- Ensure `contract_info.json` exists with correct ABI and contract address
- `contract_info.json` format:
```json
{
    "abi": [...],
    "address": "0x..."
}
```

### Running the Application
1. Ensure virtual environment is active
```bash
# If not already active, run:
source venv/bin/activate  # Linux/Mac
# or
# .\venv\Scripts\activate  # Windows
```

2. Run Flask application
```bash
python app.py
```

3. Open browser and access
```
http://localhost:5000
```

4. To deactivate virtual environment when finished
```bash
deactivate
```

### Features
- 🎫 Ticket purchase using ETH
- 💰 Real-time wallet balance display
- 🎨 Cyberpunk-styled UI
- 📱 Responsive design
- 🔗 Blockchain integration
- 🎯 Automatic transaction confirmation

### Troubleshooting
1. **Ganache Connection Error**
   - Ensure Ganache is running
   - Verify URL in `app.py` matches Ganache

2. **Smart Contract Error**
   - Check `contract_info.json` file
   - Ensure contract address is correct
   - Verify contract ABI

3. **Virtual Environment Error**
   - Ensure virtual environment is active (`venv` appears in prompt)
   - Check dependencies installation with `pip list`
   - If issues persist, delete `venv` folder and recreate

### Directory Structure
```
ticketing_project/
├── app.py                 # Flask backend
├── deploy_contract.py     # Smart contract deployment script
├── README.md             # This file
├── contract_info.json    # Smart contract configuration
├── venv/                # Virtual environment (generated)
└── templates/            # Frontend templates
    ├── index.html       # Main page
    └── ticket.html      # Ticket confirmation page
```

### Tech Stack
- Backend: Flask (Python)
- Blockchain: Web3.py
- Frontend: Bootstrap 5, Font Awesome 6
- Template Engine: Jinja2
- Local Blockchain: Ganache 
