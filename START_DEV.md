# 🚀 Development Quick Start

## ✅ Current Status
- ✅ Frontend: No login required, opens directly to dashboard
- ✅ Backend: Auth bypass enabled for testing
- ✅ Database: Auto-fallback to SQLite if PostgreSQL unavailable
- ✅ Full workflow: Upload → Mapping → Dashboard → Forecast

---

## 🔧 Prerequisites
```bash
# Python 3.8+
python --version

# Node.js 16+
node --version
```

---

## 🏃 Run Backend (Terminal 1)

```bash
# Install dependencies
pip install -r requirements.txt

# Start backend (uses app_v2.py)
python app_v2.py
```

Backend runs on: **http://localhost:5000**

⚠️ **Auth Bypass Active**: `DEV_DISABLE_AUTH=true` in `.env`

---

## 🎨 Run Frontend (Terminal 2)

```bash
# Install dependencies
npm install

# Start frontend
npm run dev
```

Frontend runs on: **http://localhost:5173**

---

## 📊 Test Workflow

1. **Open**: http://localhost:5173
2. **Upload CSV**: Click "Upload CSV" button
3. **Map Columns**: Confirm date/value columns
4. **View Dashboard**: See forecast + analytics
5. **Adjust Settings**: Change date range, forecast horizon

---

## 🔍 Database Behavior

**Automatic Fallback:**
- Tries PostgreSQL first (`DATABASE_URL` from `.env`)
- If PostgreSQL unavailable → Falls back to `sqlite:///ml_analytics.db`
- ✅ No manual intervention needed

**Reset Database:**
```bash
# If using SQLite
rm ml_analytics.db
python -c "from database.connection import init_db; init_db()"

# If using PostgreSQL
psql -U postgres -c "DROP DATABASE ml_analytics; CREATE DATABASE ml_analytics;"
python -c "from database.connection import init_db; init_db()"
```

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check port 5000 is free
lsof -i :5000
kill -9 <PID>

# Verify dependencies
pip install -r requirements.txt --upgrade
```

### Frontend won't connect
```bash
# Check CORS in backend logs
# Should see: "ALLOWED_ORIGINS: ['http://localhost:5173']"

# Verify .env has:
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

### Database errors
```bash
# Database auto-falls back to SQLite
# Check console output:
# ✅ Connected to PostgreSQL  (or)
# ⚠️ Using SQLite fallback
```

### Upload fails
```bash
# Check uploads/ folder exists
mkdir -p uploads

# Check file permissions
chmod 755 uploads
```

---

## 📁 File Structure

```
project/
├── app_v2.py              ← Main backend (Production V1 with auth bypass)
├── app.py                 ← Legacy backend (no auth, kept for reference)
├── .env                   ← Environment config (DEV_DISABLE_AUTH=true)
├── requirements.txt       ← Python dependencies
├── src/
│   ├── App.tsx           ← React app (no login required)
│   ├── pages/Dashboard.tsx
│   └── services/api.ts   ← API calls
├── auth/
│   └── middleware.py     ← Auth bypass logic
├── database/
│   └── connection.py     ← DB with SQLite fallback
└── uploads/              ← CSV storage
```

---

## 🎯 What's Working

✅ UI opens directly (no login screen)  
✅ CSV upload with validation  
✅ Auto-detect columns (date/value/product/region/customer)  
✅ Manual column mapping modal  
✅ Dashboard with forecast chart  
✅ Country & product breakdown  
✅ RFM customer segmentation  
✅ Forecast horizon selection (1-52 weeks)  
✅ Date range filtering  
✅ Root cause analysis  
✅ Accuracy metrics with confidence bands  
✅ Backend auth bypass for testing  
✅ Database auto-fallback  

---

## ⚠️ Known Limitations (Intentional)

🚫 No blockchain logging (skipped for now)  
🚫 No wallet connect (skipped for now)  
🚫 No production security hardening  
🚫 No user management (auth bypassed)  

**Focus**: Core analytics workflow is fully functional for testing

---

## 🔄 Next Steps After Testing

1. **Enable Production Auth**: Set `DEV_DISABLE_AUTH=false` in `.env`
2. **Add User Registration**: Implement signup flow
3. **Configure PostgreSQL**: Set proper `DATABASE_URL`
4. **Deploy**: Use Heroku/Railway/AWS
5. **Add Blockchain**: Re-enable SUI logging if needed

---

## 📝 Environment Variables

```bash
# .env (Backend)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ml_analytics
JWT_SECRET=dev-secret-key-for-testing-only-change-in-production
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
FLASK_ENV=development
DEV_LOGIN_ENABLED=true
DEV_DISABLE_AUTH=true        # ⚠️ Auth bypass for testing
BLOCKCHAIN_URL=http://127.0.0.1:8545
```

No frontend `.env` needed - auth is already bypassed in frontend

---

## ✅ Ready for Testing!

Everything is configured to run smoothly with zero auth friction.

**Start both servers and test the full workflow.**
