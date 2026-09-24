<template>
	<div class="min-h-screen bg-neutral-800 text-white px-4 py-4 flex flex-col">
		<header class="flex items-center justify-between">
			<button
				class="hover:bg-neutral-700 transition-colors duration-150 rounded-xl px-4 py-2 text-xl whitespace-nowrap"
			>
				Chat-GPT 5.2 ↓
			</button>

˜			<div class="flex items-center gap-2">
				<button
					class="hover:bg-neutral-700 transition-colors duration-150 inline-flex items-center justify-center rounded-full w-11 h-11 text-xl"
				>
					↓
				</button>
				<button
					class="hover:bg-neutral-700 transition-colors duration-150 inline-flex items-center justify-center rounded-full w-11 h-11 text-xl"
				>
					↓
				</button>
			</div>
		</header>

		<main class="flex-1 flex items-center justify-center">
			<p class="text-3xl font-bold text-center">Where should we begin?</p>
		</main>

		<footer class="pb-2">
			<div
				class="bg-neutral-700/80 rounded-full h-14 px-3 flex items-center gap-2"
			>
				<button
					class="hover:bg-neutral-600 transition-colors rounded-full w-10 h-10 flex items-center justify-center text-3xl"
				>
					+
				</button>

				<input
					class="grow bg-transparent px-3 py-2 outline-none placeholder:text-neutral-300"
					placeholder="Write a message…"
				/>

				<button
					class="hover:bg-neutral-600 transition-colors rounded-full w-10 h-10 flex items-center justify-center text-3xl"
				>
					+
				</button>
				<button
					class="hover:bg-neutral-600 transition-colors rounded-full w-10 h-10 flex items-center justify-center text-3xl"
				>
					+
				</button>
			</div>
		</footer>
	</div>
</template>
