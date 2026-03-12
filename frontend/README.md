## Frontend (Vue 3 + Vite)

This folder contains the Vue.js single-page application that implements the posts feed, modal post view and infinite scroll required by the assignment.

### Requirements

- Node.js 18+ and npm

### Install dependencies

```bash
cd frontend
npm install
```

### Run dev server

```bash
npm run dev
```

By default Vite will start on `http://localhost:5173`. In Docker, the frontend talks to the FastAPI backend through the `/api` proxy configured in `vite.config.mts`.

