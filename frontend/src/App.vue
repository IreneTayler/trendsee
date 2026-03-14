<template>
  <div class="flex min-h-screen bg-slate-100 text-slate-900">
    <Sidebar />
    <main class="ml-64 flex-1 px-6 py-6">
      <header class="mb-6">
        <h1 class="text-2xl font-semibold">Лента публикаций</h1>
        <p class="mt-1 text-sm text-slate-500">Карточки постов с бэкенда. Модалка по клику, бесконечная прокрутка.</p>
      </header>
      <section class="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
        <FeedView />
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import FeedView from "./views/FeedView.vue";
import Sidebar from "./components/Sidebar.vue";
</script>
