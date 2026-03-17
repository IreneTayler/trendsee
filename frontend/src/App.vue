<template>
  <div class="flex min-h-screen bg-slate-100 text-slate-900">
    <Sidebar :open="sidebarOpen" @update:open="sidebarOpen = $event" />

    <!-- Drag handle: when sidebar is hidden, user can drag from the edge to reveal it -->
    <div
      v-if="!sidebarOpen"
      class="fixed inset-y-0 left-0 z-20 w-2 cursor-ew-resize md:w-3"
      @mousedown="onSidebarDragStart"
      @mousemove="onSidebarDragMove"
      @mouseup="onSidebarDragEnd"
      @mouseleave="onSidebarDragEnd"
      @touchstart.prevent="onSidebarDragStart"
      @touchmove.prevent="onSidebarDragMove"
      @touchend="onSidebarDragEnd"
    />

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
const sidebarDragStartX = ref<number | null>(null);
const sidebarDragActive = ref(false);

const getClientX = (event: MouseEvent | TouchEvent): number => {
  if ("touches" in event) {
    const touch = event.touches[0];
    return touch ? touch.clientX : 0;
  }
  return (event as MouseEvent).clientX;
};

const onSidebarDragStart = (event: MouseEvent | TouchEvent) => {
  sidebarDragStartX.value = getClientX(event);
  sidebarDragActive.value = true;
};

const onSidebarDragMove = (event: MouseEvent | TouchEvent) => {
  if (!sidebarDragActive.value || sidebarDragStartX.value == null) return;
  const currentX = getClientX(event);
  const delta = currentX - sidebarDragStartX.value;
  if (delta > 40) {
    sidebarOpen.value = true;
    sidebarDragActive.value = false;
    sidebarDragStartX.value = null;
  }
};

const onSidebarDragEnd = () => {
  sidebarDragActive.value = false;
  sidebarDragStartX.value = null;
};

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
