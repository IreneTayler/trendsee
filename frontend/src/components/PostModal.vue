<template>
  <Teleport to="body">
    <Transition name="fade">
      <div v-if="visible" class="overlay" @click.self="onClose">
        <Transition name="slide-up">
          <div class="modal">
            <button class="modal__close" @click="onClose" aria-label="Close">
              ✕
            </button>
            <header class="modal__header">
              <h2 class="modal__title">{{ post?.title }}</h2>
              <p class="modal__meta">
                <span>User #{{ post?.user_id }}</span>
                <span>Created: {{ createdAt }}</span>
                <span>Updated: {{ updatedAt }}</span>
              </p>
            </header>
            <section class="modal__body">
              <p class="modal__text">
                {{ post?.text }}
              </p>
            </section>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { computed } from "vue";
import type { Post } from "../api";

const props = defineProps<{
  visible: boolean;
  post: Post | null;
}>();

const emit = defineEmits<{
  (e: "close"): void;
}>();

const onClose = () => emit("close");

const createdAt = computed(() =>
  props.post
    ? new Date(props.post.created_at).toLocaleString(undefined, {
        dateStyle: "medium",
        timeStyle: "short",
      })
    : "",
);

const updatedAt = computed(() =>
  props.post
    ? new Date(props.post.updated_at).toLocaleString(undefined, {
        dateStyle: "medium",
        timeStyle: "short",
      })
    : "",
);
</script>

<style scoped>
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.8);
  backdrop-filter: blur(12px);
  display: flex;
  justify-content: center;
  align-items: flex-end;
  padding: 2rem 1rem;
  z-index: 40;
}

.modal {
  position: relative;
  max-width: 720px;
  width: 100%;
  border-radius: 1.25rem;
  background: #020617;
  border: 1px solid rgba(148, 163, 184, 0.6);
  padding: 1.75rem 1.75rem 1.5rem;
  box-shadow:
    0 24px 80px rgba(15, 23, 42, 0.9),
    0 0 0 1px rgba(15, 23, 42, 0.9);
  color: #e5e7eb;
}

.modal__close {
  position: absolute;
  top: 1rem;
  right: 1.25rem;
  border: none;
  background: transparent;
  color: #9ca3af;
  cursor: pointer;
  font-size: 1.1rem;
  padding: 0.25rem;
  border-radius: 999px;
  transition:
    background 0.15s ease,
    color 0.15s ease;
}

.modal__close:hover {
  background: rgba(15, 23, 42, 0.8);
  color: #e5e7eb;
}

.modal__header {
  margin-bottom: 1rem;
}

.modal__title {
  margin: 0 0 0.5rem;
  font-size: 1.4rem;
  font-weight: 600;
}

.modal__meta {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
  font-size: 0.8rem;
  color: #9ca3af;
}

.modal__body {
  max-height: min(60vh, 460px);
  overflow-y: auto;
  padding-right: 0.5rem;
}

.modal__text {
  white-space: pre-wrap;
  line-height: 1.6;
  font-size: 0.95rem;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-up-enter-active,
.slide-up-leave-active {
  transition:
    transform 0.22s ease,
    opacity 0.22s ease;
}

.slide-up-enter-from,
.slide-up-leave-to {
  transform: translateY(12px);
  opacity: 0;
}

@media (min-width: 640px) {
  .overlay {
    align-items: center;
  }
}
</style>

