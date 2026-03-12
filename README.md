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

