<template>
  <article class="card" @click="$emit('click')">
    <h2 class="card__title">{{ post.title }}</h2>
    <p class="card__preview">
      {{ previewText }}
    </p>
    <div class="card__meta">
      <span class="card__date">{{ formattedDate }}</span>
    </div>
  </article>
</template>

<script setup lang="ts">
import { computed } from "vue";
import type { Post } from "../api";

const props = defineProps<{
  post: Post;
}>();

const previewText = computed(() =>
  props.post.text.length > 140 ? props.post.text.slice(0, 140) + "…" : props.post.text,
);

const formattedDate = computed(() =>
  new Date(props.post.created_at).toLocaleString(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  }),
);
</script>

<style scoped>
.card {
  padding: 1.25rem 1.5rem;
  border-radius: 1rem;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.5);
  cursor: pointer;
  transition:
    transform 0.15s ease,
    box-shadow 0.15s ease,
    border-color 0.15s ease,
    background 0.15s ease;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.8);
  border-color: #38bdf8;
  background: rgba(15, 23, 42, 0.95);
}

.card__title {
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: #e5e7eb;
}

.card__preview {
  margin: 0 0 0.75rem;
  font-size: 0.9rem;
  line-height: 1.5;
  color: #cbd5f5;
}

.card__meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.8rem;
  color: #9ca3af;
}

.card__date {
  white-space: nowrap;
}
</style>

