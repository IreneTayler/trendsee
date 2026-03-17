<template>
  <li>
    <button
      type="button"
      class="group relative flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-left text-[16px] h-[40px] text-[#41616b] transition-colors duration-200 hover:bg-[#41616b14] hover:text-[#0f172a]"
      :class="active ? 'bg-[#2B31B3] text-white font-medium hover:bg-[#2B31B3] hover:text-white' : ''"
      @click="$emit('click')"
    >
      <span
        class="absolute left-0 top-1.5 h-[calc(100%-12px)] w-1 rounded-r-full bg-transparent transition-colors"
        :class="active ? 'bg-white/80' : 'group-hover:bg-[#2B31B3]/20'"
        aria-hidden="true"
      />
      <!-- Render image passed as prop -->
      <img
        v-if="image"
        :src="image"
        alt=""
        class="w-[20px] h-[20px] transition-opacity duration-200"
        :class="active ? 'opacity-100' : 'opacity-90 group-hover:opacity-100'"
      />

      <!-- Render text passed via default slot -->
      <span><slot /></span>

      <!-- Render badge if provided -->
      <span
        v-if="badge"
        class="ml-auto h-[23px] text-xs pt-[4px] pb-[4px] pl-[8px] pr-[8px] rounded-full"
        :class="active ? 'bg-white/20 text-white' : 'bg-[#D5D6F8] text-[#2B31B3]'"
      >
        {{ badge }}
      </span>
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