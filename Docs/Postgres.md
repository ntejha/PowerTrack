# PostgreSQL Setup for PowerTrack Project

This guide shows how to **download, install, configure, and use PostgreSQL** for the `PowerTrack` project inside a mamba environment, including setting a permanent password for the `ntejha` user.

---

## 1. Download & Install PostgreSQL

```bash
mamba create -n powertrack python=3.11 -y
mamba activate powertrack
mamba install -c conda-forge postgresql
```

## 2. Initialize PostgreSQL Database Directory

```bash
mkdir -p /home/ntejha/Projects/PowerTrack/pg_data
initdb -D /home/ntejha/Projects/PowerTrack/pg_data
```
---

### 3. Start PostgreSQL

```bash
pg_ctl -D /home/ntejha/Projects/PowerTrack/pg_data -l ~/pglogfile start
```
---

### 4. Connect to PostgreSQL

```bash
psql -U ntejha -d postgres
```
---

### 5. Set Password for ntejha

```bash
ALTER USER ntlejha WITH PASSWORD 'MySecurePassword123';
```
---

### 6. Change to Login

Edit the pg_hba.conf : ```nano /home/ntejha/Projects/PowerTrack/pg_data/pg_hba.conf```

Find :

```
local   all             all                                     trust
```

Change to :  

```
local   all             all                                     md5
```

Restart PostgreSQL :   ```pg_ctl -D /home/ntejha/Projects/PowerTrack/pg_data restart```

---

### 7. Login and Use 

```bash
psql -U ntlejha -d postgres -W
```



