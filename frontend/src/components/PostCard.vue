<template>
  <article class="post-card cursor-pointer overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm transition hover:shadow-md" @click="$emit('click')">
    <div class="post-card__media">
      <img v-if="imageSrc" :src="imageSrc" alt="" class="post-card__img" />
      <div v-else class="post-card__media-placeholder" />
      <div class="post-card__badges post-card__badges--left">
        <span class="post-card__badge"><span class="post-card__badge-icon">▶</span> Reels</span>
        <span class="post-card__badge"><span class="post-card__badge-icon">🔥</span> X10</span>
      </div>
      <div class="post-card__badges post-card__badges--right">
        <span class="post-card__action-icon">♡</span>
        <span class="post-card__action-icon">↗</span>
      </div>
      <div class="post-card__metrics">
        <span class="post-card__metric">👁 105k</span>
        <span class="post-card__metric">♡ 85k</span>
        <span class="post-card__metric">💬 15k</span>
        <span class="post-card__metric">↗ 485</span>
      </div>
    </div>
    <div class="post-card__body">
      <div class="post-card__profile">
        <div class="post-card__avatar">B</div>
        <div class="post-card__profile-text">
          <span class="post-card__username">@blogerich</span>
          <span class="post-card__followers">384.5K</span>
        </div>
      </div>
      <h2 class="post-card__title">{{ post.title }}</h2>
      <p class="post-card__preview">{{ previewText }}</p>
      <p class="post-card__date">{{ formattedDate }}</p>
      <button type="button" class="post-card__cta" @click.stop="$emit('click')">Анализ</button>
    </div>
  </article>
</template>

<script setup lang="ts">
import { computed } from "vue";
import type { Post } from "../api";
const props = defineProps<{ post: Post; imageSrc?: string }>();
defineEmits<{ (e: "click"): void }>();
const previewText = computed(() => (props.post.text.length > 140 ? props.post.text.slice(0, 140) + "…" : props.post.text));
const formattedDate = computed(() => new Date(props.post.created_at).toLocaleDateString("ru-RU", { day: "2-digit", month: "2-digit", year: "numeric" }));
</script>

<style scoped>
.post-card { width: 100%; }
.post-card__media { position: relative; padding-top: 160%; background: linear-gradient(160deg, #e2e8f0, #cbd5e1); }
.post-card__media-placeholder { position: absolute; inset: 0; }
.post-card__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.post-card__badges { position: absolute; display: flex; flex-direction: column; gap: 6px; }
.post-card__badges--left { top: 10px; left: 10px; }
.post-card__badges--right { top: 10px; right: 10px; }
.post-card__badge { display: inline-flex; align-items: center; gap: 4px; padding: 4px 10px; border-radius: 999px; background: rgba(15,23,42,.75); color: #fff; font-size: 11px; }
.post-card__action-icon { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 8px; background: rgba(15,23,42,.6); color: #fff; font-size: 14px; }
.post-card__metrics { position: absolute; left: 10px; right: 10px; bottom: 10px; display: flex; justify-content: space-between; padding: 8px 12px; border-radius: 999px; background: linear-gradient(90deg, rgba(15,23,42,.88), rgba(15,23,42,.72)); color: #fff; font-size: 11px; }
.post-card__body { padding: 12px 14px 14px; }
.post-card__profile { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
.post-card__avatar { width: 36px; height: 36px; border-radius: 999px; background: linear-gradient(135deg, #f97316, #ec4899 50%, #6366f1); color: #fff; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.post-card__profile-text { display: flex; flex-direction: column; flex: 1; min-width: 0; }
.post-card__username { font-size: 13px; font-weight: 600; color: #4338ca; }
.post-card__followers { font-size: 11px; color: #64748b; }
.post-card__title { margin: 0 0 6px; font-size: 14px; font-weight: 600; color: #0f172a; line-height: 1.3; }
.post-card__preview { margin: 0 0 8px; font-size: 13px; line-height: 1.45; color: #334155; }
.post-card__date { margin: 0 0 12px; font-size: 11px; color: #94a3b8; }
.post-card__cta { width: 100%; padding: 10px 16px; border: none; border-radius: 999px; background: #4338ca; color: #fff; font-size: 14px; font-weight: 600; cursor: pointer; }
.post-card__cta:hover { background: #3730a3; }
</style>
