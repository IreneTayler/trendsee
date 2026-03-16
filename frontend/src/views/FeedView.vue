<template>
  <section class="space-y-4">
    <header class="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
      <label class="flex flex-col text-xs font-medium text-slate-500">
        <span class="mb-1">User ID</span>
        <input
          v-model.number="userId"
          type="number"
          min="1"
          class="w-24 rounded-lg border border-slate-300 px-2 py-1 text-sm text-slate-900"
        />
      </label>
    </header>

    <!-- Row label like in design: date + Анализ -->
    <div class="flex flex-wrap items-center gap-3 text-sm text-slate-500">
      <span>12.12.2025</span>
      <button type="button" class="rounded-lg bg-indigo-600 px-4 py-2 text-white hover:bg-indigo-700">Анализ</button>
    </div>

    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4" ref="feedRoot">
      <PostCard
        v-for="post in posts"
        :key="post.id"
        :post="post"
        :image-src="cardImage"
        @click="openPost(post, cardImage)"
        @analyze="openPost"
      />
      <div v-if="isLoading" class="col-span-full flex items-center justify-center gap-2 text-sm text-slate-500">
        <span class="h-4 w-4 animate-spin rounded-full border-2 border-slate-300 border-t-sky-400" /> Загрузка…
      </div>
      <p v-if="!hasMore && posts.length > 0" class="col-span-full text-center text-xs text-slate-400">Вы дошли до конца ленты.</p>
    </div>

    <!-- Find more reels + progress like in design -->
    <div class="mt-8 flex flex-wrap items-center justify-center gap-4">
      <button type="button" class="inline-flex items-center gap-2 rounded-xl bg-indigo-600 px-6 py-3 text-white hover:bg-indigo-700">
        <span>⚡</span>
        Найти еще ролики
      </button>
      <span class="text-sm text-slate-500">Видео: {{ posts.length }} из 3000</span>
    </div>

    <PostModal :visible="isModalOpen" :post="selectedPost" :image-src="selectedImageSrc" @close="isModalOpen = false" />
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import { fetchUserPosts, type Post } from "../api";
import PostCard from "../components/PostCard.vue";
import PostModal from "../components/PostModal.vue";
import cardImage from "../imgs/image.png";

const posts = ref<Post[]>([]);
const page = ref(0);
const limit = 10;
const isLoading = ref(false);
const hasMore = ref(true);
const userId = ref<number>(1);
const isModalOpen = ref(false);
const selectedPost = ref<Post | null>(null);
const selectedImageSrc = ref<string | undefined>(undefined);

function openPost(post: Post, imageSrc?: string) {
  selectedPost.value = post;
  selectedImageSrc.value = imageSrc;
  isModalOpen.value = true;
}

async function loadMore() {
  if (isLoading.value || !hasMore.value) return;
  // Don't call backend if userId is not valid yet
  if (!userId.value || userId.value < 1) return;
  isLoading.value = true;
  try {
    const offset = page.value * limit;
    const data = await fetchUserPosts(userId.value, limit, offset);
    if (data.length < limit) hasMore.value = false;
    posts.value.push(...data);
    page.value += 1;
  } catch (e) {
    console.error(e);
    hasMore.value = false;
  } finally {
    isLoading.value = false;
  }
}

function handleScroll() {
  const el = document.documentElement;
  if (el.scrollHeight - (window.scrollY + el.clientHeight) < 500) loadMore();
}

onMounted(() => {
  loadMore();
  window.addEventListener("scroll", handleScroll, { passive: true });
});
onUnmounted(() => window.removeEventListener("scroll", handleScroll));
watch(userId, () => {
  posts.value = [];
  page.value = 0;
  hasMore.value = true;
  loadMore();
});
</script>
