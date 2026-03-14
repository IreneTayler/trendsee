<template>
  <div class="flex min-h-screen bg-slate-100 text-slate-900">
    <Sidebar />
    <main class="ml-64 flex-1 px-6 py-6">
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
