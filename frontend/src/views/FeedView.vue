<template>
  <section class="space-y-4 pb-24">
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

    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4" ref="feedRoot">
      <PostCard
        v-for="post in posts"
        :key="post.id"
        :post="post"
        :image-src="cardImage"
        @click="openPost(post, cardImage)"
        @analyze="openPost"
      />
      <template v-if="isLoading && posts.length === 0">
        <article
          v-for="i in 8"
          :key="'skeleton-' + i"
          class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm"
        >
          <div class="relative pt-[160%] bg-slate-200">
            <div class="absolute inset-0 animate-pulse bg-slate-300/60" />
          </div>
          <div class="space-y-3 p-3">
            <div class="flex items-center gap-2">
              <div class="h-9 w-9 shrink-0 animate-pulse rounded-full bg-slate-200" />
              <div class="flex-1 space-y-1">
                <div class="h-3 w-20 animate-pulse rounded bg-slate-200" />
                <div class="h-2.5 w-14 animate-pulse rounded bg-slate-100" />
              </div>
            </div>
            <div class="h-3.5 w-full max-w-[90%] animate-pulse rounded bg-slate-200" />
            <div class="h-3 w-[80%] animate-pulse rounded bg-slate-100" />
            <div class="h-2.5 w-16 animate-pulse rounded bg-slate-100" />
            <div class="h-10 w-full animate-pulse rounded-xl bg-slate-200" />
          </div>
        </article>
      </template>
      <div v-else-if="isLoading" class="col-span-full flex items-center justify-center gap-3 py-8 text-sm text-slate-500">
        <span class="inline-flex h-8 w-8 animate-spin rounded-full border-2 border-slate-200 border-t-indigo-500" />
        <span>Загрузка...</span>
      </div>
      <p v-if="!hasMore && posts.length > 0" class="col-span-full text-center text-xs text-slate-400">Вы дошли до конца ленты.</p>
    </div>

    <!-- When there are cards: inline find-more + counter -->
    <div v-if="posts.length > 0" class="mt-8 flex flex-wrap items-center justify-center gap-4">
      <button type="button" class="inline-flex items-center gap-2 rounded-xl bg-indigo-600 px-6 py-3 text-white hover:bg-indigo-700">
        <span>⚡</span>
        Найти еще ролики
      </button>
      <span class="text-sm text-slate-500">
        Видео: {{ posts.length }}<span v-if="totalCount !== null"> из {{ totalCount }}</span>
      </span>
    </div>

    <!-- When no cards: button fixed at bottom of viewport -->
    <div
      v-if="posts.length === 0 && !isLoading"
      class="fixed bottom-0 left-0 right-0 z-40 flex justify-center py-4"
    >
      <button type="button" class="inline-flex items-center gap-2 rounded-xl bg-indigo-600 px-6 py-3 text-white hover:bg-indigo-700">
        <span>⚡</span>
        Найти еще ролики
      </button>
    </div>

    <PostModal
      :visible="isModalOpen"
      :post="selectedPost"
      :image-src="selectedImageSrc"
      :loading="isPostRevealLoading"
      @close="isModalOpen = false"
    />
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import { fetchUserPosts, fetchUserPostCount, type Post } from "../api";
import PostCard from "../components/PostCard.vue";
import PostModal from "../components/PostModal.vue";
import cardImage from "../imgs/image.png";

const posts = ref<Post[]>([]);
const page = ref(0);
const limit = 10;
const isLoading = ref(false);
const hasMore = ref(true);
const totalCount = ref<number | null>(null);
const userId = ref<number>(1);
const isModalOpen = ref(false);
const selectedPost = ref<Post | null>(null);
const selectedImageSrc = ref<string | undefined>(undefined);
const isPostRevealLoading = ref(false);

function openPost(post: Post, imageSrc?: string) {
  isModalOpen.value = true;
  isPostRevealLoading.value = true;
  selectedPost.value = null;
  selectedImageSrc.value = imageSrc;
  // Give a short, intentional reveal animation (improves perceived performance)
  window.setTimeout(() => {
    selectedPost.value = post;
    isPostRevealLoading.value = false;
  }, 220);
}

async function loadMore() {
  if (isLoading.value || !hasMore.value) return;
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

async function loadInitial() {
  if (!userId.value || userId.value < 1) return;
  isLoading.value = true;
  posts.value = [];
  page.value = 0;
  hasMore.value = true;
  try {
    const [count, data] = await Promise.all([
      fetchUserPostCount(userId.value),
      fetchUserPosts(userId.value, limit, 0),
    ]);
    totalCount.value = count;
    posts.value = data;
    page.value = 1;
    if (data.length < limit) hasMore.value = false;
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
  loadInitial();
  window.addEventListener("scroll", handleScroll, { passive: true });
});
onUnmounted(() => window.removeEventListener("scroll", handleScroll));
watch(userId, () => {
  totalCount.value = null;
  if (!userId.value || userId.value < 1) {
    posts.value = [];
    return;
  }
  loadInitial();
});
</script>
