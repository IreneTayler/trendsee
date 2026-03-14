<template>
  <aside class="flex w-64 flex-col bg-slate-900 px-4 py-5 text-slate-100">
    <div class="mb-4 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <img :src="logoUrl" alt="trendsee" class="h-7 object-contain" />
        <span class="text-xs text-slate-400">Beta</span>
      </div>
      <button type="button" class="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-600 text-white hover:bg-indigo-500">+</button>
    </div>

    <input
      type="text"
      placeholder="Поиск контента"
      class="mb-4 w-full rounded-lg border border-slate-700 bg-slate-800 px-3 py-2 text-sm text-white placeholder-slate-400 focus:border-indigo-500 focus:outline-none"
    />

    <nav class="flex-1 space-y-4">
      <SidebarGroup>
        <template #label>Поиск контента</template>
        <SidebarItem active>Главная</SidebarItem>
        <SidebarItem>Видео</SidebarItem>
        <SidebarItem>Шпионаж</SidebarItem>
        <SidebarItem badge="712">Контент радар</SidebarItem>
      </SidebarGroup>
      <SidebarGroup>
        <template #label>Работа с соцсетями</template>
        <SidebarItem>Кросс-постинг</SidebarItem>
        <SidebarItem>Чат боты</SidebarItem>
      </SidebarGroup>
      <SidebarGroup>
        <template #label>Инструменты</template>
        <SidebarItem>ИИ-сценарий</SidebarItem>
        <SidebarItem>Карусели</SidebarItem>
        <SidebarItem>Анализ видео</SidebarItem>
        <SidebarItem>Анализ профиля</SidebarItem>
        <SidebarItem badge="Скоро">Черновик</SidebarItem>
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
</script>
