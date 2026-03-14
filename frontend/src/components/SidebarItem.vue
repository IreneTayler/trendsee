<template>
  <li>
    <button
      type="button"
      class="flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-left text-sm hover:bg-slate-800"
      :class="active ? 'bg-indigo-600 font-medium text-white' : ''"
      @click="$emit('click')"
    >
      <span><slot /></span>
      <span v-if="badge" class="ml-auto rounded-full bg-slate-700 px-2 py-0.5 text-xs">{{ badge }}</span>
    </button>
  </li>
</template>

<script setup lang="ts">
defineProps<{ active?: boolean; badge?: string }>();
defineEmits<{ (e: "click"): void }>();
</script>
