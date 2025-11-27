# 🚀 Local Testing Guide

## Quick Start

This guide will help you run the Dash AI analytics app locally for testing and development.

---

## ⚙️ Prerequisites

- **Python 3.9+** installed
- **Node.js 16+** and npm installed
- Basic terminal/command line knowledge

---

## 📦 Step 1: Install Dependencies

### Backend Dependencies

```bash
pip install -r requirements.txt
```

### Frontend Dependencies

```bash
npm install
```

---

## 🗄️ Step 2: Setup Database

The app uses SQLite by default (no PostgreSQL needed for testing).

Initialize the database:

```bash
python init_db.py
```

This creates `ml_analytics.db` with all required tables.

---

## 🔧 Step 3: Configure Environment

Ensure your `.env` file has these settings:

```env
# Backend runs in dev mode with auth bypass
DEV_DISABLE_AUTH=true
FLASK_ENV=development

# Database (SQLite for local testing)
DATABASE_URL=sqlite:///ml_analytics.db

# CORS for local frontend
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

**Frontend** (if you have a separate frontend `.env`):
```env
VITE_DEV_DISABLE_AUTH=true
```

---

## 🚀 Step 4: Start the Application

### Terminal 1: Start Backend

```bash
python app.py
```

✅ Backend should start on: **http://localhost:5000**

You should see:
```
✅ Database ready
🚀 Starting Flask server (debug=True)
📍 Backend: http://localhost:5000
⚠️ DEV MODE: Auth bypass enabled (DEV_DISABLE_AUTH=true)
```

### Terminal 2: Start Frontend

```bash
npm run dev
```

✅ Frontend should start on: **http://localhost:5173** (or 5174)

---

## 🧪 Step 5: Test the Application

### **Scenario 1: No CSV Uploaded (Empty State)**

1. Open browser at **http://localhost:5173**
2. You should see:
   - Dashboard with **empty charts** (showing 0 values)
   - Message: "No CSV file uploaded yet"
   - All chart frames are visible but showing placeholder/empty state
   - No errors or broken UI

### **Scenario 2: Upload CSV**

1. Click **"Upload Dataset"** button
2. Select a CSV file with columns like:
   - `Date` or `InvoiceDate`
   - `Amount` or `Sales` or `Quantity` (numeric value)
   - Optional: `Product`, `Country`, `CustomerID`
3. Click **"Upload & Analyze"**

**Expected Result:**
- Upload succeeds
- If auto-detection is confident, dashboard loads immediately
- If not, you'll see a **mapping modal** to confirm fields
- Dashboard shows real charts with your data

### **Scenario 3: View Dashboard**

After successful upload:
- ✅ KPI cards show total value, growth, avg per week, transactions
- ✅ Forecast chart with historical data and predictions
- ✅ Country/Product bar charts (if data has these columns)
- ✅ RFM segmentation (if CustomerID exists)
- ✅ Date range picker works
- ✅ Forecast horizon selector (2/4/8/12 weeks)

---

## 🐛 Troubleshooting

### "Failed to upload CSV file"

**Cause**: Backend not running or database issue

**Solution**:
```bash
# Check backend is running
curl http://localhost:5000/health

# Reinitialize database
python init_db.py

# Restart backend
python app.py
```

### "Invalid JSON response from server"

**Cause**: Backend returning HTML error page instead of JSON

**Solution**:
1. Check backend terminal for error messages
2. Ensure `DEV_DISABLE_AUTH=true` in `.env`
3. Verify database is initialized

### Charts not showing

**Cause**: Data format issue or missing columns

**Solution**:
1. Ensure CSV has date and numeric columns
2. Check browser console (F12) for errors
3. Try the mapping modal to manually assign columns

### Database locked error

**Cause**: Multiple processes accessing SQLite

**Solution**:
```bash
# Stop all Python processes
# Delete the database and recreate
rm ml_analytics.db
python init_db.py
python app.py
```

---

## 📂 File Structure

```
/
├── app.py                    # ✅ Main backend entry point
├── database/
│   ├── connection.py         # SQLite connection
│   ├── models.py             # Database models
│   └── init_db.sql
├── auth/
│   ├── middleware.py         # Auth bypass for dev mode
│   └── routes.py
├── ml/
│   └── forecast.py           # ML forecasting logic
├── uploads/                  # ← User-uploaded CSV files
├── src/                      # React frontend
│   ├── pages/Dashboard.tsx
│   ├── components/
│   └── services/api.ts
└── .env                      # ← Configuration
```

---

## 🎯 What to Expect

### With NO CSV uploaded:
- Dashboard renders with **empty/zero state**
- All chart containers visible
- Message: "No CSV file uploaded yet"
- Upload button prominent and functional

### With CSV uploaded:
- Real data in all visualizations
- Forecasts generated using ML models
- Interactive date range filtering
- Downloadable results

---

## 🔐 Dev Mode vs Production

**Current Setup (Dev Mode):**
- ✅ No authentication required
- ✅ Direct access to dashboard
- ✅ SQLite database (simple, local)
- ❌ No Web3/blockchain
- ❌ No Sui wallet
- ❌ No production security

**For Production (TODO):**
- Implement real authentication
- PostgreSQL database
- Web3 wallet integration
- Blockchain logging
- Security hardening

---

## 🆘 Need Help?

1. Check backend logs in terminal 1
2. Check browser console (F12 → Console tab)
3. Check network tab (F12 → Network) for failed API calls
4. Ensure both backend and frontend are running
5. Verify `.env` has `DEV_DISABLE_AUTH=true`

---

## ✅ Success Checklist

- [ ] Backend starts without errors
- [ ] Frontend loads at http://localhost:5173
- [ ] Dashboard shows empty state (no errors)
- [ ] CSV upload works
- [ ] Mapping modal appears (if needed)
- [ ] Dashboard shows real data after upload
- [ ] Date range picker functions
- [ ] Charts render properly

---

**Happy Testing! 🎉**
