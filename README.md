## Trendsee

Trendsee is a small full‑stack app for browsing a user’s posts feed, opening a detailed analysis modal, and working with a FastAPI backend backed by Postgres + Redis.

### Tech stack

- **Frontend**: Vue 3 + Vite + Tailwind CSS
- **Backend**: FastAPI + SQLAlchemy (async) + asyncpg
- **Data**: Postgres
- **Cache**: Redis
- **Dev runtime**: Docker Compose

### Project structure

- **`frontend/`**: Vue app (Vite dev server)
- **`backend/`**: FastAPI app
- **`docker-compose.yml`**: local dev stack (frontend, backend, postgres, redis)

### Quick start (recommended): Docker Compose

From the repository root:

```bash
docker compose up --build
```

Then open:

- **Frontend**: `http://localhost:5173`
- **Backend** (host): `http://localhost:8001`

### Services and ports

- **frontend**: `5173:5173`
- **backend**: `8001:8000`
- **postgres**: `5433:5432` (host port is 5433)
- **redis**: internal (default 6379)

### API overview

All backend routes are mounted under the `/api` prefix.

- **Health**: `GET /health`
- **Posts**
  - `GET /api/posts/user/{user_id}?limit=...&offset=...`
  - `GET /api/posts/user/{user_id}/count`
  - `GET /api/posts/{post_id}`
  - `POST /api/posts` (requires auth)
  - `PATCH /api/posts/{post_id}` (requires auth)
  - `DELETE /api/posts/{post_id}` (requires auth)
- **Users / Tokens**
  - `POST /api/users`
  - `GET /api/users/{user_id}/token`

### Backend startup notes

Postgres can take a moment to become ready (especially after an unclean shutdown). The stack includes:

- a **Postgres healthcheck** (`pg_isready`)
- a **backend startup retry loop** so the API won’t exit while Postgres is still “starting up”

### Development notes (frontend)

The UI uses Tailwind heavily. Key behaviors:

- Feed initial load fetches **count + first page in parallel** for better perceived speed.
- Cards clamp preview text to **2 lines**.
- Modal:
  - right panel scrolls
  - left column is sticky (“fixed” within modal)
  - modal can be dragged (mouse/touch)
  - background page scroll is locked while modal is open

### Troubleshooting

#### Docker build fails: `TLS handshake timeout` pulling `node:20-alpine`

This is almost always a network/VPN/proxy/DNS issue reaching Docker Hub.

Try:

```bash
docker pull node:20-alpine
docker compose build --no-cache frontend
docker compose up
```

If it still fails:

- Temporarily disable VPN/proxy
- Check Docker Desktop network/DNS settings
- Retry later (Docker Hub / network flakiness happens)

#### Frontend can’t reach backend (`ENOTFOUND backend`, proxy errors)

This typically happens if the backend container exited. Check logs and restart:

```bash
docker compose ps
docker compose up -d backend
```

#### Postgres “system is starting up”

If the backend starts before Postgres is ready, it should now retry automatically. If you still see issues, restart the stack:

```bash
docker compose down
docker compose up --build
```

### License

Internal/educational project (no license specified).

## Trendsee Test Task

Fullstack test project: FastAPI backend with JWT and Redis cache, Vue.js frontend with feed, modal post view and infinite scroll.

### Project structure

- **backend**: FastAPI service with PostgreSQL and Redis
- **frontend**: Vue 3 + Vite SPA for posts feed
- **docker-compose.yml**: runs full stack with one command

### Run with Docker

```bash
docker-compose up --build
```

Backend will be available at `http://localhost:8001`, frontend at `http://localhost:5173`.

### Backend (FastAPI)

- **Stack**: FastAPI, async SQLAlchemy, PostgreSQL, Redis, JWT
- **Key features**:
  - Users CRUD
  - JWT token issued on user creation and by user id (for testing)
  - Posts CRUD with ownership checks
  - Hot posts (first 10 minutes) served from Redis, older posts from Postgres with artificial 2s delay
  - Dependency Injection for DB, Redis, repositories and services

Main endpoints (short):

- `POST /users` – create user, returns JWT
- `GET /users/{id}/token` – issue JWT for user id
- `PATCH /users/{id}` – update user name
- `DELETE /users/{id}` – delete user
- `POST /posts` – create post (auth)
- `PATCH /posts/{id}` – update post (auth + owner)
- `DELETE /posts/{id}` – delete post (auth + owner)
- `GET /posts/user/{user_id}` – list posts of user (limit/offset)
- `GET /posts/{id}` – get single post

You can explore full schema and responses at `http://localhost:8001/docs`.

### Frontend (Vue.js)

- **Stack**: Vue 3, Vite, Axios
- **Features**:
  - Posts feed for a selected user (default user `#1`)
  - Card with title, short text and created date
  - Modal with full post info (title, text, user_id, created_at, updated_at) with animated transition
  - Infinite scroll: when you scroll within 500px of the bottom, next page loads and appends
  - Loading indicator and graceful end-of-list state

### API base URL

In Docker, frontend talks to backend via `/api` proxy. For local dev you can run them separately:

```bash
# backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# frontend
cd frontend
npm install
npm run dev
```

Then adjust `vite.config.mts` `target` if needed (default `http://localhost:8000` or `http://localhost:8001` depending on your setup).

