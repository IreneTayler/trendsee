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

    <div class="flex-1 space-y-4 mt-6 p-4 bg-white rounded-xl">
      <div class="flex justify-between">
        <div class="flex">
          <img :src="Fire" alt="trendsee" class="h-[24px] w-[24px]" />
          <p class="mb-1 text-sm font-bold italic text-[#4e616b]">Токены</p>
        </div>
        <p class="text-sm text-[#4e616b]">1 245 / 4 497</p>
      </div>
      <div>
        <div class="mt-1 h-1.5 w-full overflow-hidden rounded-full bg-slate-700">
          <div class="h-full w-[28%] rounded-full bg-indigo-500" />
        </div>
      </div>
      <button type="button" class="flex w-full items-center justify-between text-base text-[#4e616b] hover:text-white">
        Creative +
        <span><img :src="iconLeadingRight" alt="trendsee" class="size-[20px]" /></span>
      </button>
    </div>

    <div class="flex items-center space-y-4 gap-3 p-2">
      <div class="flex-shrink-0 from-indigo-500 to-pink-500" >
        <img :src="image1" alt="trendsee" class="size-[30px] rounded-full" />
      </div>
      <div class="min-w-0 flex-1">
        <p class="truncate text-base text-[#41616b]">Александра</p>
        <p class="truncate text-xs text-slate-400">+7 (999) 999-99-99</p>
      </div>
      <button type="button" class="text-slate-400 hover:text-white" aria-label="Выход">
        <img :src="iconLeadingRightMore" alt="trendsee" class="size-[15px]" />          
      </button>
    </div>

    <div class="flex items-end space-y-4 gap-3 pl-2">       
        <img :src="RU" alt="trendsee" class="size-[20px]" /> 
        <span class="text-xs text-slate-500">RU</span>
        <img :src="iconLeadingDown" alt="trendsee" class="size-[15px]" /> 
    </div>

    
  </aside>
</template>

<script setup lang="ts">
import SidebarGroup from "./SidebarGroup.vue";
import SidebarItem from "./SidebarItem.vue";
import logoUrl from "../imgs/Logo full.png";
import iconLeadingLeft from "../imgs/Icon_leading_left.png";
import Fire from "../imgs/Fire.png";
import iconLeadingRight from "../imgs/Icon_leading_right.png";
import image1 from "../imgs/image1.png";
import iconLeadingRightMore from "../imgs/Icon_leading_right_more.png";
import RU from "../imgs/RU.png";
import iconLeadingDown from "../imgs/Icon_leading_down.png";
</script>
