<template>
  <article
    class="min-w-[220px] max-w-[262px] h-[576px] w-full cursor-pointer overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm transition-shadow hover:shadow-md"
    @click="$emit('click')"
  >
    <div class="relative h-[400px] bg-gradient-to-br from-slate-200 to-slate-300">
      <img :src="resolvedImageSrc" alt="" class="absolute inset-0 h-full w-full object-cover" />

      <!-- Left badges -->
      <div class="absolute left-2.5 top-2.5 flex flex-col gap-1.5">
        <span class="inline-flex items-center gap-1 rounded-lg bg-black/40 px-2.5 py-1 text-xs text-white backdrop-blur-xl">
          <img :src="socialMediaLogos" alt="trendsee" class="size-4" />
          Reels
        </span>
        <span class="inline-flex items-center gap-1 rounded-lg bg-black/40 px-2.5 py-1 text-xs text-white backdrop-blur-xl">
          <img :src="whiteFire" alt="trendsee" class="h-4" />
          X10
        </span>
      </div>

      <!-- Right icons -->
      <div class="absolute right-2.5 top-2.5 flex flex-col gap-1.5">
        <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-slate-900/60">
          <img :src="Heart" alt="trendsee" class="size-4" />
        </span>
        <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-slate-900/60">
          <img :src="externalLink" alt="trendsee" class="size-4" />
        </span>
      </div>

      <!-- Bottom metrics -->
      <div class="absolute bottom-2.5 left-2.5 right-2.5 flex justify-between rounded-xl bg-black/30 px-4 py-2 text-xs text-white backdrop-blur-md">
        <div class="flex-col items-center gap-1.5">
          <img :src="eye" alt="" />
          <span>105k</span>
        </div>
        <div class="flex-col items-center gap-1.5">
          <div class="size-5" >
            <img :src="Heart" alt="" />
          </div>
          <span>85k</span>
        </div>
        <div class="flex-col items-center gap-1.5">
          <div class="size-5" >
            <img :src="comments" alt="" />
          </div>
          <span>15k</span>
        </div>
        <div class="flex-col items-center gap-1.5">
          <div class="size-5" >
            <img :src="shares" alt="" />
          </div>
          <span>485</span>
        </div>
      </div>
    </div>

    <div class="px-3.5 pb-3.5 pt-1">
      <div class="flex items-center gap-2">
        <img :src="image1" alt="" class="size-10 rounded-full" />
        <div class="min-w-0 flex-1">
          <div class="text-sm font-semibold text-[#2b31b3]">@blogerich</div>
          <div class="text-xs text-[#4e616b]">384.5K</div>
        </div>
        <div class="flex items-center gap-1">
          <div class="size-3" >
            <img :src="plus" alt="" />
          </div>
          <div class="size-6" >
            <img :src="incognitoMode" alt="" />
          </div>
        </div>
      </div>

      <p
        class="mt-3 mb-3 text-xs leading-[1.45] text-slate-700 [display:-webkit-box] [-webkit-box-orient:vertical] [-webkit-line-clamp:2] overflow-hidden"
      >
        {{ previewText }}
      </p>
      <p class="text-[11px] text-slate-400">{{ formattedDate }}</p>
      <button
        type="button"
        class="mt-2 w-full rounded-xl bg-indigo-700 px-4 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-indigo-800"
        @click.stop="$emit('analyze', post, imageSrc)"
      >
        Анализ
      </button>
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
