<template>
  <div class="app">
    <header class="app__header">
      <h1 class="app__title">Trendsee Feed</h1>
    </header>
    <main class="app__main">
      <FeedView />
    </main>
  </div>
</template>

<script setup lang="ts">
import FeedView from "./views/FeedView.vue";
</script>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: #0f172a;
  color: #e5e7eb;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.app__header {
  padding: 1rem 2rem;
  border-bottom: 1px solid rgba(148, 163, 184, 0.3);
  background: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(10px);
  position: sticky;
  top: 0;
  z-index: 10;
}

.app__title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.app__main {
  flex: 1;
  padding: 2rem 1rem;
  max-width: 900px;
  margin: 0 auto;
  width: 100%;
}

@media (max-width: 640px) {
  .app__header {
    padding-inline: 1rem;
  }

  .app__main {
    padding-inline: 1rem;
  }
}
</style>

