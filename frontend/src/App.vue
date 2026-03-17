<template>
  <div class="flex min-h-screen bg-slate-100 text-slate-900">
    <Sidebar :open="sidebarOpen" @update:open="sidebarOpen = $event" />
    <main
      class="bg-[#fff] flex-1 px-4 py-4 md:px-6 md:py-6 transition-[margin] duration-300"
      :class="sidebarOpen ? 'md:ml-64' : 'md:ml-0'"
    >
      <section class="p-6">
        <FeedView />
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";
import FeedView from "./views/FeedView.vue";
import Sidebar from "./components/Sidebar.vue";

const sidebarOpen = ref(true);

const handleResize = () => {
  if (window.innerWidth < 1024) {
    sidebarOpen.value = false;
  } else {
    sidebarOpen.value = true;
  }
};

onMounted(() => {
  handleResize();
  window.addEventListener("resize", handleResize);
});

onUnmounted(() => {
  window.removeEventListener("resize", handleResize);
});
</script>
