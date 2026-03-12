<template>
  <section>
    <header class="feed-header">
      <div>
        <h2 class="feed-header__title">Your posts</h2>
        <p class="feed-header__subtitle">
          Infinite scroll feed with cached backend. Demo user: <code>#1</code>
        </p>
      </div>
      <div class="feed-header__controls">
        <label class="feed-header__field">
          <span>User ID</span>
          <input v-model.number="userId" type="number" min="1" />
        </label>
      </div>
    </header>

    <div class="feed" ref="feedContainer">
      <PostCard
        v-for="post in posts"
        :key="post.id"
        :post="post"
        @click="openPost(post)"
      />

      <p v-if="!isLoading && posts.length === 0" class="feed__empty">
        No posts yet for this user.
      </p>

      <div v-if="isLoading" class="feed__loader">
        <span class="spinner" /> Loading…
      </div>

      <p v-if="!hasMore && posts.length > 0" class="feed__end">
        You have reached the end.
      </p>
    </div>

    <PostModal :visible="isModalOpen" :post="selectedPost" @close="isModalOpen = false" />
  </section>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref, watch } from "vue";
import { fetchUserPosts, type Post } from "../api";
import PostCard from "../components/PostCard.vue";
import PostModal from "../components/PostModal.vue";

const posts = ref<Post[]>([]);
const page = ref(0);
const limit = 10;
const isLoading = ref(false);
const hasMore = ref(true);
const userId = ref<number>(1);

const isModalOpen = ref(false);
const selectedPost = ref<Post | null>(null);

const feedContainer = ref<HTMLElement | null>(null);

async function loadMore() {
  if (isLoading.value || !hasMore.value) return;
  isLoading.value = true;
  try {
    const offset = page.value * limit;
    const data = await fetchUserPosts(userId.value, limit, offset);
    if (data.length < limit) {
      hasMore.value = false;
    }
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
  const scrollElement = document.documentElement;
  const scrollTop = window.scrollY || scrollElement.scrollTop;
  const viewportHeight = window.innerHeight || scrollElement.clientHeight;
  const fullHeight = scrollElement.scrollHeight;

  if (fullHeight - (scrollTop + viewportHeight) < 500) {
    loadMore();
  }
}

function openPost(post: Post) {
  selectedPost.value = post;
  isModalOpen.value = true;
}

onMounted(() => {
  loadMore();
  window.addEventListener("scroll", handleScroll, { passive: true });
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});

watch(userId, () => {
  posts.value = [];
  page.value = 0;
  hasMore.value = true;
  loadMore();
});
</script>

<style scoped>
.feed-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.feed-header__title {
  margin: 0 0 0.25rem;
  font-size: 1.4rem;
  font-weight: 600;
}

.feed-header__subtitle {
  margin: 0;
  font-size: 0.9rem;
  color: #9ca3af;
}

.feed-header__controls {
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.feed-header__field {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  font-size: 0.8rem;
  color: #9ca3af;
}

.feed-header__field input {
  padding: 0.3rem 0.5rem;
  border-radius: 0.5rem;
  border: 1px solid rgba(148, 163, 184, 0.6);
  background: rgba(15, 23, 42, 0.9);
  color: #e5e7eb;
  width: 5rem;
}

.feed {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.feed__loader,
.feed__end,
.feed__empty {
  text-align: center;
  margin-top: 1.5rem;
  font-size: 0.9rem;
  color: #9ca3af;
}

.spinner {
  display: inline-block;
  width: 1rem;
  height: 1rem;
  border-radius: 999px;
  border: 2px solid rgba(148, 163, 184, 0.5);
  border-top-color: #38bdf8;
  margin-right: 0.5rem;
  animation: spin 0.7s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 640px) {
  .feed-header {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>

