<template>
  <aside class="fixed top-0 left-0 h-screen text-white flex w-64 flex-col bg-[#f4f5f6] px-4 py-5 text-slate-100 ">
    <div class="mb-4 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <img :src="logoUrl" alt="trendsee" class="h-7 object-contain" />
      </div>
      <button type="button" class="flex size-[20px] justify-end">
        <img :src="iconLeadingLeft" alt="trendsee" class="size-[15px]" />
      </button>
    </div>

    <nav class="flex-1 space-y-4">
      <SidebarGroup>
        <template #label class="text-lowercase">
          <div class="text-[#839397] text-sm text-lowercase">Поиск контента</div>
        </template>
        <SidebarItem :image="'src/imgs/Vector.png'">Главная</SidebarItem>
        <SidebarItem :image="'src/imgs/Vector (1).png'">Видео</SidebarItem>
        <SidebarItem :image="'src/imgs/Vector (2).png'">Шпионаж</SidebarItem>
        <SidebarItem :image="'src/imgs/Vector (3).png'" badge="712">Контент радар</SidebarItem>
      </SidebarGroup :image="'src/imgs/Vector (4).png'">
      <SidebarGroup>
        <template #label class="text-lowercase">
          <div class="text-[#839397] text-sm text-lowercase">соцсетями</div>
        </template>
        <SidebarItem :image="'src/imgs/Vector (5).png'">Кросс-постинг</SidebarItem>
        <SidebarItem :image="'src/imgs/Vector (6).png'">Чат боты</SidebarItem>
      </SidebarGroup>
      <SidebarGroup>        
        <template #label class="text-lowercase">
          <div class="text-[#839397] text-sm text-lowercase">Инструменты</div>
        </template>
        <SidebarItem :image="'src/imgs/Vector (7).png'">ИИ-сценарий</SidebarItem>
        <SidebarItem :image="'src/imgs/Vector (8).png'">Карусели</SidebarItem>
        <SidebarItem :image="'src/imgs/Vector (9).png'">Анализ видео</SidebarItem>
        <SidebarItem :image="'src/imgs/Vector (10).png'">Анализ профиля</SidebarItem>
        <SidebarItem :image="'src/imgs/Vector (11).png'" badge="Скоро">Черновик</SidebarItem>
      </SidebarGroup>
    </nav>

    <div class="mt-4 space-y-3 border-t border-slate-700 pt-4">
      <div>
        <p class="mb-1 text-xs font-medium text-red-400">Токены</p>
        <p class="text-xs text-slate-400">1 245 / 4 497</p>
        <div class="mt-1 h-1.5 w-full overflow-hidden rounded-full bg-slate-700">
          <div class="h-full w-[28%] rounded-full bg-indigo-500" />
        </div>
      </div>
      <button type="button" class="flex w-full items-center justify-between text-xs text-slate-400 hover:text-white">
        Creative +
        <span>→</span>
      </button>
      <div class="flex items-center gap-3 rounded-lg bg-slate-800/80 p-2">
        <div class="h-10 w-10 flex-shrink-0 rounded-full bg-gradient-to-br from-indigo-500 to-pink-500" />
        <div class="min-w-0 flex-1">
          <p class="truncate text-sm font-medium text-white">Александра</p>
          <p class="truncate text-xs text-slate-400">+7 (999) 999-99-99</p>
        </div>
        <span class="text-xs text-slate-500">RU</span>
        <button type="button" class="text-slate-400 hover:text-white" aria-label="Выход">↗</button>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
import SidebarGroup from "./SidebarGroup.vue";
import SidebarItem from "./SidebarItem.vue";
import logoUrl from "../imgs/Logo full.png";
import iconLeadingLeft from "../imgs/Icon_leading_left.png";
</script>
