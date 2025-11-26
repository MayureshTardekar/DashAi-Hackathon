# 🚀 Local Development - Quick Start

## ✅ What Works
- CSV Upload → Column Mapping → Dashboard & Forecast
- No login required (dev mode auth bypass)
- SQLite database (no PostgreSQL setup needed)
- All analytics features working

---

## 📋 Prerequisites

```bash
# Python 3.8+
python --version

# Node.js 16+
node --version
```

---

## 🏃 Step 1: Setup Database

```bash
# Install Python dependencies
pip install -r requirements.txt

# Initialize database (creates ml_analytics.db)
python init_db.py
```

Expected output:
```
🔧 Initializing database...
✅ Using database: sqlite:///ml_analytics.db
✅ Database initialized successfully!
```

---

## 🖥️ Step 2: Start Backend

```bash
python app.py
```

Expected output:
```
✅ Using database: sqlite:///ml_analytics.db
🔧 Checking database...
✅ Database ready
🚀 Starting Flask server (debug=True)
📍 Backend: http://localhost:5000
⚠️ DEV MODE: Auth bypass enabled (DEV_DISABLE_AUTH=true)
```

Backend runs on: **http://localhost:5000**

---

## 🎨 Step 3: Start Frontend

**Open a new terminal:**

```bash
# Install dependencies (first time only)
npm install

# Start frontend
npm run dev
```

Expected output:
```
VITE ready in 500 ms
➜  Local:   http://localhost:5173/
```

Frontend runs on: **http://localhost:5173**

---

## 🧪 Step 4: Test the App

### 1. Open Frontend
Navigate to: **http://localhost:5173**

You should see the dashboard directly (no login page).

### 2. Upload CSV
- Click **"Upload CSV"** button in the top-right
- Select any CSV file with:
  - Date column (e.g., `InvoiceDate`, `Date`, `OrderDate`)
  - Numeric value column (e.g., `Amount`, `Sales`, `Revenue`)
  - Optional: Product, Country, CustomerID columns

### 3. Column Mapping
- If auto-detection fails, you'll see a mapping modal
- Select the correct columns for:
  - **Date** (required)
  - **Value** (required)
  - **Product** (optional)
  - **Region/Country** (optional)
  - **Customer ID** (optional)
- Click **"Save Mapping"**

### 4. View Dashboard
- See forecast chart with confidence bands
- View top countries (if Country column mapped)
- View top products (if Product column mapped)
- View RFM segmentation (if CustomerID mapped)
- Adjust forecast horizon (1-52 weeks)
- Change date range with date picker

---

## 📁 File Structure

```
project/
├── app.py                    ← Main backend (start with this)
├── init_db.py               ← Database initialization
├── .env                     ← Config (DEV_DISABLE_AUTH=true)
├── requirements.txt         ← Python dependencies
├── ml_analytics.db          ← SQLite database (auto-created)
├── uploads/                 ← CSV storage (auto-created)
│   └── 1/                   ← User 1's uploads
├── auth/
│   ├── middleware.py        ← Dev auth bypass
│   └── routes.py           ← Auth endpoints
├── database/
│   ├── connection.py        ← SQLite connection
│   └── models.py           ← DB models
├── ml/
│   └── forecast.py         ← ML forecasting logic
├── src/
│   ├── App.tsx             ← React app entry
│   ├── pages/Dashboard.tsx ← Main dashboard
│   └── services/api.ts     ← API calls
└── package.json            ← Frontend dependencies
```

---

## 🔍 Troubleshooting

### ❌ Backend won't start

**Problem:** Port 5000 already in use
```bash
# Find process on port 5000
lsof -i :5000

# Kill it
kill -9 <PID>

# Or use different port
python app.py  # Then edit in .env: FLASK_PORT=5001
```

**Problem:** Missing dependencies
```bash
pip install -r requirements.txt --upgrade
```

---

### ❌ Frontend won't start

**Problem:** Port 5173 in use
```bash
# Kill Vite process
pkill -f vite

# Or let Vite auto-assign new port
npm run dev
```

**Problem:** Module not found
```bash
rm -rf node_modules package-lock.json
npm install
```

---

### ❌ Upload fails

**Problem:** `uploads/` folder missing
```bash
mkdir -p uploads
chmod 755 uploads
```

**Problem:** File too large
- Default limit: 100MB
- Check file size: `ls -lh yourfile.csv`
- Reduce data or increase `MAX_FILE_SIZE` in `app.py`

---

### ❌ Database errors

**Problem:** `ml_analytics.db` corrupted
```bash
# Delete and recreate
rm ml_analytics.db
python init_db.py
```

**Problem:** Permission denied
```bash
chmod 644 ml_analytics.db
```

---

### ❌ Frontend shows 404/401 errors

**Check backend is running:**
```bash
# Test health endpoint
curl http://localhost:5000/health

# Should return:
# {"status":"healthy","timestamp":"2025-..."}
```

**Check CORS:**
Backend console should show:
```
ALLOWED_ORIGINS: ['http://localhost:5173']
```

---

### ❌ Charts not showing

**Problem:** Missing columns
- Ensure CSV has required columns (date + value)
- Check browser console (F12) for errors
- Try re-uploading and mapping columns

**Problem:** Data too sparse
- Need at least 10 rows for forecast
- Need multiple time periods for trend analysis

---

## 🎯 What's Working

✅ Direct dashboard access (no login)  
✅ CSV upload with validation  
✅ Auto-detect date/value/product/country/customer columns  
✅ Manual column mapping modal  
✅ ML forecast with ARIMA/Prophet/LinearRegression  
✅ Forecast horizon selection (1-52 weeks)  
✅ Date range filtering  
✅ Top countries breakdown (if Country mapped)  
✅ Top products breakdown (if Product mapped)  
✅ RFM customer segmentation (if CustomerID mapped)  
✅ Root cause analysis  
✅ Accuracy metrics with confidence bands  
✅ SQLite auto-fallback (no PostgreSQL needed)  

---

## ⚠️ Not Implemented (Intentionally Skipped)

🚫 Sui wallet connect  
🚫 Blockchain logging  
🚫 Production security hardening  
🚫 Multi-tenant user management  
🚫 Real authentication (bypassed for dev)  

---

## 🔄 Reset Everything

If you want to start fresh:

```bash
# Stop all servers (Ctrl+C in both terminals)

# Delete database and uploads
rm ml_analytics.db
rm -rf uploads/

# Recreate database
python init_db.py

# Restart backend
python app.py

# Restart frontend (in new terminal)
npm run dev
```

---

## ✅ Ready for Testing!

**Backend:** http://localhost:5000  
**Frontend:** http://localhost:5173  
**Health Check:** http://localhost:5000/health

Everything is configured to work immediately with zero auth friction.
