<template>
  <div class="space-y-1">
    <p class="mb-1 text-xs font-semibold tracking-wide text-slate-500 h-[29px]"><slot name="label" /></p>
    <ul class="space-y-1"><slot /></ul>
  </div>
</template>

<script setup lang="ts"></script>
