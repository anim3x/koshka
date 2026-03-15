<template>
  <main
    class="
      h-[82%]
      bg-white
      flex items-center justify-center">
    <div class="w-full max-w-sm min-w-50">
      <div class="relative">
        <input
          class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 border border-slate-200 rounded-md transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow
          pl-3 pr-28 py-2
          text-lg placeholder:text-base"
          placeholder="Всё о кино..." 
        >
        <button
          class="rounded border border-transparent text-center text-white transition-all shadow-sm hover:shadow active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none
          bg-blue-500 hover:bg-blue-400
          text-base
          absolute inset-y-2 right-2 flex items-center px-3 py-1"
          type="button"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="#fff"
            class="w-4 h-4 mr-2">
            <path
              fill-rule="evenodd"
              d="M10.5 3.75a6.75 6.75 0 1 0 0 13.5 6.75 6.75 0 0 0 0-13.5ZM2.25 10.5a8.25 8.25 0 1 1 14.59 5.28l4.69 4.69a.75.75 0 1 1-1.06 1.06l-4.69-4.69A8.25 8.25 0 0 1 2.25 10.5Z"
              clip-rule="evenodd" />
          </svg>
          Поиск
        </button> 
      </div>
    </div>
  </main>
</template>