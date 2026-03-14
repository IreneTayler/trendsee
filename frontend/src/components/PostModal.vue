<template>
  <Teleport to="body">
    <Transition name="fade">
      <div v-if="visible" class="fixed inset-0 z-40 flex items-end justify-center bg-slate-900/60 backdrop-blur-sm sm:items-center" @click.self="onClose">
        <Transition name="slide-up">
          <div class="max-h-[90vh] w-full max-w-2xl overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-2xl">
            <header class="flex items-start justify-between gap-4 border-b border-slate-100 p-4">
              <div>
                <h2 class="mb-1 text-lg font-semibold text-slate-900">{{ post?.title }}</h2>
                <p class="flex flex-wrap gap-x-4 text-xs text-slate-500">
                  <span>User #{{ post?.user_id }}</span>
                  <span>Created: {{ createdAt }}</span>
                  <span>Updated: {{ updatedAt }}</span>
                </p>
              </div>
              <button type="button" class="inline-flex h-8 w-8 items-center justify-center rounded-full text-slate-400 hover:bg-slate-100 hover:text-slate-700" @click="onClose">✕</button>
            </header>
            <section class="max-h-[60vh] overflow-y-auto px-4 pb-4 pt-2">
              <p class="whitespace-pre-wrap text-sm leading-relaxed text-slate-800">{{ post?.text }}</p>
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
const props = defineProps<{ visible: boolean; post: Post | null }>();
const emit = defineEmits<{ (e: "close"): void }>();
const onClose = () => emit("close");
const createdAt = computed(() => props.post ? new Date(props.post.created_at).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" }) : "");
const updatedAt = computed(() => props.post ? new Date(props.post.updated_at).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" }) : "");
</script>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
.slide-up-enter-active, .slide-up-leave-active { transition: transform 0.22s ease, opacity 0.22s ease; }
.slide-up-enter-from, .slide-up-leave-to { transform: translateY(12px); opacity: 0; }
</style>
