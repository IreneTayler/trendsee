<template>
  <li>
    <button
      type="button"
      class="flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-left text-[16px] h-[40px] hover:bg-[#41616b92] text-[#41616b]"
      :class="active ? 'bg-indigo-600 font-medium' : ''"
      @click="$emit('click')"
    >
      <!-- Render image passed as prop -->
      <img v-if="image" :src="image" alt="Image" class="w-[20px] h-[20px]" />

      <!-- Render text passed via default slot -->
      <span><slot /></span>

      <!-- Render badge if provided -->
      <span v-if="badge" class="ml-auto h-[23px] text-xs  pt-[4px] pb-[4px] pl-[8px] pr-[8px] bg-[#e6e8ea] rounded-full">{{ badge }}</span>
    </button>
  </li>
</template>

<script setup lang="ts">
defineProps<{ 
  active?: boolean; 
  badge?: string; 
  image?: string; // Prop for image URL 
}>();
defineEmits<{ (e: "click"): void }>();
</script>