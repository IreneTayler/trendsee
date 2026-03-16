<template>
  <article class="post-card cursor-pointer overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm transition hover:shadow-md" @click="$emit('click')">
    <div class="post-card__media">
      <img :src="resolvedImageSrc" alt="" class="post-card__img" />
      <div class="post-card__badges post-card__badges--left">
        <span class="post-card__badge">
          <span><img :src="socialMediaLogos" alt="trendsee" class="size-[16px]" /> </span> 
          Reels
        </span>
        <span class="post-card__badge">
          <span><img :src="whiteFire" alt="trendsee" class="h-[16px]" /> </span> 
          X10
        </span>
      </div>
      <div class="post-card__badges post-card__badges--right">
        <span class="post-card__action-icon">
          <img :src="Heart" alt="trendsee" class="size-[16px]" />
        </span>
        <span class="post-card__action-icon">
          <img :src="externalLink" alt="trendsee" class="size-[16px]" />
        </span>
      </div>
      <div class="post-card__metrics">
        <div class="post-card__metric">
          <div  class="size-[20px]" ><img :src="eye" alt=""/></div> 
          <div class="text-xs">105k</div>
        </div>
        <div class="post-card__metric">
          <div  class="size-[20px]" ><img :src="Heart" alt=""/></div> 
          <div class="text-xs">85k</div>
        </div>
        <div class="post-card__metric">
          <div  class="size-[20px]" ><img :src="comments" alt=""/></div> 
          <div class="text-xs">15k</div>
        </div>
        <div class="post-card__metric">
          <div  class="size-[20px]" ><img :src="shares" alt=""/></div> 
          <div class="text-xs">485</div>
        </div>
      </div>
    </div>
    <div class="post-card__body">
      <div class="post-card__profile">
        <div class="">
          <img :src="image1" alt="" class="size-[40px] post-card__avatar" />          
        </div>
        <div class="post-card__profile-text">
          <span class="post-card__username">@blogerich</span>
          <span class="post-card__followers">384.5K</span>
        </div>
        <div class="size-[24px]">
          <img :src="incognitoMode" alt=""  />          
          <img :src="plus" alt=""  />          
        </div>
      </div>
      <h2 class="post-card__title">{{ post.title }}</h2>
      <p class="post-card__preview">{{ previewText }}</p>
      <p class="post-card__date">{{ formattedDate }}</p>
      <button type="button" class="post-card__cta" @click.stop="$emit('analyze', post, imageSrc)">Анализ</button>
    </div>
  </article>
  
</template>

<script setup lang="ts">
import { computed } from "vue";
import type { Post } from "../api";
const props = defineProps<{ post: Post; imageSrc?: string }>();
defineEmits<{ (e: "analyze", post: Post, imageSrc?: string): void; (e: "click"): void }>();
const previewText = computed(() => {
  const base = props.post.text && props.post.text.trim().length > 0 ? props.post.text : props.post.title;
  return base.length > 140 ? base.slice(0, 140) + "…" : base;
});
const formattedDate = computed(() =>
  new Date(props.post.created_at).toLocaleDateString("ru-RU", { day: "2-digit", month: "2-digit", year: "numeric" }),
);

const resolvedImageSrc = computed(() => props.imageSrc ?? cardImage);

import socialMediaLogos from "../imgs/Social media Logos.png";
import whiteFire from "../imgs/white_fire.png";
import Heart from "../imgs/Heart.png";
import externalLink from "../imgs/External Link.png";
import eye from "../imgs/eye.png";
import comments from "../imgs/Comments.png";
import shares from "../imgs/Shares.png";
import image1 from "../imgs/image1.png";
import cardImage from "../imgs/image.png";
import incognitoMode from "../imgs/Incognito_mode.png";
import plus from "../imgs/plus.png";
</script>

<style scoped>
.post-card { width: 100%; }
.post-card__media { position: relative; padding-top: 160%; background: linear-gradient(160deg, #e2e8f0, #cbd5e1); }
.post-card__media-placeholder { position: absolute; inset: 0; }
.post-card__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.post-card__badges { position: absolute; display: flex; flex-direction: column; gap: 6px; }
.post-card__badges--left { top: 10px; left: 10px; }
.post-card__badges--right { top: 10px; right: 10px; }
.post-card__badge { display: inline-flex; align-items: center; gap: 4px; padding: 4px 10px; border-radius: 8px; background: var(--Black-40, #00000066); backdrop-filter: blur(16px); color: #fff; font-size: 12px; }
.post-card__action-icon { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 8px; background: rgba(15,23,42,.6); color: #fff; font-size: 14px; }
.post-card__metrics { position: absolute; left: 10px; right: 10px; bottom: 10px; display: flex; justify-content: space-between; padding: 8px 16px; border-radius: 12px; background: var(--Black-30, #0000004D); backdrop-filter: blur(8px); color: #fff; font-size: 12px; }
.post-card__body { padding: 12px 14px 14px; }
.post-card__profile { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
.post-card__avatar { width: 36px; height: 36px; border-radius: 999px; background: linear-gradient(135deg, #f97316, #ec4899 50%, #6366f1); color: #fff; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.post-card__profile-text { display: flex; flex-direction: column; flex: 1; min-width: 0; }
.post-card__username { font-size: 14px; font-weight: 600; color: #2b31b3; }
.post-card__followers { font-size: 12px; color: #4e616b; }
.post-card__title { margin: 0 0 6px; font-size: 14px; font-weight: 600; color: #0f172a; line-height: 1.3; }
.post-card__preview { margin: 0 0 8px; font-size: 12px; line-height: 1.45; color: #334155; }
.post-card__date { margin: 0 0 12px; font-size: 11px; color: #94a3b8; }
.post-card__cta { width: 100%; padding: 10px 16px; border: none; border-radius: 12px; background: #4338ca; color: #fff; font-size: 14px; font-weight: 600; cursor: pointer; }
.post-card__cta:hover { background: #3730a3; }

</style>
